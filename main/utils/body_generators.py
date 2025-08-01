from main.config import config
import xml.etree.ElementTree as ET
from main.utils.transaction_data import transaction_data
from datetime import datetime
from main.utils.generate import (
    generate_random_iban_01,
    generate_random_remittance_info_01,
    generate_full_name,
    generate_random_amount,
    generate_purpose_code,
    generate_end_to_end_id,
    generate_transaction_id,
    generate_random_uetr,
    generate_current_date,
)


def fill_xml_pacs_008(parent, variant="valid"):
    """
    Fills the XML tree with a PACS.008 message.
    Args:
        parent: The root XML element to append the data to.
        variant: Controls the validity or structure of the XML (e.g., "valid", "invalid", "incorrect_structure").
    """
    # Create group header section (GrpHdr)
    grp_hdr = ET.SubElement(parent, "GrpHdr")
    msg_id = ET.SubElement(grp_hdr, "MsgId")
    transaction_data.msg_id = msg_id.text = "djufhJCnoC6mm1xNMf"  # Static here,because generated on emulator processing
    cre_dt_tm = ET.SubElement(grp_hdr, "CreDtTm")
    cre_dt_tm.text = datetime.now().isoformat()  # Current ISO datetime
    ET.SubElement(grp_hdr, "NbOfTxs").text = "1"

    # Settlement information (SttlmInf)
    sttlm_inf = ET.SubElement(grp_hdr, "SttlmInf")
    ET.SubElement(sttlm_inf, "SttlmMtd").text = "CLRG"
    sttlm_acct = ET.SubElement(sttlm_inf, "SttlmAcct")
    id = ET.SubElement(sttlm_acct, "Id")
    othr = ET.SubElement(id, "Othr")
    settlm_acct_id = ET.SubElement(othr, "Id")
    if variant == "invalid":
        transaction_data.settlm_acct_id = settlm_acct_id.text = f"{config.XMI_SENDER}_CLR_M_BRL_NOM"
    else:
        transaction_data.settlm_acct_id = settlm_acct_id.text = f"{config.XMI_SENDER}_CLR_M_SAR_NOM"

    # Credit transfer transaction information (CdtTrfTxInf)
    cdt_trf_tx_inf = ET.SubElement(parent, "CdtTrfTxInf")

    # Payment identification
    pmt_id = ET.SubElement(cdt_trf_tx_inf, "PmtId")
    instr_id = ET.SubElement(pmt_id, "InstrId")
    transaction_data.instr_id = instr_id.text = "InstrId-pacs778-20241025a"
    end_to_end_id = ET.SubElement(pmt_id, "EndToEndId")
    transaction_data.end_to_end_id = end_to_end_id.text = generate_end_to_end_id()
    tx_id = ET.SubElement(pmt_id, "TxId")
    transaction_data.tx_id = tx_id.text = generate_transaction_id()
    uetr = ET.SubElement(pmt_id, "UETR")
    transaction_data.uetr = uetr.text = generate_random_uetr()

    # Payment type information
    pmt_tp_inf = ET.SubElement(cdt_trf_tx_inf, "PmtTpInf")
    ctgy_purp = ET.SubElement(pmt_tp_inf, "CtgyPurp")
    sttlmn_type = ET.SubElement(ctgy_purp, "Cd")
    transaction_data.sttlmn_type = sttlmn_type.text = "DNS"

    # Settlement amount
    intr_bk_sttlm_amt = ET.SubElement(cdt_trf_tx_inf, "SttlmAmt", Ccy="SAR")
    transaction_data.intr_bk_sttlm_amt = intr_bk_sttlm_amt.text = str(generate_random_amount())

    # Settlement date (skipped if incorrect_structure)
    if variant != "incorrect_structure":
        intr_bk_sttlm_dt = ET.SubElement(cdt_trf_tx_inf, "SttlmDt")
        transaction_data.intr_bk_sttlm_dt = intr_bk_sttlm_dt.text = generate_current_date()
    else:
        transaction_data.intr_bk_sttlm_dt = None

    # Instructed amount
    instd_amt = ET.SubElement(cdt_trf_tx_inf, "InstdAmt", Ccy="SAR")
    transaction_data.instd_amt = instd_amt.text = transaction_data.intr_bk_sttlm_amt
    ET.SubElement(cdt_trf_tx_inf, "ChrgBr").text = "DEBT"

    # Instructing and instructed agents
    instg_agt = ET.SubElement(cdt_trf_tx_inf, "InstgAgt")
    fin_instn_id = ET.SubElement(instg_agt, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    ET.SubElement(othr, "Id").text = config.XMI_SENDER

    instd_agt = ET.SubElement(cdt_trf_tx_inf, "InstdAgt")
    fin_instn_id = ET.SubElement(instd_agt, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    ET.SubElement(othr, "Id").text = config.XMI_RECEIVER

    # Debtor information
    ultmt_dbtr = ET.SubElement(cdt_trf_tx_inf, "UltmtDbtr")
    ET.SubElement(ultmt_dbtr, "Nm").text = "UltmtDbtr Name"
    ET.SubElement(ultmt_dbtr, "CtryOfRes").text = "AR"

    dbtr = ET.SubElement(cdt_trf_tx_inf, "Dbtr")
    dbtr_name = ET.SubElement(dbtr, "Nm")
    transaction_data.dbtr_name = dbtr_name.text = generate_full_name()
    pstl_adr = ET.SubElement(dbtr, "PstlAdr")
    ET.SubElement(pstl_adr, "SubDept").text = "SubDept"
    ET.SubElement(pstl_adr, "Room").text = "Room"
    ET.SubElement(pstl_adr, "PstCd").text = "Postal Code"
    ET.SubElement(pstl_adr, "TwnNm").text = "Town Name"
    ET.SubElement(pstl_adr, "TwnLctnNm").text = "Town Location Name"
    ET.SubElement(pstl_adr, "CtrySubDvsn").text = "Country Subdivision"
    ET.SubElement(pstl_adr, "Ctry").text = "BR"

    # Debtor account
    dbtr_acct = ET.SubElement(cdt_trf_tx_inf, "DbtrAcct")
    id = ET.SubElement(dbtr_acct, "Id")
    dbtr_acct_id = ET.SubElement(id, "IBAN")
    transaction_data.dbtr_acct_id = dbtr_acct_id.text = generate_random_iban_01()

    # Debtor agent
    dbtr_agt = ET.SubElement(cdt_trf_tx_inf, "DbtrAgt")
    fin_instn_id = ET.SubElement(dbtr_agt, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    dbtr_xmi = ET.SubElement(othr, "Id")
    transaction_data.dbtr_xmi = dbtr_xmi.text = config.XMI_SENDER

    # Creditor agent
    cdtr_agt = ET.SubElement(cdt_trf_tx_inf, "CdtrAgt")
    fin_instn_id = ET.SubElement(cdtr_agt, "FinInstnId")
    othr = ET.SubElement(fin_instn_id, "Othr")
    cdtr_xmi = ET.SubElement(othr, "Id")
    transaction_data.cdtr_xmi = cdtr_xmi.text = config.XMI_RECEIVER

    # Creditor information
    cdtr = ET.SubElement(cdt_trf_tx_inf, "Cdtr")
    cdtr_name = ET.SubElement(cdtr, "Nm")
    transaction_data.cdtr_name = cdtr_name.text = generate_full_name()
    pstl_adr = ET.SubElement(cdtr, "PstlAdr")
    ET.SubElement(pstl_adr, "StrtNm").text = "Street Name"
    ET.SubElement(pstl_adr, "BldgNm").text = "Building Number"
    ET.SubElement(pstl_adr, "PstCd").text = "Postal Code"
    ET.SubElement(pstl_adr, "TwnNm").text = "Town Name"
    ET.SubElement(pstl_adr, "Ctry").text = "SA"

    # Creditor account
    cdtr_acct = ET.SubElement(cdt_trf_tx_inf, "CdtrAcct")
    id = ET.SubElement(cdtr_acct, "Id")
    cdtr_acct_id = ET.SubElement(id, "IBAN")
    transaction_data.cdtr_acct_id = cdtr_acct_id.text = generate_random_iban_01()

    # Purpose code
    purp = ET.SubElement(cdt_trf_tx_inf, "Purp")
    purp_cd = ET.SubElement(purp, "Cd")
    transaction_data.purp_cd = purp_cd.text = generate_purpose_code()

    # Remittance info
    rmt_inf = ET.SubElement(cdt_trf_tx_inf, "RmtInf")
    rmt_info = ET.SubElement(rmt_inf, "Ustrd")
    transaction_data.rmt_info = rmt_info.text = generate_random_remittance_info_01()


def fill_xml_pacs_009(parent, variant="valid"):
    """
    Fills the XML tree with a PACS.009 message.
    Args:
        parent: The root XML element to append the data to.
        variant: Controls validity/structure for testing purposes.
    """
    # Group Header
    grp_hdr = ET.SubElement(parent, "GrpHdr")
    msg_id = ET.SubElement(grp_hdr, "MsgId")
    transaction_data.msg_id = msg_id.text = "pacs009MsgId12345"
    cre_dt_tm = ET.SubElement(grp_hdr, "CreDtTm")
    cre_dt_tm.text = datetime.now().isoformat()
    ET.SubElement(grp_hdr, "NbOfTxs").text = "1"

    # Settlement Information
    sttlm_inf = ET.SubElement(grp_hdr, "SttlmInf")
    ET.SubElement(sttlm_inf, "SttlmMtd").text = "CLRG"
    sttlm_acct = ET.SubElement(sttlm_inf, "SttlmAcct")
    id = ET.SubElement(sttlm_acct, "Id")
    othr = ET.SubElement(id, "Othr")
    settlm_acct_id = ET.SubElement(othr, "Id")
    if variant == "invalid":
        transaction_data.settlm_acct_id = settlm_acct_id.text = f"{config.XMI_SENDER}_CLR_M_BRL_NOM"
    else:
        transaction_data.settlm_acct_id = settlm_acct_id.text = f"{config.XMI_SENDER}_CLR_M_SAR_NOM"

    # Transaction Info
    cdt_trf_tx_inf = ET.SubElement(parent, "CdtTrfTxInf")
    pmt_id = ET.SubElement(cdt_trf_tx_inf, "PmtId")
    instr_id = ET.SubElement(pmt_id, "InstrId")
    transaction_data.instr_id = instr_id.text = "InstrId-pacs009-20241025b"
    end_to_end_id = ET.SubElement(pmt_id, "EndToEndId")
    transaction_data.end_to_end_id = end_to_end_id.text = generate_end_to_end_id()
    tx_id = ET.SubElement(pmt_id, "TxId")
    transaction_data.tx_id = tx_id.text = generate_transaction_id()
    uetr = ET.SubElement(pmt_id, "UETR")
    transaction_data.uetr = uetr.text = generate_random_uetr()

    pmt_tp_inf = ET.SubElement(cdt_trf_tx_inf, "PmtTpInf")
    ctgy_purp = ET.SubElement(pmt_tp_inf, "CtgyPurp")
    sttlmn_type = ET.SubElement(ctgy_purp, "Cd")
    transaction_data.sttlmn_type = sttlmn_type.text = "DNS"

    # Settlement Amount & Date
    intr_bk_sttlm_amt = ET.SubElement(cdt_trf_tx_inf, "SttlmAmt", Ccy="SAR")
    transaction_data.intr_bk_sttlm_amt = intr_bk_sttlm_amt.text = str(generate_random_amount())
    transaction_data.instd_amt = transaction_data.intr_bk_sttlm_amt

    if variant != "incorrect_structure":
        intr_bk_sttlm_dt = ET.SubElement(cdt_trf_tx_inf, "SttlmDt")
        transaction_data.intr_bk_sttlm_dt = intr_bk_sttlm_dt.text = generate_current_date()
    else:
        transaction_data.intr_bk_sttlm_dt = None
