import os
# Setting absolute path of the project
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML_FILE_PATH = os.path.join(PROJECT_DIR, 'my_generated_pacs_008', 'pacs_008.xml')

# API Endpoints and Constants
ISO_EMULATOR_URL = "https://iso-emulator.dev.xabeta.tech/admin/upload"
KEYCLOAK_URL = "https://keycloak.dev.xabeta.tech"
API_TECH_URL = "https://dev.xabeta.tech"
API_BASE_URL = "https://dev.xabeta.tech/"
API_DEV_URL = "https://api.dev.xabeta.tech"
X_USERINFO_ADMIN = ("eyJpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsI"
              "m5hbWUiOiJzd2FnZ2VyLXVzZXIiLCJlbWFpbCI6InN3YWdnZXItdXNlckB4YWJldGEuY29tI"
              "iwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFkbWluIl19LCJpc3MiOiJodHRwczovL2tleWNsb2FrLmRldi54YWJldGEudGVjaC"
              "9yZWFsbXMvYmFja29mZmljZSJ9")

# Sender data
USERNAME = "maxim.s@xabeta.com"
PASSWORD = "Xabeta_2024!"
XMI_SENDER = "XMBER007SAFF"
EXPECTED_SENDER_NAME = "Maksym"
ADMIN_USERNAME = "admin"

PLATFORM = "XXBTAHQRAECS"
SENDER = "XMBER007SAFF"
RECEIVER = "XMBER011BRFF"

# Predefined values for transaction verification and receiver data
EXPECTED_TRANSACTION_TYPE = "credit_transfer"
EXPECTED_RECEIVER_NAME = "Brazilian bank"
EXPECTED_CURRENCY = "SAR"
XMI_RECEIVER = "XMBER011BRFF"

from main.utils.transaction_data import TransactionData
transaction_data = TransactionData()
