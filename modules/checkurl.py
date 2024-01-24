# /usr/local/bin/python3.12 -m pip install
from getdomain import get_domain
from remhtttp import remove_protocol
import tldextract
import requests
import whois
import pythonwhois
from datetime import datetime


def check_url_length(url):
    try:
        # Extract the domain from the URL
        domain = get_domain(url)

        # Check if the URL length is greater than 54 characters
        if len(url) > 54:
            return 1  # Indicates URL length greater than 54
        else:
            return -1  # Indicates URL length less than or equal to 54
    except:
        return 0  # Error or invalid URL


def check_shortening_service(url):
    try:
        # Check if the URL contains common URL shortening service keywords
        shortening_keywords = ["bit.ly", "tinyurl", "goo.gl", "ow.ly", "t.co"]

        if any(keyword in url for keyword in shortening_keywords):
            return 1  # Indicates the presence of a URL shortening service
        else:
            return -1  # Indicates no URL shortening service
    except:
        return 0  # Error or invalid URL


def check_having_at_symbol(url):
    try:
        # Check if the '@' symbol is present in the URL
        if '@' in url:
            return 1  # Indicates the presence of '@' symbol
        else:
            return -1  # Indicates no '@' symbol
    except:
        return 0  # Error or invalid URL


def check_double_slash_redirecting(url):
    try:
        # Check if the double slash redirecting pattern is present in the URL
        out_url = remove_protocol(url)
        if "//" in out_url:
            return 1  # Indicates the presence of double slash redirecting
        else:
            return -1  # Indicates no double slash redirecting
    except:
        return 0  # Error or invalid URL


def check_having_sub_domain(url):
    try:
        # Extract the domain using tldextract
        extracted_info = tldextract.extract(url)
        subdomain = extracted_info.subdomain

        # Check if a subdomain is present
        if subdomain:
            return 1  # Indicates the presence of a subdomain
        else:
            return -1  # Indicates no subdomain
    except:
        return 0  # Error or invalid URL


def check_ssl_final_state(url):
    try:
        # Send a HEAD request to the URL to get SSL certificate information
        response = requests.head(url, verify=True)

        # Check if the response has a valid SSL certificate
        if response.ok:
            return 1  # Indicates a valid SSL certificate
        else:
            return -1  # Indicates an invalid SSL certificate
    except:
        return 0  # Error or invalid URL


def check_domain_registration_length(url):
    try:
        # Extract the domain from the URL
        domain = get_domain(url)

        print(domain)

        # Get WHOIS information for the domain
        details = pythonwhois.get_whois(domain)

        print(details)

        return 1

        # # Check if WHOIS information contains creation date
        # if 'creation_date' in domain_info:
        #     creation_date = domain_info['creation_date']
        #     print(creation_date)

        #     # Calculate the registration length in days
        #     if isinstance(creation_date, list):
        #         creation_date = creation_date[0]
        #     registration_length = (creation_date - datetime.now()).days

        #     print(registration_length)

        #     # Check if registration length is greater than a threshold (e.g., 365 days)
        #     if registration_length > 365:
        #         return 1  # Indicates a domain registered for a longer period
        #     else:
        #         return -1  # Indicates a domain registered for a shorter period
        # else:
        #     return 0  # WHOIS information does not contain creation date
    except:
        return 0  # Error or invalid URL


# Example usage:
url = "https://thintry.com"
result = check_domain_registration_length(url)

print(f"The Domain_registeration_length feature for {url} is: {result}")
