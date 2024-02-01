# Import necessary libraries
import numpy as np
import joblib
from modules.ipcheck import check_having_IP_Address
from modules.checkurl import check_url_length, check_shortening_service, check_having_at_symbol, check_double_slash_redirecting, check_having_sub_domain, check_ssl_final_state, check_https_token_with_request, check_request_url, check_links_in_tags, check_url_of_anchor, check_sfh, check_submitting_to_email, check_redirect, check_iframe, check_google_index, check_links_pointing_to_page, check_statistical_report, check_domain_registration_length, get_domain_age, check_dns_security
from urllib.parse import urlparse
from colorama import Fore, Back, Style

# Load the trained model
model_filename = 'model/trained_model.joblib'
model = joblib.load(model_filename)

def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

url = 'https://thintry.com/'
# url_two = 'https://myphoneoffer.com/'
# having_ip = check_having_IP_Address(get_domain(url))
# url_length = check_url_length(url)
# is_shorted = check_shortening_service(url)
# having_at_symbol = check_having_at_symbol(url)
# double_slash_redirecting = check_double_slash_redirecting(url)
# having_sub_domain = check_having_sub_domain(url)
# ssl_final_state = check_ssl_final_state(url)
# https_token = check_https_token_with_request(url)
# request_url = check_request_url(url)
# url_anchor = check_url_of_anchor(url)
# links_in_tag = check_links_in_tags(url)
# sfh = check_sfh(url)
# submitting_email = check_submitting_to_email(url)
# is_redirect = check_redirect(url)
# is_containe_iframe = check_iframe(url)
# google_index = check_google_index(url)
# links_pointing = check_links_pointing_to_page(url)
# static_repo = check_statistical_report(url)

# # Prepare input data for prediction (exclude the "Index" column)
# new_data_values = np.array([
#     [having_ip, url_length, is_shorted, having_at_symbol, double_slash_redirecting, having_sub_domain, ssl_final_state, 1, -1, 1, https_token, request_url, url_anchor, links_in_tag, sfh, submitting_email, 1, is_redirect, 0, 1, 1, is_containe_iframe, 1, -1, -1, 0, google_index, links_pointing, static_repo, 1, -1]
#     # Add more rows as needed
# ])

having_ip = check_having_IP_Address(get_domain(url))
url_length = check_url_length(url)
is_shorted = check_shortening_service(url)
having_at_symbol = check_having_at_symbol(url)
double_slash_redirecting = check_double_slash_redirecting(url)
having_sub_domain = check_having_sub_domain(url)
ssl_final_state = check_ssl_final_state(url)
domain_registration_length = check_domain_registration_length(url)
favicon = -1
port = -1
https_token = check_https_token_with_request(url)
request_url = check_request_url(url)
url_of_anchor = check_url_of_anchor(url)
links_in_tags = check_links_in_tags(url)
sfh = check_sfh(url)
submitting_to_email = check_submitting_to_email(url)
abnormal_url = -1
redirect = check_redirect(url)
on_mouseover = -1
right_click = -1
popup_window = -1
iframe = check_iframe(url)
age_of_domain = get_domain_age(url)
dns_record = check_dns_security(url)
web_traffic = -1
page_rank = -1
google_index = check_google_index(url)
links_pointing_to_page = check_links_pointing_to_page(url)
statistical_report = check_statistical_report(url)

# print([having_ip, url_length, is_shorted, having_at_symbol, double_slash_redirecting, having_sub_domain, ssl_final_state, domain_registration_length, favicon, port, https_token, request_url, url_of_anchor, links_in_tags, sfh, submitting_to_email, abnormal_url, redirect, on_mouseover, right_click, popup_window, iframe, age_of_domain, dns_record, web_traffic, page_rank, google_index, links_pointing_to_page, statistical_report])

new_data_values = np.array([
    [having_ip, url_length, is_shorted, having_at_symbol, double_slash_redirecting, having_sub_domain, ssl_final_state, domain_registration_length, favicon, port, https_token, request_url, url_of_anchor, links_in_tags, sfh, submitting_to_email, abnormal_url, redirect, on_mouseover, right_click, popup_window, iframe, age_of_domain, dns_record, web_traffic, page_rank, google_index, links_pointing_to_page, statistical_report]
])


# having_IP_Address  { -1,1 }
# URL_Length   { 1,0,-1 }
# Shortining_Service { 1,-1 }
# having_At_Symbol   { 1,-1 }
# double_slash_redirecting { -1,1 }
# Prefix_Suffix  { -1,1 }
# having_Sub_Domain  { -1,0,1 }
# SSLfinal_State  { -1,1,0 }
# Domain_registeration_length { -1,1 } ///////////
# Favicon { 1,-1 }
# port { 1,-1 }
# HTTPS_token { -1,1 }
# Request_URL  { 1,-1 }
# URL_of_Anchor { -1,0,1 }
# Links_in_tags { 1,-1,0 }
# SFH  { -1,1,0 }
# Submitting_to_email { -1,1 }
# Abnormal_URL { -1,1 }
# Redirect  { 0,1 }
# on_mouseover  { 1,-1 }
# RightClick  { 1,-1 }
# popUpWidnow  { 1,-1 }
# Iframe { 1,-1 }
# age_of_domain  { -1,1 }
# DNSRecord   { -1,1 }
# web_traffic  { -1,0,1 }
# Page_Rank { -1,1 }
# Google_Index { 1,-1 }
# Links_pointing_to_page { 1,0,-1 }
# Statistical_report { -1,1 }

# Make predictions
predictions = model.predict(new_data_values)

# Display predictions
print(Fore.YELLOW + "Predictions:", predictions)

if  predictions[0] == 1:
    print(Fore.GREEN + "Trustfull Website.")
else:
    print(Fore.RED + "Untrustfull Website.")

print(Style.RESET_ALL)