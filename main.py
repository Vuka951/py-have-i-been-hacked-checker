from check_email import check_email, headers
from check_password import check_password


print('******************************************************')
print('Have my passwords or emails been hacked?!!?!? Checker')
print('******************************************************')

while True:
    what_to_check = str(input('Email or Password? '))
    if what_to_check.lower() == 'password':
        password = input('Password to check: ')
        check_password(password)
    elif what_to_check.lower() == 'email':
        if headers['hibp-api-key'] and headers['User-Agent']:
            email = input('Email to check: ')
            check_email(email)
        else:
            print('You need to provide an hibp-api-key and User-Agent first')
    else:
        print('EMAIL OR PASSWORD MF!')
