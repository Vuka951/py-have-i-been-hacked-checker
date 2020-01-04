import requests

# to use the email check you need to provid the User-Agent (AppName or a short description of your app) and an "hibp-api-key" that you need to buy
headers = {
    'User-Agent': None,
    'hibp-api-key': None
}


def check_email(email):
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'

    res = requests.request('GET', url, headers=headers)
    if res.status_code != 200:
        raise RuntimeError(
            f'Fetching Error: {res.status_code}')
    # since the account breach endpoint returns an array of breach names we can get the count much easier
    count = len(res.json())
    if count:
        print(
            f'{email} was found {count} times')
    else:
        print(f'{email} was not found, ur all good!')
