import random
import string
from datetime import datetime, timedelta
import uuid


def generate_random_iban(country_code="AS"):
    """Generate random IBAN with specified country code"""
    check_digits = f"{random.randint(10, 99)}"
    account_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=22))
    return f"{country_code}{check_digits}{account_number}"


# General first names (mix of cultural origins)
FIRST_NAMES = [
    'Liam', 'Emma', 'Noah', 'Olivia', 'William', 'Ava', 'James', 'Isabella',
    'Oliver', 'Sophia', 'Benjamin', 'Charlotte', 'Elijah', 'Mia', 'Lucas',
    'Amelia', 'Mason', 'Harper', 'Logan', 'Evelyn', 'Alexander', 'Abigail',
    'Ethan', 'Emily', 'Jacob', 'Elizabeth', 'Michael', 'Mila', 'Daniel',
    'Ella', 'Henry', 'Avery', 'Jackson', 'Sofia', 'Sebastian', 'Camila',
    'Aiden', 'Aria', 'Matthew', 'Scarlett', 'Samuel', 'Victoria', 'David',
    'Madison', 'Joseph', 'Luna', 'Carter', 'Grace', 'Owen', 'Chloe',
    'Wyatt', 'Penelope', 'John', 'Layla', 'Jack', 'Riley', 'Luke', 'Zoey',
    'Jayden', 'Nora', 'Dylan', 'Lily', 'Grayson', 'Eleanor', 'Levi', 'Hannah',
    'Isaac', 'Lillian', 'Gabriel', 'Addison', 'Julian', 'Aubrey', 'Mateo',
    'Ellie', 'Anthony', 'Stella', 'Jaxon', 'Natalie', 'Lincoln', 'Zoe',
    'Joshua', 'Leah', 'Christopher', 'Hazel', 'Andrew', 'Violet', 'Theodore',
    'Aurora', 'Caleb', 'Savannah', 'Ryan', 'Audrey', 'Asher', 'Brooklyn',
    'Nathan', 'Bella', 'Thomas', 'Claire', 'Leo', 'Skylar'
]

# General surnames (mix of cultural origins)
SURNAMES = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
    'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez',
    'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
    'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark',
    'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King',
    'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green',
    'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell',
    'Carter', 'Roberts', 'Kim', 'Li', 'Singh', 'Patel', 'Wang', 'Chen',
    'Kumar', 'Ali', 'Zhang', 'Liu', 'Khan', 'Ahmed', 'Mohammed', 'Yang',
    'Wu', 'Huang', 'Park', 'Vargas', 'Silva', 'Fernandez', 'Rossi', 'Müller',
    'Schmidt', 'Dubois', 'Moreau', 'Ivanov', 'Smirnov', 'Kowalski', 'Nowak',
    'Nakamura', 'Sato', 'Yamamoto', 'Sokolov', 'Popov', 'Jansen', 'De Jong',
    'Visser', 'Andersson', 'Johansson', 'Nilsson', 'Garcia', 'Martinez'
]


def generate_full_name():
    """Generate a full name by randomly selecting a first and last name."""
    first = random.choice(FIRST_NAMES)
    last = random.choice(SURNAMES)
    full_name = f"{first} {last}"
    return full_name


def generate_random_amount(min=10, max=30):
    """Generate random currency amount"""
    return round(random.uniform(min, max), 2)


def generate_random_above_amount(min=1000, max=10000):
    """Generate random currency amount"""
    return round(random.uniform(min, max), 2)


def generate_random_below_amount(min=1, max=5):
    """Generate random currency amount"""
    return round(random.uniform(min, max), 2)


def generate_future_date(days_ahead=30):
    """Generate future date string in ISO format"""
    return (datetime.now() + timedelta(days=random.randint(1, days_ahead))).isoformat()


def generate_random_uetr():
    """Generate random UUID for UETR"""
    return str(uuid.uuid4())


def generate_current_date():
    """Generate random UUID for UETR"""
    # Generate current date in YYYY-MM-DD format
    return datetime.now().strftime("%Y-%m-%d")


