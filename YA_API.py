import requests

OAUTH_TOKEN = ''
HOST = 'https://cloud-api.yandex.net/v1/disk/resources/'


class YaApi:
    
    def create_folder(self):
        res = requests.put(HOST, params={'path': 'HomeWork'}, headers={'Authorization': OAUTH_TOKEN})
        return res.status_code

    def delete_folder(self):
        delete_res = requests.delete(HOST, params={'path': 'HomeWork'}, headers={'Authorization': OAUTH_TOKEN})


if __name__ == '__main__':
    ya_api = YaApi()
    if ya_api.create_folder() == 409:
        ya_api.delete_folder()
        ya_api.create_folder()
        print('Папка создана')
    else:
        print('Папка создана')
    
