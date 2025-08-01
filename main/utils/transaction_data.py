class TransactionData:
    """
    A data container class for storing information related to a financial transaction.
    This is often used for generating or parsing ISO messages.
    """

    def __init__(self):
        # Message-level identifiers and metadata
        self.msg_id = None  # Unique identifier for the message
        self.cre_dt_tm = None  # Creation date and time of the message
        self.nb_of_txs = None  # Number of transactions in the message

        # Settlement-related information
        self.settlm_acct_id = None  # Settlement account identifier
        self.sttlmn_type = None  # Settlement type (e.g., CLRG = clearing)

        # Payment identifiers
        self.instr_id = None  # Instruction ID: unique per instructing party
        self.end_to_end_id = None  # End-to-end ID: consistent between sender and receiver
        self.tx_id = None  # Transaction ID: used by the banks involved
        self.uetr = None  # Unique End-to-End Transaction Reference
        self.clr_sys_ref = None  # Clearing system reference (e.g., CHIPS ID)

        # Monetary details
        self.intr_bk_sttlm_amt = None  # Interbank settlement amount
        self.intr_bk_sttlm_dt = None  # Interbank settlement date
        self.ccy = None  # Currency of the transaction
        self.instd_amt = None  # Instructed amount (the amount instructed by the sender)

        # Debtor details
        self.dbtr_name = None  # Name of the debtor
        self.dbtr_acct_id = None  # Debtor's account identifier
        self.dbtr_xmi = None  # Debtor’s external messaging identifier (XMI)

        # Creditor details
        self.cdtr_xmi = None  # Creditor’s external messaging identifier (XMI)
        self.cdtr_name = None  # Name of the creditor
        self.cdtr_acct_id = None  # Creditor's account identifier

        # Additional payment information
        self.purp_cd = None  # Purpose code for the transaction (e.g., SALA for salary)
        self.rmt_info = None  # Remittance information (free text or structured)

        # Authorization & status
        self.access_token = None  # Token for authorized API access (if needed)
        self.transaction_status = None  # Status of the transaction (e.g., pending, completed)


# Global instance of the transaction data to be reused or filled in tests
transaction_data = TransactionData()
