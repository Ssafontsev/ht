import requests


def get_most_int(heroes):
    int_dict = {}
    for hero in heroes:
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
        list_with_heroes = response.json()['results']
        for elm in list_with_heroes:
            if elm['name'] == hero:
                int_dict[hero] = elm['powerstats']['intelligence']
    for key in int_dict:
        int_dict[key] = int(int_dict[key])
    max_val = max(int_dict.values())
    final_dict = {k: v for k, v in int_dict.items() if v == max_val}
    for key, value in final_dict.items():
        print("{} самый умный из супергероев со значением intelligence = {}".format(key, value))
    return


get_most_int(['Hulk', 'Captain America', 'Thanos'])
