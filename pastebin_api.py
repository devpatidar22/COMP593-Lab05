import requests

DEVELOPER_KEY = 'VMEQDEfMXfoTApAHoohSHhE-Bk7pWGsf'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("this is a title", 'thi\ns is \na body', '1H', True)
    print(f'New Paste URL: {url}')

def post_new_paste(title, body_text , expiration = '10M', listed = False):
    """ Post a new public post to a PasteBin

    Args:
        title (str): Paste Title
        body_text (str): Body Text
        expiration (str, optional): expiration date of your paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Weather paste is publicly available (True) or not (False). Defaults to False.

    Returns:
        _type_: URL of the new paste, if successful, None if unsuccessful.
    """
    paste_params = {
        'api_dev_key' : DEVELOPER_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private' : 0 if listed else 1
    }
    
    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(url=PASTEBIN_API_URL,data=paste_params)
   
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    
    else:
        print("Failed")
        print(f'Status code: {resp_msg.status_code} {resp_msg.reason}')
        print(f"Reason: {resp_msg.text}")
    return


if __name__ == "__main__":
    main()