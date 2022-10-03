def get_log(login, password, attemp=3, er_msg='Система заблокирована. Повторите попытку через 5 мин.'):
    lg = input(login)
    attemp -= 1
    while True:
        psw = input(password)
        if len(psw) < 8 and attemp > 0:
            print('Short password')
            attemp -= 1
            continue
        elif psw in lg and attemp > 0:
            print('Password contains login')
            attemp -= 1
            continue
        elif len(psw) >= 8 and psw not in lg:
            print('Password was set')
            return
        else:
            print(er_msg)
            return


get_log(login='Login: ', password='Password: ', attemp=2)

