import json
from datetime import datetime
from uuid import uuid4


# print(datetime.now())
def user_list(file_path):
    try:
        with open(file_path) as f:
            users = json.load(f)
            return users
    except FileNotFoundError as e:
        print(e)


def create_user(file_path):
    username = input('Enter your username: ').title()
    email = input("Enter your email : ")
    age = int(input("Enter your age : "))
    created_at = str(datetime.now())
    user_id = str(uuid4())
    user = {"user_id": user_id,
            "username": username,
            "email": email, "age": age,
            "created_at": created_at,
            "is_active": True}
    users_list = user_list(file_path)
    with open(file_path, 'w') as file:
        users_list.append(user)
        json.dump(users_list, file, indent=3)
        print(f'{username} user successfully added')


def read_user(file_path):
    user_id = input("Enter your user_id : ")
    users = user_list(file_path)
    for user in users:
        if user["user_id"] == user_id:
            return user
    else:
        print(f'{user_id} Not found')


def update_user(file_path, user_id):
    users = user_list(file_path)
    update_username = input("Enter your update username : ").title()
    update_age = int(input("Enter your update age : "))
    for user in users:
        if user["user_id"] == user_id:
            user["username"] = update_username
            user["age"] = update_age
            print('User successfully updated')
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=3)
            break

    else:
        print(f'{user_id} is not found')


# update_user('users.json', '22e98e9b-440f-4f9a-9ddd-dd8de76e5799')
def user_delete(file_path, user_id):
    users = user_list(file_path)
    index = -1
    for user in users:
        index += 1
        if user["user_id"] == user_id:
            del users[index]
            print('User successfully deleted')
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)
            break
    else:
        print(f'{user_id} not found')


user_delete('users.json', '123')


# def menu():
#     print('Create =>1')
#     print('Update -> 2')
#     print('exit => q')
#     return input('?:')
#
#
# def run():
#     while True:
#         choice = menu()
#         if choice == '1':
#             create_user(file_path='users.json')
#         elif choice == '2':
#             update_user()
#
#         elif choice == 'q':
#             break