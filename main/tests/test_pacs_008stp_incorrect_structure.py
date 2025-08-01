import pytest
from main.utils.iso_file_utils import get_status_from_response
from main.utils import api_calls


# Parametrize test to use an ISO file with an intentionally incorrect structure
@pytest.mark.parametrize("pacs_008_iso_xml", [("incorrect_structure", "pacs_008stp")], indirect=True)
def test_pacs_008stp_incorrect_structure(pacs_008_iso_xml):

    # Send the ISO file and get the raw HTTP response
    response = api_calls.send_iso_file(pacs_008_iso_xml, return_raw_response=True)

    # Ensure the response is not empty
    assert response is not None, "No response returned from API"

    # Extract the status from the raw response (e.g. ACKED or NACKED)
    status = get_status_from_response(response)

    # Verify that the response status is NACKED due to incorrect structure
    assert status == "NACKED", \
        f"Expected status 'NACKED', but got '{status}'"
