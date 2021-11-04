import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": 'Python tests/test 1.txt', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        request_code = requests.put(href, data=open(file_path, 'rb')).status_code
        return request_code


if __name__ == '__main__':
    path_to_file = 'test.txt'
    ya_token = ...
    uploader = YaUploader(ya_token)
    print(uploader.upload(path_to_file))
