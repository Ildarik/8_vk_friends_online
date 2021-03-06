import getpass
import vk

APP_ID = 6101946

def get_user_login():
    typed_login = input('Please type login: ')
    return typed_login

def get_user_password():
    typed_password = getpass.getpass(prompt='Please type password: ')
    return typed_password

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_id_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_id_online)
    return friends_online

def output_friends_to_console(friends_online):
    print('My friends online: ')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
