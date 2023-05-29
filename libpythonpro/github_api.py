import requests


def buscar_avatar(usuario):
    '''
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário no GitHub
    :return: str com link do avatar
    '''

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    data = resp.json()

    if 'avatar_url' in data:
        return data['avatar_url']
    else:
        return 'Avatar não encontrado'


if __name__ == '__main__':
    print(buscar_avatar('lucascomaru'))

