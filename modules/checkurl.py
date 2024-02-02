# /usr/local/bin/python3.12 -m pip install
# from getdomain import get_domain
# from remhtttp import remove_protocol
import tldextract
import requests
import whois
import datetime
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
        #     registration_length = (creation_date - datetime.datetime.now()).days

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


def check_submitting_to_email(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all form elements in the parsed HTML
        form_elements = soup.find_all('form')

        # Check if any form element contains an input field for email submission
        for form in form_elements:
            email_inputs = form.find_all('input', {'type': 'email'})
            if email_inputs:
                return 1  # Return -1 if an input field for email submission is found

        # If no form elements contain an input field for email submission, return 1
        return -1
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return -1  # Return 0 to indicate that Submitting_to_email is not applicable or an error occurred


def check_redirect(url):
    try:
        # Send an HTTP GET request to the URL with allow_redirects=False to prevent automatic redirection
        response = requests.get(url, allow_redirects=False, timeout=5)

        # Check if the response status code indicates a redirect (3xx status code)
        if 300 <= response.status_code < 400:
            return 1  # Return -1 if the URL redirects
        else:
            return -1  # Return 0 if the URL does not redirect
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        # Return 1 if the URL is not applicable (e.g., invalid URL or request error)
        return -1


def check_iframe(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all iframe elements in the parsed HTML
        iframe_elements = soup.find_all('iframe')

        # Check if any iframe elements were found
        if iframe_elements:
            return 1  # Return -1 if the website contains an iframe
        else:
            return -1  # Return 0 if the website does not contain an iframe
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        # Return 1 if the URL is not applicable (e.g., invalid URL or request error)
        return -1


def check_google_index(url):
    try:
        # Send a request to the Google Custom Search JSON API to search for the website URL
        response = requests.get(
            f"https://www.googleapis.com/customsearch/v1?key=AIzaSyCb5-OKQQ1uMnJ7FEr-TtMNzAKdacVviME&cx=432e43142f9084620&q=site:{url}"
        )

        # Check if the website URL appears in the search results
        if 'items' in response.json() and len(response.json()['items']) > 0:
            return 1  # Return 1 if the website is indexed by Google
        else:
            return -1  # Return -1 if the website is not indexed by Google
    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return -1  # Return 0 if there was an error during the check


def check_links_pointing_to_page(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor elements (<a>) with href attributes
        anchor_elements = soup.find_all('a', href=True)

        # # Initialize a counter for external links
        # external_links_count = 0

        # # Iterate through the anchor elements to count external links
        # for anchor in anchor_elements:
        #     # Parse the href attribute value to extract the domain of the link
        #     parsed_href = urlparse(anchor['href'])
        #     if parsed_href.netloc and parsed_href.netloc != urlparse(url).netloc:
        #         # Increment the counter if the link points to an external domain
        #         external_links_count += 1

        # Return the number of external links pointing to the page
        if(len(anchor_elements)):
            # print(1)
            return 1
        else:
            return -1
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return -1  # Return -1 to indicate an error occurred during the check


def check_statistical_report(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=5)

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Define keywords related to statistical reports
        statistical_keywords = ['statistical report',
                                'statistics', 'data analysis']

        # Search for the presence of keywords in the page content
        for keyword in statistical_keywords:
            if keyword in soup.get_text():
                return 1  # Return 1 if a statistical report is found based on keywords

        # If no keywords are found, return -1
        return -1  # Return -1 to indicate no statistical report found
    except requests.RequestException as e:
        return -1  # Return 0 to indicate an error occurred during the check


def check_domain_registration_length(url):
    try:
        domain = get_domain(url)
        response = whois.whois(domain)
        creation_date = response.creation_date
        expiration_date = response.expiration_date
        if creation_date and expiration_date:
            registration_length = (expiration_date[0] - creation_date[0]).days
            print(f"Domain registration length: {registration_length} days")
            if registration_length >= 366:
                return 1
            else:
                return -1
        else:
            print("Creation date or expiration date not found.")
            return -1
    except:
        return -1


def get_domain_age(url):
    try:
        domain = get_domain(url)
        print(domain)
        response = whois.whois(domain)
        creation_date = response.creation_date
        if creation_date:
            current_date = datetime.datetime.now()
            domain_age = (current_date - creation_date[0]).days
            print(f"Domain age: {domain_age} days")
            if (domain_age >= 230):
                return 1
            else:
                return -1
        else:
            print("Creation date not found.")
            return -1
    except:
        return -1

import dns.resolver

def check_dns_security(url):
    try:
        domain = get_domain(url)
        # Query the DNS records for the domain
        answers = dns.resolver.resolve(domain, 'DNSKEY', raise_on_no_answer=False)
        
        # Check if DNS records are secure
        if answers:
            print(f"DNS records for {domain} are secure.")
            return 1
        else:
            print(f"DNS records for {domain} are not secure.")
            return -1
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist.")
        return -1
    except:
        return -1


def check_favicon(url):
    try:
        # Send an HTTP GET request to the URL to retrieve its content
        response = requests.get(url, timeout=10)  # Increased timeout to 10 seconds

        # Raise an exception for HTTP errors (e.g., 404 Not Found)
        response.raise_for_status()

        # Parse the HTML content of the web page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags (hyperlinks) in the parsed HTML
        link_tags = soup.find_all('link')

        # Fav Icon Link
        fav_link = 'false'

        # Check each anchor tag for the 'icon' rel attribute
        for tag in link_tags:
            rel = tag.get('rel')
            if rel and 'icon' in rel:
                href = tag.get('href')
                if href:
                    fav_link = href
                    return 1  # Return 1 if a suspicious pattern is found
                else:
                    fav_link = 'false'
                    return -1  # Return -1 if no suspicious pattern is found

        # If no 'icon' rel attribute is found in any link tag
        if(fav_link.startswith("./") or fav_link.startswith("/") or fav_link.startswith(url)):
            return 1
        else:
            return -1

    except requests.exceptions.Timeout:
        # Handle timeout errors separately
        print("The request timed out")
        return 0  # Return 0 for timeout errors

    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        print(f"An error occurred: {e}")
        return 0  # Return 0 for other request exceptions
