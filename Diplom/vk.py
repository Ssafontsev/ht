import requests
from pprint import pprint

with open('token.txt') as file_object:
    token = file_object.read().strip()
with open('yatoken.txt') as f:
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

        complete_list = res.json()['response']['items']
        photos_to_upload = []
        url_names = []
        for line in complete_list:
            photo_info = {}
            qty_likes = line['likes']['count']
            photo_date = line['date']
            biggest_photo = line['sizes'][-1]
            photo_name = f'{qty_likes}.jpg'
            for item in photos_to_upload:
                if item['file_name'] == photo_name:
                    photo_name = f'{qty_likes}_{photo_date}.jpg'
            url_names.append([biggest_photo['url'], photo_name])
            photo_info['file_name'] = photo_name
            photo_info['size'] = biggest_photo['type']
            print(photo_info)
            photos_to_upload.append(photo_info)

        return url_names

vk_client = VkUser(token, '5.130')
vk_client.get_photos_links()




# for link, name in vk_client.get_photos_links():
#     response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                              params={'path': name,
#                                      'url': link},
#                              headers={'Authorization': f'OAuth {yatoken}'})


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
