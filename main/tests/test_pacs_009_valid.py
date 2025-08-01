import pytest
from main.utils.transaction_data import transaction_data
from main.config import config
from main.utils import api_calls
from main.utils.api_calls import get_clr_sys_ref_by_net_ref, \
    get_messages_by_clr_sys_ref, get_transactions_by_clr_sys_ref


# Parametrize test with a specific XML file marked as "valid" and of type "pacs_009"
@pytest.mark.parametrize("pacs_009_iso_xml", [("valid", "pacs_009")], indirect=True)
def test_pacs_009_valid(pacs_009_iso_xml):

    # Send the valid ISO XML file and retrieve the Network Reference (net_ref)
    net_ref = api_calls.send_iso_file(pacs_009_iso_xml)

    # Verify that network reference was received
    assert net_ref is not None, "No NetworkReference in response"
    print(f"\nTransaction processed successfully! NS_REF: {net_ref}")

    # Retrieve clr_sys_ref using net_ref
    clr_sys_ref = get_clr_sys_ref_by_net_ref(net_ref)
    assert clr_sys_ref is not None, "No clr_sys_ref in response"
    print(f"\nClr_sys_ref retrieved successfully! clr_sys_ref: {clr_sys_ref}")

    # Retrieve all messages related to this transaction using clr_sys_ref
    resp_data = get_messages_by_clr_sys_ref(clr_sys_ref)
    print(f"\nMessages: {resp_data}")

    # Extract message content list
    messages_scope = resp_data.get("content", [])
    print(f"\nMessages: {messages_scope}")

    # Validate message 0
    msg0 = messages_scope[0]
    print(f"\nMessages scope retrieved successfully! messages_scope: {msg0}")
    assert msg0["message_type"] == "pacs.002.001.10"
    assert msg0["sender_xmi"] == config.PLATFORM
    assert msg0["receiver_xmi"] == config.RECEIVER

    # Validate message 1
    msg1 = messages_scope[1]
    assert msg1["message_type"] == "pacs.002.001.10"
    assert msg1["sender_xmi"] == config.PLATFORM
    assert msg1["receiver_xmi"] == config.SENDER

    # Validate message 2
    msg2 = messages_scope[2]
    assert msg2["message_type"] == "pacs.002.001.10"
    assert msg2["sender_xmi"] == config.RECEIVER
    assert msg2["receiver_xmi"] == config.PLATFORM

    # Validate message 3
    msg3 = messages_scope[3]
    assert msg3["message_type"] == "pacs.009.001.08"
    assert msg3["sender_xmi"] == config.PLATFORM
    assert msg3["receiver_xmi"] == config.RECEIVER

    # Validate message 4
    msg4 = messages_scope[4]
    assert msg4["message_type"] == "pacs.009.001.08"
    assert msg4["sender_xmi"] == config.SENDER
    assert msg4["receiver_xmi"] == config.PLATFORM

    # Get the transaction history by clr_sys_ref and validate data
    transactions = get_transactions_by_clr_sys_ref(clr_sys_ref)
    assert transactions, "No transactions returned"

    # Expected transaction status
    expected_tx_status = "COMPLETED"
    tx = transactions[0]

    # Validate transaction status
    assert tx["status"] == expected_tx_status, \
        f"Expected status '{expected_tx_status}', got '{tx['status']}'"

    # Validate creditor (receiver) XMI
    assert tx["creditor"]["xmi"] == transaction_data.cdtr_xmi, \
        f"Expected creditor xmi '{transaction_data.cdtr_xmi}', got '{tx['creditor']['xmi']}'"

    # Validate creditor name
    assert tx["creditor"]["name"] == config.EXPECTED_RECEIVER_NAME, \
        f"Expected creditor name '{config.EXPECTED_RECEIVER_NAME}', got '{tx['creditor']['name']}'"

    # Validate debtor (sender) XMI
    assert tx["debtor"]["xmi"] == transaction_data.dbtr_xmi, \
        f"Expected debtor xmi '{transaction_data.dbtr_xmi}', got '{tx['debtor']['xmi']}'"

    # Validate debtor name
    assert tx["debtor"]["name"] == config.EXPECTED_SENDER_NAME, \
        f"Expected debtor name '{config.EXPECTED_SENDER_NAME}', got '{tx['debtor']['name']}'"

    # Validate currency
    assert tx["currency"] == config.EXPECTED_CURRENCY, \
        f"Expected currency '{config.EXPECTED_CURRENCY}', got '{tx['currency']}'"

    # Validate amount
    assert tx["amount"] == float(transaction_data.instd_amt), \
        f"Expected amount '{transaction_data.instd_amt}', got '{tx['amount']}'"
