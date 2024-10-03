import ssl
import socket
import datetime
import requests

WEBSITES = [
    'sib.seal.or.id',
    'kemdikbud.go.id'
]


def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            # Extract the 'notAfter' field from the certificate
            not_after_str = cert['notAfter']
            # Convert the date string to a datetime object
            expiry_date = datetime.datetime.strptime(
                not_after_str, "%b %d %H:%M:%S %Y %Z")
            return expiry_date


def get_status(website):
    website = "https://" + website
    try:
        status = requests.get(website).status_code
        return "Working" if status == 200 else "Error 404"
    except requests.exceptions.RequestException as e:
        return "Connection Failed!!"


def main():
    web_status_dict = {website: get_status(website) for website in WEBSITES}

    print("Website Status:")
    for website, status in web_status_dict.items():
        expiry_date = get_ssl_expiry_date(website)
        print(f"Site: {website}")
        print(f"Connection status: {status}")
        print(f"SSL expiry date: {expiry_date.strftime('%Y-%m-%d')}")
        print()


if __name__ == "__main__":
    main()
