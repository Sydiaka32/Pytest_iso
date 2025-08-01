import pytest
import xml.etree.ElementTree as ET
from main.utils.body_generators import fill_xml_pacs_008, fill_xml_pacs_009
from main.utils.hdr_generators import create_app_header
from main.utils.iso_file_utils import create_pacs_008_iso_xml, set_xml_file_path, write_iso_xml, create_pacs_009_iso_xml


@pytest.fixture
def pacs_008_iso_xml(request):
    """
    Pytest fixture for generating a PACS.008 XML ISO message file.

    request.param can be either:
      - a single string (body_variant), in which case hdr_variant defaults to "pacs_008"
      - a 2-tuple (body_variant, hdr_variant)
    """
    # Unpack parameters from test call
    param = request.param
    if isinstance(param, (list, tuple)):
        body_variant, hdr_variant = param
    else:
        body_variant, hdr_variant = param, "pacs_008"

    # Create the root XML element and header
    root = ET.Element("Main")
    create_app_header(root, hdr_variant=hdr_variant)

    # Add ISO message structure
    doc = ET.SubElement(
        root,
        "Document",
        xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"
    )
    fi_to_fi = ET.SubElement(doc, "FIToFICstmrCdtTrf")

    # Populate the body of the message
    fill_xml_pacs_008(fi_to_fi, variant=body_variant)

    # Write the XML to a file and return the file path
    xml_path = set_xml_file_path(request.node.name)
    write_iso_xml(root, xml_path)
    return xml_path


@pytest.fixture
def pacs_009_iso_xml(request):
    """
    Pytest fixture for generating a PACS.009 XML ISO message file.

    request.param can be either:
      - a single string (body_variant), in which case hdr_variant defaults to "pacs_009"
      - a 2-tuple (body_variant, hdr_variant)
    """
    # Unpack parameters from test call
    param = request.param
    if isinstance(param, (list, tuple)):
        body_variant, hdr_variant = param
    else:
        body_variant, hdr_variant = param, "pacs_009"

    # Create the root XML element and header
    root = ET.Element("Main")
    create_app_header(root, hdr_variant=hdr_variant)

    # Add ISO message structure
    doc = ET.SubElement(
        root,
        "Document",
        xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08"
    )
    fi_cdt_trf = ET.SubElement(doc, "FICdtTrf")

    # Populate the body of the message
    fill_xml_pacs_009(fi_cdt_trf, variant=body_variant)

    # Write the XML to a file and return the file path
    xml_path = set_xml_file_path(request.node.name)
    write_iso_xml(root, xml_path)
    return xml_path
