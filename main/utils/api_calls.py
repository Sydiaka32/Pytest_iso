import time
import requests
import xml.etree.ElementTree as ET
from main.config import config


# AUTHENTICATION FUNCTIONS

def get_access_token():
    """
    Retrieves an access token for a regular user from Keycloak.
    Returns the access token as a string if successful, otherwise None.
    """
    url = f'{config.KEYCLOAK_URL}/realms/portal/protocol/openid-connect/token'  # Token endpoint URL
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': 'front-client',
        'username': config.USERNAME,
        'password': config.PASSWORD,
        'grant_type': 'password'
    }

    response = requests.post(url, headers=headers, data=data)  # Send POST request to get token
    if response.status_code == 200:
        json_data = response.json()
        access_token = json_data.get("access_token")
        if access_token:
            print("Access token retrieved successfully.")
            return access_token
        else:
            print("Access token not found in the response.")
            return None
    else:
        print(f"Failed to retrieve access token. Status code: {response.status_code}")
        return None


def get_access_token_admin():
    """
    Retrieves an access token for an admin user from Keycloak.
    Returns the token as a string if successful, otherwise None.
    """
    url = f'{config.KEYCLOAK_URL}/realms/backoffice/protocol/openid-connect/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': 'front-client',
        'username': config.ADMIN_USERNAME,
        'password': config.PASSWORD,
        'grant_type': 'password'
    }

    response = requests.post(url, headers=headers, data=data)  # Send POST request to get token
    if response.status_code == 200:
        json_data = response.json()
        access_token = json_data.get("access_token")
        if access_token:
            print("Access token retrieved successfully.")
            return access_token
        else:
            print("Access token not found in the response.")
            return None
    else:
        print(f"Failed to retrieve access token. Status code: {response.status_code}")
        return None


# ISO MESSAGE FUNCTIONS

def send_iso_file(file_path, return_raw_response=False):
    """
    Sends an ISO XML message to the emulator and optionally returns raw response.

    Args:
        file_path (str): Path to the ISO XML file.
        return_raw_response (bool): If True, return raw XML string response.

    Returns:
        str or None: NetworkReference value or raw response or None.
    """
    with open(file_path, 'rb') as f:
        xml_data = f.read()  # Read binary content of the XML file

    headers = {'Content-Type': 'application/xml'}

    try:
        # Send the ISO message to the emulator
        response = requests.post(config.ISO_EMULATOR_URL, data=xml_data, headers=headers, timeout=10)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        if return_raw_response:
            return response.text  # Optionally return raw XML response

        if response.status_code == 200:
            try:
                # Parse response and extract NetworkReference
                root = ET.fromstring(response.text)
                net_ref = root.find('.//NetworkReference')
                if net_ref is not None:
                    return net_ref.text
                else:
                    print("NetworkReference tag not found.")
                    return None
            except ET.ParseError as e:
                print(f"Failed to parse XML: {e}")
                return None
        else:
            print("Non-200 response received.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# RETRIEVE DATA FUNCTIONS

def get_clr_sys_ref_by_net_ref(net_ref, page=0, size=10):
    """
    Retrieves `clr_sys_ref` using the `net_ref` from the messaging-admin API.

    Args:
        net_ref (str): The Network Reference of related ISO message.
        page (int): Pagination page number.
        size (int): Number of results per page.

    Returns:
        str or None: The corresponding `clr_sys_ref` if found, else None.
    """
    url = f"{config.API_TECH_URL}/api/messaging/v1/messaging-admin/messages"
    params = {"search": net_ref, "page": page, "size": size}
    headers = {"X-USERINFO": config.X_USERINFO_ADMIN}

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()

    content = resp.json().get("content", [])
    if not content:
        return None

    return content[0].get("clr_sys_ref")  # Return only the clr_sys_ref of the first result


def get_messages_by_clr_sys_ref(clr_sys_ref, page=0, size=100):
    """
    Retrieves all messages associated with a specific `clr_sys_ref`.
    Includes a delay before sending the request.

    Args:
        clr_sys_ref (str): The Clearing System Reference to search for.
        page (int): Page number.
        size (int): Number of results per page (default 100 for full list).

    Returns:
        dict: JSON response containing message data.
    """
    time.sleep(8)  # Allow system some time to process the messages
    url = f"{config.API_TECH_URL}/api/messaging/v1/messaging-admin/messages"
    params = {"search": clr_sys_ref, "page": page, "size": size}
    headers = {"X-USERINFO": config.X_USERINFO_ADMIN}

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_transactions_by_clr_sys_ref(clr_sys_ref, page=0, size=20):
    """
    Retrieves transaction associated with a specific `clr_sys_ref`.

    Args:
        clr_sys_ref (str): The reference used to link transactions.
        page (int): Page number for pagination.
        size (int): Number of results per page.

    Returns:
        list: A list of transaction records.
    """
    url = f"{config.API_TECH_URL}/api/ledger/v1/ledger-admin/transactions"
    params = {
        "clr_sys_ref": clr_sys_ref,
        "page": page,
        "size": size,
    }
    headers = {
        "Accept": "*/*",
        "X-USERINFO": config.X_USERINFO_ADMIN,
    }

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json().get("content", [])  # Return the list of transactions
