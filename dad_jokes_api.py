import requests

DAD_JOKES_API_URL = "https://icanhazdadjoke.com/"
DAD_JOKES_SEARCH_API = f'{DAD_JOKES_API_URL}search'

def main():
    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list)
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that contains a search term

    Args:
        search_term (str): Search Term

    Returns:
        list: List of jokes that contains search term.
    """
    
     
    header_params = {'Accept' : 'application/json'}
    query_str_params = {'term' : search_term}
    
    print(f"Searching Dad jokes Api for '{search_term}' jokes...", end='')
    resp_msg = requests.get(DAD_JOKES_SEARCH_API, headers=header_params, params=query_str_params)
   
    if resp_msg.ok:
        print('Success!')
        body_dict = resp_msg.json()
        jokes_list = [j['joke'] for j in body_dict['results']] 
        return jokes_list
    
    else:
        print("Failed")
        print(f'Status code: {resp_msg.status_code} {resp_msg.reason}')

    
    
    return
    
    
def get_random_dad_joke():
    """Get a random dad joke

    Returns:
        str: Dad joke
    """
    
    head_params = {'Accept' : 'application/json'}
    
    
    print("Sending GET Request to Dad jokes Api ...", end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=head_params)
   
    if resp_msg.ok:
        print('Success!')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    
    else:
        print("Failed")
        print(f'Status code: {resp_msg.status_code} {resp_msg.reason}')

    
if __name__ == '__main__':
    main()