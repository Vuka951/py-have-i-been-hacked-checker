import requests
import hashlib


def password_request_api_data(url_param):
    url = f'https://api.pwnedpasswords.com/range/{url_param}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Fetching Error: {res.status_code}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_password_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, rest = sha1password[:5], sha1password[5:]
    response = password_request_api_data(first5_char)
    return get_password_leaks_count(response, rest)


def check_password(password):
    count = pwned_password_api_check(password)
    if count:
        print(
            f'{password} was found {count} times')
    else:
        print(f'{password} was not found, ur all good!')
