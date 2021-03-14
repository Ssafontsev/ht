import requests
from pprint import pprint

with open('Diplom/token.txt') as file_object:
    token = file_object.read().strip()
with open('Diplom/yatoken.txt') as f:
    yatoken = f.read().strip()

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version,

        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']

    def get_photos_links(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'photos.get'
        followers_params = {
            'album_id': 'profile',
            'count': 10,
            'user_id': user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params}).json()['response']['items']
        dict_url = {}
        list_url = []
        for line in res:
            dict_url.update(line)
            list_url.append(dict_url['sizes'][-1]['url'])
            # pprint(line)

        return list_url

vk_client = VkUser(token, '5.130')
vk_client.get_photos_links()
num = 0
for link in vk_client.get_photos_links():

    num += 1
    response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                        params={'path': num,
                                'url': link},
                        headers={'Authorization': f'OAuth {yatoken}'})



# for link in vk_client.get_photos_links():
#     with open(link, 'rb') as f:
#         requests.post(href, files={'file': f})


# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загружает файл file_path на яндекс диск"""
#         file_name = vk_client.get_photos_links()#file_path.split('/')[-1]
#         token = self.token
#         response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                                 params={'path': file_name},
#                                 headers={'Authorization': f'OAuth {token}'})
#         href = response.json()['href']
#         with open(file_path, 'rb') as f:
#             requests.put(href, files={'file': f})
#         if response.status_code == 200:
#             print('Успешная выгрузка файла')
#         return
#
# # if __name__ == '__main__':
# uploader = YaUploader(yatoken)
# uploader.upload(vk_client.get_photos_links())
