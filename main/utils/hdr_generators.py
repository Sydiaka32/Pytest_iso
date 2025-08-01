from main.config import config
import xml.etree.ElementTree as ET
from datetime import datetime
from main.utils.generate import generate_biz_msg_idr


def create_app_header(root, hdr_variant="pacs_008"):
    """Create the AppHdr section of the XML message based on the specified variant."""

    # Create the AppHdr root element with appropriate XML namespace
    app_hdr = ET.SubElement(root, "AppHdr", xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02")

    # Sender Financial Institution ID (FIId)
    fr = ET.SubElement(app_hdr, "Fr")
    fi_id = ET.SubElement(fr, "FIId")
    fin_instn_id = ET.SubElement(fi_id, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    ET.SubElement(othr, "Id").text = config.XMI_SENDER

    # Receiver Financial Institution ID (hardcoded)
    to = ET.SubElement(app_hdr, "To")
    fi_id = ET.SubElement(to, "FIId")
    fin_instn_id = ET.SubElement(fi_id, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    ET.SubElement(othr, "Id").text = "RAECS"  # Hardcoded receiver ID

    # Header metadata
    ET.SubElement(app_hdr, "BizMsgIdr").text = generate_biz_msg_idr()

    # Message Definition Identifier and Business Service based on the variant
    if hdr_variant == "pacs_008":
        ET.SubElement(app_hdr, "MsgDefIdr").text = "pacs.008.001.08"
        ET.SubElement(app_hdr, "BizSvc").text = "CTR"
    elif hdr_variant == "pacs_008stp":
        ET.SubElement(app_hdr, "MsgDefIdr").text = "pacs.008.001.08"
        ET.SubElement(app_hdr, "BizSvc").text = "STP"
    elif hdr_variant == "pacs_009":
        ET.SubElement(app_hdr, "MsgDefIdr").text = "pacs.009.001.08"
        ET.SubElement(app_hdr, "BizSvc").text = "CTR"

    # Creation date/time in ISO 8601 format
    ET.SubElement(app_hdr, "CreDt").text = datetime.now().isoformat()

    # Additional fixed header fields
    ET.SubElement(app_hdr, "PssblDplct").text = "false"
    ET.SubElement(app_hdr, "Prty").text = "NORM"
