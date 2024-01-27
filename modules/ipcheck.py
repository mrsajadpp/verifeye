# url_features.py

import socket
import re
# from getdomain import get_domain


def check_having_IP_Address(url):
    try:
        # Extract the domain from the URL
        domain = url

        print(domain)

        # Get the IP address of the domain
        ip_address = socket.gethostbyname(domain)
        print(ip_address)

        # Check if the IP address is present in the URL
        if ip_address:
            return 1  # Indicates having IP address
        else:
            return -1  # Indicates not having IP address
    except:
        return 0  # Error or invalid URL
