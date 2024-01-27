# /usr/local/bin/python3.12 -m pip install
# from getdomain import get_domain
# from remhtttp import remove_protocol
import tldextract
import requests
import whois
# import pythonwhois
from datetime import datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def remove_protocol(url):
    if url.startswith("https://"):
        return url[len("https://"):]
    elif url.startswith("http://"):
        return url[len("http://"):]
    else:
        return url


def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


def check_url_length(url):
    try:
        # Extract the domain from the URL
        domain = get_domain(url)

        # Check if the URL length is greater than 54 characters
        if len(domain) > 54:
            return -1  # Indicates URL length greater than 54
        else:
            return 1  # Indicates URL length less than or equal to 54
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


# Coding loading .........................

# def check_domain_registration_length(url):
#     # try:
#         # Extract the domain from the URL
#         domain = get_domain(url)

#         print(domain)

#         # Get WHOIS information for the domain
#         details = pythonwhois.get_whois(domain)

#         print(details)

#         return 1

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
    # except:
    #     return 0  # Error or invalid URL

def check_https_token_with_request(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url, timeout=5)

        # Check if the response URL contains the HTTPS token
        starts = response.url.startswith("https://")
        print(response.url)
        if (starts):
            return 1
        else:
            return -1

    except:
        return 0


def check_request_url(url):
    try:
        # Send an HTTP HEAD request to the URL to check its headers
        response = requests.head(url, timeout=5)

        # Check if the response status code indicates success (2xx)
        if response.status_code // 100 == 2:
            # Add your custom criteria for a valid request URL here
            # For example, check if the server responds with a valid content type
            # valid_content_types = ['text/html', 'application/json']
            # content_type = response.headers.get('content-type')
            return 1
        else:
            # Handle non-success status codes if needed
            return -1
    except:
        return 0


def check_url_of_anchor(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags (hyperlinks) in the parsed HTML
        anchor_tags = soup.find_all('a')

        # Check each anchor tag for suspicious attributes or patterns
        for tag in anchor_tags:
            href = tag.get('href')
            if href:
                # Add your custom checks for the URL_of_Anchor feature here
                # For example, check if the href attribute contains suspicious patterns
                if 'javascript:' in href or 'data:' in href:
                    return -1  # Return False if a suspicious pattern is found

        # If no suspicious patterns are found in any anchor tags, return True
        return 1
    except:
        return 0


def check_links_in_tags(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all relevant HTML tags that may contain links
        relevant_tags = ['a', 'img', 'link', 'script']

        # Initialize a counter for the number of links found
        links_count = 0

        # Iterate over each relevant tag to count the number of links
        for tag_name in relevant_tags:
            tags = soup.find_all(tag_name)
            for tag in tags:
                # For 'a' tags, check the 'href' attribute
                if tag_name == 'a':
                    if tag.get('href'):
                        links_count += 1
                # For 'img' tags, check the 'src' attribute
                elif tag_name == 'img':
                    if tag.get('src'):
                        links_count += 1
                # For 'link' tags, check the 'href' attribute
                elif tag_name == 'link':
                    if tag.get('href'):
                        links_count += 1
                # For 'script' tags, check the 'src' attribute
                elif tag_name == 'script':
                    if tag.get('src'):
                        links_count += 1

        # Return the total number of links found within relevant tags
        return links_count
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return -1  # Return -1 to indicate an error

def check_sfh(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all form elements in the parsed HTML
        form_elements = soup.find_all('form')

        # Check if any form element has an action attribute pointing to an external URL
        for form in form_elements:
            action = form.get('action')
            if action and ('http://' in action.lower() or 'https://' in action.lower()):
                return -1  # Return -1 if an external URL is found in the form action

        # If no form elements have an action attribute pointing to an external URL, return 1
        return 1
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return 0  # Return 0 to indicate that SFH is not applicable or an error occurred