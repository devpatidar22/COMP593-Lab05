import requests

def main():
    info = get_information_of_pokemon("1")
    print(info)
    return

def get_information_of_pokemon(name):
    """ Collectes the data of specified name pokemon from PokeAPI

    Args:
        name (str or int): Name of the pokemon whose information is required

    Returns:
        dict: Returns a dictonary containing the information of pokemon if fetched successfully. Returns None if unsuccessfull.
    """
    name = str(name).lower().strip()
    link = f"https://pokeapi.co/api/v2/pokemon/{name}"
    info = requests.get(link)
    print(f"Getting information for {name}...", end='')
    
    if info.ok:
        print('success')
        return info.json()
    else:
        print('failure')
        print("Response code: 404 (Not Found)")
        return None


if __name__ == '__main__':
    main()