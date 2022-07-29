import urllib.request

from api_key import API_KEY
import pyrebase

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

firebase = pyrebase.initialize_app(API_KEY)

# auth = firebase.auth()
# storage = firebase.storage()
database = firebase.database()


# Auth Email
# choice = int(input("Press 1 to Sign In, Press 2 to Register: "))
#
# if choice == 1:
#     email = input("Enter Your Email: ")
#     password = input("Enter Your Password: ")
#
#     try:
#         auth.sign_in_with_email_and_password(email, password)
#         print("Sign In Successfully")
#     except:
#         print("Please Enter Valid Email and Password")
#
# if choice == 2:
#     email = input("Enter Your Email: ")
#     password = input("Enter Your Password: ")
#     confirm_password = input("Please Confirm your above Password: ")
#
#     if password == confirm_password:
#         try:
#             auth.create_user_with_email_and_password(email, password)
#             print("User Created SuccessFully")
#         except:
#             print("Email Already exists")
#     else:
#         print("Password != Confirm_Password")

# Login
# def upload():
#     username = input("Please Enter your name")
#     filename = input("Please Enter the File You can to Upload")
#     cloud_file_name = f"{username}/{filename}"
#     storage.child(cloud_file_name).put(filename)
#
# def view():
#     username = input("Please Enter your name")
#     filename = input("Please Enter the File You can to Upload")
#     cloud_file_name = f"{username}/{filename}"
#     print(storage.child(cloud_file_name).get_url(None))
#
# def download():
#     username = input("Please Enter your name")
#     filename = input("Please Enter the File You can to Upload")
#     cloud_file_name = f"{username}/{filename}"
#     storage.child(cloud_file_name).download("",filename=filename)
#
# def read_file():
#     username = input("Please Enter your name")
#     filename = input("Please Enter the File You can to Upload")
#     cloud_file_name = f"{username}/{filename}"
#     url = storage.child(cloud_file_name).get_url(None)
#     f = urllib.request.urlopen(url).read()
#     print(url)
#
#
# read_file()

data = {
    'age': 20,
    'address': "Banaras",
    'friend': True,
    'name': "Anjuman Hassan"
}

database.push(data)