# Import necessary libraries
import numpy as np
import joblib
from modules.ipcheck import check_having_IP_Address
from modules.checkurl import check_url_length, check_shortening_service, check_having_at_symbol, check_double_slash_redirecting, check_having_sub_domain, check_ssl_final_state
from urllib.parse import urlparse

# Load the trained model
model_filename = 'model/trained_model.joblib'
model = joblib.load(model_filename)

def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

url = 'https://thintry.com/'
domain = check_having_IP_Address(get_domain(url))
length = check_url_length(url)
is_shorted = check_shortening_service(url)
having_at_symbol = check_having_at_symbol(url)
double_slash_redirecting = check_double_slash_redirecting(url)
having_sub_domain = check_having_sub_domain(url)
ssl_final_state = check_ssl_final_state(url)


# Prepare input data for prediction (exclude the "Index" column)
new_data_values = np.array([
    [domain, length, is_shorted, having_at_symbol, double_slash_redirecting, having_sub_domain, ssl_final_state, 1, -1, 1, 1, -1, 1, 0, -1, -1, 1, 1, 0, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 1, -1]
    # Add more rows as needed
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
print("Predictions:", predictions)