def generate_purpose_code():
    """Pick a random purpose code"""
    purpose_codes = [
        "BONU", "CASH", "CBLK", "CCRD", "CORT", "DCRD", "DIVI", "DVPM", "EPAY",
        "FCIN", "FCOL", "GP2P", "GOVT", "HEDG", "ICCP", "IDCP", "INTC", "INTE",
        "LBOX", "LOAN", "MP2B", "MP2P", "OTHR", "PENS", "RPRE", "RRCT", "RVPM",
        "SALA", "SECU", "SSBE", "SUPP", "TAXS", "TRAD", "TREA", "VATX", "WHLD",
        "SWEP", "TOPG", "ZABA", "VOST", "FCDT", "CIPC", "CONC"
    ]
    return random.choice(purpose_codes)


def generate_random_remittance_info():
    """Generate remittance information text"""
    words = [
        ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8)))
        for _ in range(random.randint(2, 5))
    ]
    return ' '.join(words).strip()


def generate_transaction_id():
    """Generate random transaction ID"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=35))


def generate_incorrect_transaction_id():
    """Generate random incorrect transaction ID"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=37))


def generate_end_to_end_id():
    """Generate random end-to-end ID"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=35))


def generate_incorrect_end_to_end_id():
    """Generate random invalid end-to-end ID"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=36))


def generate_settlement_method():
    """Generate random settlement method"""
    return random.choice(["DNS", "RTGS"])


def generate_random_remittance_info_01(max_length=140):
    """Generate random remittance information (up to 140 characters)"""
    # Create a pool of possible characters including spaces and punctuation
    chars = string.ascii_letters + string.digits + ' /-.,#&'

    # Generate random length between 20 and max_length
    length = random.randint(20, max_length)

    # Create text with random words and separators
    elements = []
    while len(''.join(elements)) < length:
        word_length = random.randint(3, 12)
        word = ''.join(random.choices(chars.replace(' ', ''), k=word_length))
        elements.append(word)

        # Add space or separator with 30% probability
        if random.random() < 0.7 and len(elements) < (length // 3):
            elements.append(random.choice([' ', '-', '/', ', ']))

    # Join and truncate to exact length
    remittance_info = ''.join(elements)[:max_length]
    return remittance_info.strip()


def generate_random_iban_01():
    """Generate random IBAN with valid country code structure"""
    # List of country codes with IBAN specifications
    iban_specs = {
        # Country: (country_code, length, bban_pattern)
        'Germany': ('DE', 22, 'D', 18),
        'France': ('FR', 27, 'F', 23),
        'UK': ('GB', 22, 'B', 18),
        'Italy': ('IT', 27, 'T', 23),
        'Spain': ('ES', 24, 'S', 20),
        'Netherlands': ('NL', 18, 'N', 14),
    }

    # Select random country specification
    country_spec = random.choice(list(iban_specs.values()))
    country_code, total_length, bank_code, bban_length = country_spec

    # Generate valid check digits (00-99)
    check_digits = f"{random.randint(0, 99):02d}"

    # Generate Basic Bank Account Number (BBAN) according to country pattern
    bban = ''.join([
        # Bank code (country specific)
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=2)),
        # Random alphanumeric characters
        ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=bban_length - 2
        ))
    ])

    # Combine components
    return f"{country_code}{check_digits}{bban}"


def generate_invalid_iban():
    """
    Generate an invalid IBAN by taking a valid IBAN and modifying its check digits.
    The check digits are the 3rd and 4th characters (positions 2 and 3 in 0-indexed string).
    """
    valid_iban = generate_random_iban_01()
    # Extract current check digits
    current_check = valid_iban[2:4]

    # Choose a different pair of digits to "corrupt" the IBAN.
    # If the current check digits are not "00", use "00", otherwise use "99".
    invalid_check = "00" if current_check != "00" else "99"

    # Construct the invalid IBAN: country code + invalid check digits + rest of the IBAN
    invalid_iban = valid_iban[:2] + invalid_check + valid_iban[4:]
    return invalid_iban


def generate_biz_msg_idr(message_type_length=6, suffix_length=2):
    """
        Generate a business message identifier:
        Format: BizMsgIdr-{type}-{date}{suffix}
    """
    prefix = "BizMsgIdr"
    today = datetime.now().strftime("%Y%m%d")

    message_type = ''.join(random.choices(string.ascii_lowercase + string.digits, k=message_type_length))
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=suffix_length))

    return f"{prefix}-{message_type}-{today}{suffix}"
