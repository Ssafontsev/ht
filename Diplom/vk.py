import requests
import time
import json
from tqdm import tqdm


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version,
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_photos_links(self, user_id: str, qty_photos: str):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'photos.get'
        followers_params = {
            'album_id': 'profile',
            'count': qty_photos,
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
        with open('Diplom/about_photos.json', 'w') as json_file:
            json.dump(photos_to_upload, json_file)
        return url_names


class YaUploader:
    def __init__(self, token: str, user_id: str):
        self.token = token
        self.user_id = user_id

    def create_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.user_id}
        headers = {'Authorization': self.token}
        response = requests.put(url, params=params, headers=headers)
        if response.status_code == 201:
            print(f'Папка "{self.user_id}" создана на диске.')
        else:
            error_message = response.json()['message']
            print(f'Ошибка код - {response.status_code}: {error_message}')

    def upload(self, lst_link_name):
        for link, name in tqdm(lst_link_name):
            response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                     params={'path': f"{self.user_id}/{name}",
                                             'url': link},
                                     headers={'Authorization': f'OAuth {self.token}'})
            if response.status_code == 202:
                time.sleep(0.1)
        return


if __name__ == '__main__':
    user_id_input = str(input('Введите user_id: '))
    qty_photos_input = str(input('Введите количество фото для загрузки: '))
    yatoken = str(input('Введите ваш токен с полигона Яндекс: '))
    tokenvk = str(input('Введите ваш токен VK: '))
    vk_client = VkUser(tokenvk, '5.130')
    listoflinks = vk_client.get_photos_links(user_id_input, qty_photos_input)
    uploader = YaUploader(yatoken, user_id_input)
    uploader.create_dir()
    uploader.upload(listoflinks)
