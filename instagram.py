from pathlib import Path
from instagrapi import Client


class Instagram:
    def __init__(self, username, password):
        self.ACCOUNT_USERNAME = username
        self.ACCOUNT_PASSWORD = password

        self.cl = Client()
        print("Instagram 계정에 로그인합니다: " + self.ACCOUNT_USERNAME)
        self.cl.login(self.ACCOUNT_USERNAME, self.ACCOUNT_PASSWORD)
        print("Instagram 계정에 성공적으로 로그인했습니다: " + self.ACCOUNT_USERNAME)

    def upload_story(self, file_name):
        print('스토리 업로드 중...')
        self.cl.photo_upload_to_story(
            Path('img/{}.png'.format(file_name))
        )
        print('스토리가 업로드 되었습니다!')
