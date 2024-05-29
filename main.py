from pathlib import Path
from instagrapi import Client
from datetime import datetime
import getpass

from generate_image import make_image

ACCOUNT_USERNAME = "kkr_developer"
ACCOUNT_PASSWORD = getpass.getpass("계정 비밀번호를 입력하세요: ")

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


def upload_story(file_name):
    print('스토리 업로드 중...')
    cl.photo_upload_to_story(
        Path('img/{}.png'.format(file_name))
    )
    print('스토리가 업로드 되었습니다!')


def main(message, file_name=datetime.today().strftime('%y%m%d')):
    make_image(message, file_name)
    upload_story(file_name)


if __name__ == '__main__':
    # main('Hello, World!')
    make_image('Hello, World!', '240529')
    upload_story('240529')
