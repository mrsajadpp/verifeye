from getdomain import get_domain
from remhtttp import remove_protocol
import tldextract


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
