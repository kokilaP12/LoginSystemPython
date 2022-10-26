import re
def welcome():
    print("Welcome to your User dashboard")

def gainAccess(Username=None, Password=None):
    Username = input("Login with your username:")
    Password = input("Login with your Password:")

    if not len(Username or Password) < 1:
        if True:
            file2 = open("credentials.txt")
            content = file2.readlines()
            loginusername= content[0]
            loginpassword=content[1]

            print(loginusername)
            print(Username)
            print(loginpassword)
            print(Password)
        try:
            if (Username == loginusername):


                try:
                    if (Password == loginpassword):

                        print("Login success!")
                        print("Hi", Username)
                        welcome()
                    else:
                        print("Wrong password")

                except:
                    print("Incorrect passwords or username")
            else:
                print("Username doesn't exist")
                register()
        except:
            print("Password or username doesn't exist")
        else:
            print("Error logging into the system")

    else:
        print("Please attempt login again")
        gainAccess()



def register(username=None,password=None):
    username = input('please enter username : ')
    password = input('please enter password : ')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not(re.fullmatch(regex, username)):

     print("Invalid username")
    l, u, p, d = 0, 0, 0, 0

    if (len(password) > 5 and len(password) <=16):
     for i in password:

        # counting lowercase alphabets
        if (i.islower()):
            l+=1

            # counting uppercase alphabets
        if (i.isupper()):
            u+=1

            # counting digits
        if (i.isdigit()):
            d+=1

            # counting the mentioned special characters
        if(i=='@'or i=='$' or i=='_'):
            p+=1
    if not(l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):

     print("Invalid Password")

    file1 = open('credentials.txt', 'w')
    file1.write(username)
    file1.write("\n")
    file1.write(password)
    file1.close()

    print("Successfully created user")


def home(option=None):
    print("Welcome, please select an option")
option = input("Login | Signup:")
if option == "Login":
    gainAccess()
elif option == "Signup":
    register()
else:
    print("Please Login/Signup")

home()
