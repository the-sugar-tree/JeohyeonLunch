from generate_image import make_image
from instagram import Instagram
from neis import get_meal_info
from datetime import datetime

import schedule
import time

DEBUG = False

with open('secrets', 'r', encoding='utf-8') as f:
    key = f.readline().strip()
    password = f.readline().strip()

insta = Instagram("kkr_developer", password)

weekdays = ['월', '화', '수', '목', '금']


def do_today():
    today = datetime.today()
    today_str = today.strftime("%Y%m%d")
    make_image(f"{today.month}월 {today.day}일 ({weekdays[today.weekday()]})\n"+get_meal_info(key), today_str)
    insta.upload_story(today_str)


if __name__ == '__main__':
    if DEBUG:
        do_today()
    else:
        schedule.every().day.at("08:00").do(do_today)
        while True:
            schedule.run_pending()
            time.sleep(1)
