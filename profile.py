import colour
import datetime
import re
from colour import *
import calendar

colour = Colour()


class Profile:

    def __init__(self):
        self.profile = {}
        self.now = datetime.datetime.now()

    def message(self, text, colour_choice):
        return colour_choice + str(text) + colour.end

    def identification(self):
        self.profile["first_name"] = str(input(colour.yellow + "> First Name : " + colour.end).replace(" ", ""))
        self.profile["last_name"] = str(input(colour.yellow + "> Last Name : " + colour.end).replace(" ", ""))
        self.profile["nickname"] = str(input(colour.yellow + "> Nickname : " + colour.end).replace(" ", ""))
        self.profile["Id_number"] = str(input(colour.yellow + "> ID-Number : " + colour.end).replace(" ", ""))

        religions = ['christian', 'muslim', 'jew', 'budism', 'hinduism', 'none', 'other']
        religion_choice = str(input(colour.yellow + "> Religion (christian, muslim, jew, budism, hinduism, none, "
                                                    "other): " + colour.end).replace(" ", ""))
        while religion_choice not in religions:
            print(self.message("\r\n[-] You must enter one of the options above!\n", colour.red))
            religion_choice = str(input(colour.yellow + "> Religion (christian, muslim, jew, budism, hinduism, none, "
                                                        "other): " + colour.end).replace(" ", ""))
        if religion_choice != 'none' or religion_choice != 'other':
            self.profile["religion"] = religion_choice

        birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)
        while len(birthdate) == 0 or len(birthdate) != 8:
            print(self.message("\r\n[-] You must enter 8 digits for birthday!\n", colour.red))
            birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)

        self.profile["birth_day"] = str(birthdate[0:2])
        self.profile["birth_month"] = str(birthdate[2:4])
        self.profile["birth_year"] = str(birthdate[-4:])
        self.profile["age"] = str(self.now.year - int(birthdate[-4:]))

    def email(self):
        email_address = str(input(colour.yellow + "> Email address : " + colour.end).replace(" ", ""))
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        while not re.match(email_regex, email_address):
            print(self.message("\r\n[-] You must enter a correct email address ( xxxx@yyyy.zzz!\n", colour.red))
            email_address = str(input(colour.yellow + "> Email address : " + colour.end).replace(" ", ""))

        self.profile["email_user"] = str(email_address.split('@')[0])

    def phone(self):
        phone = str(input(colour.yellow + "> Phone Number (+XXX.. NNNNNNNNN..) : " + colour.end))
        self.profile["phone_country"] = str(phone.split(' ')[0])
        self.profile["phone_number"] = str(phone.split(' ')[1])

    def education(self):
        self.profile["prim_school"] = str(
            input(colour.yellow + "> Primary school : " + colour.end).replace(" ", ""))
        self.profile["sec_school"] = str(
            input(colour.yellow + "> Secondary school : " + colour.end).replace(" ", ""))
        self.profile["university"] = str(input(colour.yellow + "> University : " + colour.end).replace(" ", ""))

    def address(self):
        self.profile["street"] = str(input(colour.yellow + "> Street address: " + colour.end).replace(" ", ""))
        self.profile["street_number"] = str(
            input(colour.yellow + "> Street Number address: " + colour.end).replace(" ", ""))
        self.profile["floor"] = str(input(colour.yellow + "> Floor adress : " + colour.end).replace(" ", ""))
        self.profile["door"] = str(input(colour.yellow + "> Door adress : " + colour.end).replace(" ", ""))
        self.profile["post_code"] = str(input(colour.yellow + "> Post Code : " + colour.end).replace(" ", ""))

    def politics(self):
        politics = ['liberal', 'conservative', "socialist ", "comunist", "anarchist", "christian-democrat",
                    "socialdemocrat", "other", "none"]
        orientation = str(input(colour.yellow + "> Political orientation (liberal, conservative, "
                                                "socialist,"
                                                "comunist, anarchist, christian-democrat, socialdemocrat,"
                                                "other, none ): "
                                + colour.end).replace(" ", ""))
        while orientation not in politics:
            print(self.message("\r\n[-] You must enter one of the above options!\n", colour.red))
            orientation = str(input(colour.yellow + "> Political orientation (liberal, conservative, "
                                                    "socialist,"
                                                    "comunist, anarchist, christian-democrat, socialdemocrat,"
                                                    "other, none ): "
                                    + colour.end).replace(" ", ""))
        if orientation != 'none' or orientation != 'other':
            self.profile["politics"] = orientation

    def car(self):
        self.profile["car_model"] = str(input(colour.yellow + "> Car Model : " + colour.end).replace(" ", ""))
        self.profile["car_brand"] = str(input(colour.yellow + "> Car Brand : " + colour.end).replace(" ", ""))
        self.profile["license_plate"] = str(input(colour.yellow + "> License Plate : " + colour.end).replace(" ", ""))

    def other(self):
        self.profile["company"] = str(input(colour.yellow + "> Company : " + colour.end).replace(" ", ""))
        self.profile["pet"] = str(input(colour.yellow + "> Pet Name : " + colour.end).replace(" ", ""))
        self.profile["music"] = str(input(colour.yellow + "> Music Group : " + colour.end).replace(" ", ""))
        self.profile["artist"] = str(input(colour.yellow + "> Music Artist : " + colour.end).replace(" ", ""))
        self.profile["film"] = str(input(colour.yellow + "> Film  : " + colour.end).replace(" ", ""))
        self.profile["tv_show"] = str(input(colour.yellow + "> TV Show  : " + colour.end).replace(" ", ""))
        self.profile["sport"] = str(input(colour.yellow + "> Sport : " + colour.end).replace(" ", ""))
        self.profile["team"] = str(input(colour.yellow + "> Sport Team: " + colour.end).replace(" ", ""))
        self.profile["city"] = str(input(colour.yellow + "> City : " + colour.end).replace(" ", ""))
        self.profile["food"] = str(input(colour.yellow + "> Food : " + colour.end).replace(" ", ""))
        self.profile["celebrity"] = str(input(colour.yellow + "> Celebrity : " + colour.end).replace(" ", ""))

    def create(self, relative):
        print(self.message("\n[+] Insert the information about the " + relative + " to make a dictionary\n"
                                                                                  "[+] If you don't know all the "
                                                                                  "info, just hit enter when asked!\n",
                           colour.green))

        self.identification()
        self.email()
        self.phone()
        self.education()
        self.address()
        self.politics()
        self.car()
        self.other()

    def process(self):
        info = [self.profile["birth_day"],
                self.profile["birth_month"],
                calendar.month_name[int(self.profile["birth_month"])].lower(),
                calendar.month_name[int(self.profile["birth_month"])].capitalize(),
                calendar.month_name[int(self.profile["birth_month"])].upper(),
                calendar.month_abbr[int(self.profile["birth_month"])].lower(),
                calendar.month_abbr[int(self.profile["birth_month"])].capitalize(),
                calendar.month_abbr[int(self.profile["birth_month"])].upper(),
                self.profile["birth_year"],
                self.profile["birth_year"][-2:],
                self.profile["age"],
                self.profile["phone_country"],
                self.profile["phone_number"],
                self.profile["floor"],
                self.profile["street_number"],
                self.profile["door"]]

        del self.profile["birth_day"]
        del self.profile["birth_month"]
        del self.profile["birth_year"]
        del self.profile["age"]
        del self.profile["phone_country"]
        del self.profile["phone_number"]
        del self.profile["floor"]
        del self.profile["street_number"]
        del self.profile["door"]

        for value in self.profile.values():
            if value != "":
                info.append(value.upper())
                info.append(value.lower())
                info.append(value.capitalize())

        return info
