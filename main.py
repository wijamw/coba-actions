import ssl
import socket
import datetime

def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            # Extract the 'notAfter' field from the certificate
            not_after_str = cert['notAfter']
            # Convert the date string to a datetime object
            expiry_date = datetime.datetime.strptime(not_after_str, "%b %d %H:%M:%S %Y %Z")
            return expiry_date

# Example usage:
hostname = "sib.seal.or.id"
expiry_date = get_ssl_expiry_date(hostname)
print(f"SSL certificate for {hostname} expires on: {expiry_date}")
