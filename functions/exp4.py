def create_account(login, password):
    if get_account(login):
        return False
    with open('accounts.txt', 'a') as file:
        acc = login + ' ' + password + ';'
        file.write(acc)
    acc_file = login + '.txt'
    with open(acc_file, 'w') as ac:
        ac.write('')
    return True

def all_accounts():
    accounts = {}
    with open('accounts.txt', 'r') as file:
        data = file.read().removesuffix(';')
        a = data.split(';')
    for i in a:
        i1 = i.split(' ')[0]
        i2 = i.split(' ')[1]
        accounts.update({i1:i2})
    return accounts

def get_account(login):
    if all_accounts().get(login):
        return True
    else:
        return False

def enter_account(login, password):
    if get_account(login) == False:
        print('Incorrect Login')
        return False
    elif get_account(login) and password != all_accounts().get(login):
        print('Incorrect Password')
        return False
    else:
        print('Welcome to Account')
        return True

def account_redactor(login, password, a='read', w=''):
    if enter_account(login, password):
        file_name = login + '.txt'
        if a == 'read':
            with open(file_name, 'r') as file:
                print(file.read())
        elif a == 'write':
            with open(file_name, 'a') as file:
                file.write(w)

create_account('asena', '123456')
account_redactor('asena', '123456', a='read')
print()