# Passwordchecker
# waarbij de beperkingsregels uit een configuratiebestand ingelezen worden.
#
# Passwordgenerator
# met configurabele complexiteit
# Importing things

import configparser
import random
import string

gereratedpassword = ""
choosablecharactetrs = string.ascii_lowercase

# assign characters to string
special_characters = string.punctuation
alfabet_characters = string.ascii_lowercase
Capitalize_characters = string.ascii_uppercase
number_characters = string.digits

all_characters = string.punctuation + string.digits + string.ascii_letters

# Read config file
config = configparser.ConfigParser()

config.read('C:/pasconfig.ini')
config.read('Oefen-challanges\passconfig.ini')
config.read('passconfig.ini')

config.sections()


# Function selector
def programstart():
    genorcheck = input("Choose 1 for Checker, choose 2 for generator: ")
    if genorcheck == "1":
        passwordchecker()

    elif genorcheck == "2":
        passwordgenerator()

    else:
        print("input incorrect")
        programstart()


# Password checker
def passwordchecker():
    print("generator")

    # print the password requirements
    print("minimale lengte: " + config['default']['passwordlenght'])
    if config['default'].getboolean('Symbols'):
        print("symbols are obligatory")
    if config['default'].getboolean('Numbers'):
        print("Numbers are obligatory")
    if config['default'].getboolean('Letters'):
        print("Letters are obligatory")
    if config['default'].getboolean('Capitalize'):
        print("Capitalized letters are obligatory")

    # userinput password
    givenpassword = input("please give password: ")

    print("-------------------------------")

    # check password if it meets the requirements
    passwordgood = True

    if len(givenpassword) < config['default'].getint('passwordlenght'):
        print("password not long enough")
        passwordgood = False

    if config['default'].getboolean('Symbols') != any(c in special_characters for c in givenpassword):
        print("Password does not contain any special characters")
        passwordgood = False

    if config['default'].getboolean('Numbers') != any(c in number_characters for c in givenpassword):
        print("Password does not contain any numbers")
        passwordgood = False

    if config['default'].getboolean('Letters') != any(c in alfabet_characters for c in givenpassword):
        print("Password does not contain any lowercase characters")
        passwordgood = False

    if config['default'].getboolean('Capitalize') != any(c in Capitalize_characters for c in givenpassword):
        print("Password does not contain any uppercase characters")
        passwordgood = False

    # print if the password passed the check
    if not passwordgood:
        print("password not good enough, please try again")
        pass

    else:
        print("password Passed check")
        pass

    print("----------------------------------")


# Password Generator
def passwordgenerator():
    global gereratedpassword
    global choosablecharactetrs

    # get options from config file
    if config['default'].getboolean('Symbols'):
        choosablecharactetrs = choosablecharactetrs + string.punctuation
    if config['default'].getboolean('Numbers'):
        choosablecharactetrs = choosablecharactetrs + string.digits
    if config['default'].getboolean('Capitalize'):
        choosablecharactetrs = choosablecharactetrs + string.ascii_uppercase

    # generate password in the required length
    for x in range(config['default'].getint('passwordlenght')):
        gereratedpassword += random.choice(choosablecharactetrs)

    # print the generated password
    print(gereratedpassword)


# Running code
programstart()
