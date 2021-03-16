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
            'user_id': user_id,
            'extended': 1
        }
        res = requests.get(followers_url, params={**self.params, **followers_params})
        photos_list = res.json()['response']['items']
        photos_to_upload = []
        url_and_names_to_upload = []
        for photo in photos_list:
            about_photo = {}
            quantity_likes = photo['likes']['count']
            photo_date = photo['date']
            max_size_photo = photo['sizes'][-1]
            photo_name = f'{quantity_likes}.jpg'
            for item in photos_to_upload:
                if item['file_name'] == photo_name:
                    photo_name = f'{quantity_likes}_{photo_date}.jpg'
            url_and_names_to_upload.append([max_size_photo['url'], photo_name])
            about_photo['file_name'] = photo_name
            about_photo['size'] = max_size_photo['type']
            photos_to_upload.append(about_photo)
        return url_and_names_to_upload

vk_client = VkUser(token, '5.130')
vk_client.get_photos_links()




for link, name in vk_client.get_photos_links():
    response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                             params={'path': name,
                                     'url': link},
                             headers={'Authorization': f'OAuth {yatoken}'})


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
