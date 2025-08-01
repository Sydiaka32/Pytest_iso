# 📨 ISO API Testing with Pytest

This project focuses on automated testing of financial message formats such as `pacs.008` and `pacs.009` using Pytest. It validates proper API handling of XML messages, particularly for structure correctness and status acknowledgment.

## 🛠 Tech Stack

| Tool             | Description |
|------------------|-------------|
| `pytest`         | Python testing framework used for writing and running test cases |
| `requests`       | For making HTTP API calls to submit XML files |

## 📁 Project Structure

```
.
├── tests/
│   ├── test_pacs_008stp_valid.py
│   ├── test_pacs_008stp_incorrect_structure.py
│   ├── test_pacs_009_incorrect_structure.py
├── main/
│   ├── utils/
│   │   ├── api_calls.py
│   │   └── iso_file_utils.py
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the Project
```bash
git clone https://github.com/Sydiaka32/Pytest_iso.git
cd iso-api-tests
```

### 2. Create and Activate a Virtual Environment

#### Windows
```bash
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest tests/test_pacs_008stp_valid.py
```

## 📌 Notes

- The tests use parameterized fixtures (`pacs_008_iso_xml`, `pacs_009_iso_xml`) to load different XML variants.
- The `send_iso_file()` function abstracts HTTP request logic.

This project is licensed under the [MIT License](LICENSE).
