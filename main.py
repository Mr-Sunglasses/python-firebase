from api_key import API_KEY
import pyrebase

firebase = pyrebase.initialize_app(API_KEY)

auth = firebase.auth()
# firebase.storage()
# firebase.database()


# Auth Email
choice = int(input("Press 1 to Sign In, Press 2 to Register: "))

if choice == 1:
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")

    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Sign In Successfully")
    except:
        print("Please Enter Valid Email and Password")

if choice == 2:
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    confirm_password = input("Please Confirm your above Password: ")

    if password == confirm_password:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("User Created SuccessFully")
        except:
            print("Email Already exists")
    else:
        print("Password != Confirm_Password")
