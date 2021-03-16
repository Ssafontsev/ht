def get_photos(self, quantity_photo_to_upload=None, album_id=None):
    """
    Получает необходимую информацию о фото, для скачивания на яндекс диск
    :param quantity_photo_to_upload: количество скачиваемых фото
    :param album_id: из какого альбома качать
    :return: список с url и именами фотографий максимального размера
    """
    # если не ввести количество фото для скачивания, скачается 5 штук
    if quantity_photo_to_upload is None:
        quantity_photo_to_upload = 5
    # если не ввести id альбома, то скачаются фото альбома 'profile'
    if album_id is None:
        album_id = 'profile'
    photos_url = self.url + 'photos.get'
    photos_params = {
        'user_id': self.owner_id,
        'album_id': album_id,
        'rev': 1,
        'extended': 1,
        'count': quantity_photo_to_upload,
    }
    response = requests.get(photos_url, params={**self.params, **photos_params})
    if response.status_code == 200:
        photos_list = response.json()['response']['items']
        # список с информацией для записи в json
        photos_to_upload = []
        # список с url и именами фотографий максимального размера, для последующего скачивания на яндекс диск
        url_and_names_to_upload = []
        for photo in photos_list:
            about_photo = {}
            quantity_likes = photo['likes']['count']
            photo_date = photo['date']
            max_size_photo = photo['sizes'][-1]
            photo_name = f'{quantity_likes}.jpg'
            for item in photos_to_upload:
                # если количество лайков одинаково, то добавить дату загрузки
                if item['file_name'] == photo_name:
                    photo_name = f'{quantity_likes}_{photo_date}.jpg'
            url_and_names_to_upload.append([max_size_photo['url'], photo_name])
            about_photo['file_name'] = photo_name
            about_photo['size'] = max_size_photo['type']
            photos_to_upload.append(about_photo)
        # записывает полученую информацию в json
        with open('../json_file/about_photos.json', 'w') as json_file:
            json.dump(photos_to_upload, json_file)
        return url_and_names_to_upload
    else:
        status_code = f'Код ответа - {response.status_code}\n'
        error_message = response.json()['message']
        return f'Упс... Что-то пошло не так!\n{status_code} {error_message}\n'