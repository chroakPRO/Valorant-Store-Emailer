import requests
import json
import testemail
from PIL import Image

uuid_list = []
skins_list = []

mail_user = ""
mail_pass = ""


# Fetching Store Items.
url = "https://pd.eu.a.pvp.net/store/v2/storefront/c82adb4f-ec9f-5b68-b728-03ac24b98808"
payload = ""
headers = {
    "X-Riot-Entitlements-JWT": "",
    "Authorization": "Bearer "
}


# Fetching Store Items
response = requests.request("GET", url, data=payload, headers=headers)
result = json.loads(response.text)
#print(result)
durationmin = result["SkinsPanelLayout"]["SingleItemOffersRemainingDurationInSeconds"] / 60

for i in result["SkinsPanelLayout"]["SingleItemOffers"]:
    #print(i)
    uuid_list.append(i)


#Fetching Skin Name
urlname = "https://valorant-api.com/v1/weapons/skins"
headers = {}

response = requests.request("GET", urlname, data=payload, headers=headers)
result = json.loads(response.text)

for i in uuid_list:
    for j in result["data"]:
        if str(j["levels"][0]["uuid"]) == str(i):
            skins_list.append((j["levels"][0]["displayName"], j["levels"][0]["displayIcon"]))




a = skins_list[0][1]
b = skins_list[1][1]
c = skins_list[2][1]
d = skins_list[3][1]

e = skins_list[0][0]
f = skins_list[1][0]
g = skins_list[2][0]
h = skins_list[3][0]

testemail.send_email(a,b,c,d,e,f,g,h)
