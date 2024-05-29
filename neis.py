import requests
import json
from datetime import datetime

key = "KEY HERE"

url = "https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=" + key + "&Type=json&pIndex=1&pSize=1&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530980&MLSV_FROM_YMD=" + datetime.today().strftime("%Y%m%d")

response = requests.get(url)

code = response.status_code
value = response.text

##print("response code: " + str(code))
print(value)

json_obj = json.loads(value)

##print(json_obj['mealServiceDietInfo'][0]['head'][1]['RESULT']['CODE'])

print(json_obj['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].replace("<br/>", "\n"))
