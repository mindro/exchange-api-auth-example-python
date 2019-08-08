import requests, json
import base64
import urllib3
urllib3.disable_warnings()

api_url = "https://api-exchange.bankera.com"
token_endpoint = "/oauth/token?grant_type=client_credentials"
users_info_endpoint = "/users/info"
client_id = ""
client_secret = ""
auth_basic_header_pattern = "Basic {0}"
encodable_string = client_id + ":" + client_secret
encoded_credentials = base64.b64encode(bytes(encodable_string, "utf-8"))

encoded_cred_string = str(encoded_credentials, "utf-8");
auth_header = {'Authorization': auth_basic_header_pattern.format(encoded_cred_string)}

auth_response = requests.get(api_url+token_endpoint, headers=auth_header, verify=False)

response_json = json.loads(auth_response.text)

req_header = {'Authorization': response_json['token_type'].capitalize() + " " + response_json['access_token']}

user_info_response = requests.get(api_url+users_info_endpoint, headers=req_header, verify=False)

print(user_info_response)
