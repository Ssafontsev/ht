import requests
import time
from tqdm import tqdm

with open('Diplom/token.txt') as file_object:
    token = file_object.read().strip()
# with open('Diplom/yatoken.txt') as f:
#     yatoken = f.read().strip()

user_id = str(input('Введите user_id: '))


yatoken = str(input('Введите ваш токен с полигона Яндекс: '))

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token1, version, user_id=None):
        self.token = token1
        self.version = version
        self.user_id = user_id
        self.params = {
            'access_token': self.token,
            'v': self.version,
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_photos_links(self, user_id: str):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'photos.get'
        followers_params = {
            'album_id': 'profile',
            'count': 5,
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
            photos_to_upload.append(photo_info)
        return url_names


class YaUploader:
    def __init__(self, yatoken: str):
        self.yatoken = yatoken

    def create_dir(self, user_id):
        """Создает папку на яндекс диске"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': user_id}
        headers = {'Authorization': self.yatoken}
        response = requests.put(url, params=params, headers=headers)
        # проверка выполнения создания папки
        if response.status_code == 201:
            print(f'Папка "{user_id}" создана на диске.')
        else:
            error_message = response.json()['message']
            print(f'Ошибка код - {response.status_code}: {error_message}')

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        for link, name in vk_client.get_photos_links(user_id):
            response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                     params={'path': f"{user_id}/{name}",
                                             'url': link},
                                     headers={'Authorization': f'OAuth {self.yatoken}'})
            for i in tqdm(vk_client.get_photos_links(user_id)):
                if response.status_code == 202:
                    time.sleep(1)
        return


vk_client = VkUser(token, '5.130')

uploader = YaUploader(yatoken)
uploader.create_dir(user_id)
uploader.upload(vk_client.get_photos_links(user_id))
