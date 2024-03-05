import re
from main import get_ssl_expiry_date

def test_ssl_expiry_date_format():
    hostname = "sib.seal.or.id"  # Change to a real domain
    expiry_date = get_ssl_expiry_date(hostname)
    
    # Check if expiry date is in the correct format (YYYY-MM-DD HH:MM:SS)
    assert re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", str(expiry_date)) is not None

def test_hostname_format():
    # Check if hostname is in the correct format
    hostname = "sib.seal.or.id"  # Change to a real domain
    assert re.match(r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$", hostname) is not None
