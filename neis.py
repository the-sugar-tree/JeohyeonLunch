import requests
import json
from datetime import datetime

SCHOOL_TYPE = "J10"
SCHOOL_CODE = 7530980


def get_meal_info(key, date=datetime.today().strftime("%Y%m%d")):
    url = (f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={key}"
           f"&Type=json&pIndex=1&pSize=1&ATPT_OFCDC_SC_CODE={SCHOOL_TYPE}&SD_SCHUL_CODE={SCHOOL_CODE}&MLSV_FROM_YMD={date}")

    response = requests.get(url)

    code = response.status_code
    value = response.text

    print(value)

    json_obj = json.loads(value)

    return json_obj['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].replace("<br/>", "\n")
