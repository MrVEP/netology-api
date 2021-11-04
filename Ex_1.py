import requests


class Superhero:

    def __init__(self, token, name):
        url = 'https://superheroapi.com/api' + f'/{token}'
        self.name = name
        url_id = url + f'/search' + f'/{self.name}'
        resp1 = requests.get(url_id, timeout=5).json()
        for i in range(len(resp1['results'])):
            if resp1['results'][i]['name'] == self.name:
                self.id = resp1['results'][i]['id']
        url_stats = url + f'/{self.id}' + f'/powerstats'
        resp2 = requests.get(url_stats, timeout=5).json()
        del resp2['response']
        del resp2['id']
        del resp2['name']
        self.stats = resp2


def best_hero(heroes, stat):
    comparison = {}
    for i in heroes:
        if not isinstance(i, Superhero):
            return f'Ошибка - {i.name} не супергерой!'
        comparison[i.name] = int(i.stats[stat])
    comparison_sorted = dict(sorted(comparison.items(), key=lambda x: x[1], reverse=True))
    return list(comparison_sorted.keys())[0]


def main():
    hulk = Superhero(2619421814940190, 'Hulk')
    captain_america = Superhero(2619421814940190, 'Captain America')
    thanos = Superhero(2619421814940190, 'Thanos')
    print(best_hero([hulk, captain_america, thanos], 'intelligence'))


if __name__ == '__main__':
    main()
