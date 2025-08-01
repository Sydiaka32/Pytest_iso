import os
import xml.etree.ElementTree as ET
import pytest
from main.utils.body_generators import fill_xml_pacs_008, fill_xml_pacs_009
from main.utils.hdr_generators import create_app_header


def set_xml_file_path(test_name):
    """
    Returns a file path under the 'my_generated_iso' directory of the 'main' package,
    named after the pytest test function.
    """
    # Determine the 'main' package directory (parent of this utils folder)
    current_dir = os.path.dirname(__file__)
    main_pkg_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Build the target directory under 'main'
    xml_dir = os.path.join(main_pkg_dir, 'my_generated_iso')
    os.makedirs(xml_dir, exist_ok=True)

    # Return the full path for the test
    return os.path.join(xml_dir, f"{test_name}.xml")


def write_iso_xml(root, xml_file_path):
    """
    Write the ElementTree 'root' to disk at 'xml_file_path', with pretty indentation.
    Returns the path that was written.
    """
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)
    return xml_file_path

def create_pacs_008_iso_xml(variant="valid", hdr_variant="default"):
    """
    Creates a PACS.008 ISO XML structure using the provided body and header variants.
    """
    # Root element for ISO envelope
    root = ET.Element("BizMsgEnvlp")

    # Add application header to the root
    create_app_header(root, hdr_variant=hdr_variant)

    # Create the Document element with PACS.008 namespace
    document = ET.SubElement(
        root,
        "Document",
        xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"
    )

    # Add the message-specific element
    fi_to_fi_cstmr_cdt_trf = ET.SubElement(document, "FIToFICstmrCdtTrf")

    # Fill in the body with the selected variant
    fill_xml_pacs_008(fi_to_fi_cstmr_cdt_trf, variant=variant)

    return root

def create_pacs_009_iso_xml(variant="valid"):
    """
    Creates a PACS.009 ISO XML structure using the provided variant.
    """
    # Root element for ISO envelope
    root = ET.Element("BizMsgEnvlp")

    # Add default application header
    create_app_header(root)

    # Create the Document element with PACS.009 namespace
    document = ET.SubElement(
        root,
        "Document",
        xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08"
    )

    # Add the message-specific element
    fi_cdt_trf = ET.SubElement(document, "FICdtTrf")

    # Fill in the body with the selected variant
    fill_xml_pacs_009(fi_cdt_trf, variant=variant)

    return root


def get_status_from_response(response_text):
    """
    Extracts and returns the <Status> value from an XML response string.
    Returns None if parsing fails or if the <Status> element is not found.
    """
    try:
        root = ET.fromstring(response_text)
        status = root.find('.//Status')  # Search for the Status tag anywhere
        return status.text if status is not None else None
    except ET.ParseError:
        return None


def assert_pair_exists(msgs, message_type, sender_xmi, receiver_xmi):
    """
    Assert that a message with the given type and XMI values exists in the list.
    If not found, the test fails.
    """
    # Iterate through each message dict in the list
    for m in msgs:
        print(
            m["message_type"],
            m["sender_xmi"],
            m["receiver_xmi"]
        )
        # Build a tuple of the three fields from the message
        actual = (m["message_type"], m["sender_xmi"], m["receiver_xmi"])

        # If it matches the expected triple, we’re done—return quietly
        if actual == (message_type, sender_xmi, receiver_xmi):
            return

    # If we fell out of the loop, we never saw the expected triple—fail the test
    pytest.fail(
        f"No message found with message_type={message_type}, "
        f"sender_xmi={sender_xmi}, receiver_xmi={receiver_xmi}"
    )
