import colour
import datetime
import re
import DNS
import phonenumbers
from validate_email import validate_email
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

    def religion(self):
        religions = ['christianism', 'islam', 'judaism', 'budism', 'hinduism', 'none', 'other']
        religion_choice = str(input(colour.yellow + "> Religion (christianism, islam, judaism, budism, hinduism, none, "
                                                    "other): " + colour.end).replace(" ", ""))
        if religion_choice != "":
            while religion_choice not in religions:
                print(self.message("\r\n[-] You must enter one of the options above!\n", colour.red))
                religion_choice = str(input(colour.yellow + "> Religion (christianism, muslim, judaism, budism, "
                                                            "hinduism, none, other): " + colour.end).replace(" ", ""))
            if religion_choice != 'none' or religion_choice != 'other':
                self.profile["religion"] = religion_choice

    def birth(self):
        birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)
        if birthdate != "":
            while len(birthdate) == 0 or len(birthdate) != 8:
                print(self.message("\r\n[-] You must enter 8 digits for birthday!\n", colour.red))
                birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)

            self.profile["birth_day"] = str(birthdate[0:2])
            self.profile["birth_month"] = str(birthdate[2:4])
            self.profile["birth_year"] = str(birthdate[-4:])
            self.profile["age"] = str(self.now.year - int(birthdate[-4:]))

    def email(self):
        email_address = str(input(colour.yellow + "> Email address : " + colour.end).replace(" ", ""))

        if email_address != "":
            while not validate_email(email_address, verify=True):
                print(self.message("\r\n[-] Not valid! Email address does not exists!\n", colour.red))
                email_address = str(input(colour.yellow + "> Email address : " + colour.end).replace(" ", ""))

            self.profile["email_user"] = str(email_address.split('@')[0])

    def phone(self):
        phone = str(input(colour.yellow + "> Phone Number : " + colour.end))
        if phone != "":
            phone_parsed = phonenumbers.parse(phone, None)

            while not phonenumbers.is_valid_number(phone_parsed):
                print(self.message("\r\n[-] You must enter a correct phone number!\n", colour.red))
                phone = str(input(colour.yellow + "> Phone Number : " + colour.end))
                phone_parsed = phonenumbers.parse(phone, None)

            self.profile["phone_country"] = str(phone_parsed.country_code)
            self.profile["phone_number"] = str(phone_parsed.national_number)

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
        if orientation != "":
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

    def motorcycle(self):
        self.profile["motorcycle_model"] = str(input(colour.yellow + "> Motorcycle Model : " + colour.end).replace(" ", ""))
        self.profile["motorcycle_brand"] = str(input(colour.yellow + "> Motorcycle Brand : " + colour.end).replace(" ", ""))
        self.profile["motorcycle_plate"] = str(input(colour.yellow + "> Motorcycle License Plate : " + colour.end).replace(" ", ""))

    def work(self):
        self.profile["company"] = str(input(colour.yellow + "> Company : " + colour.end).replace(" ", ""))
        self.profile["employee_id"] = str(input(colour.yellow + "> Employee-ID : " + colour.end).replace(" ", ""))
        self.profile["position"] = str(input(colour.yellow + "> Position : " + colour.end).replace(" ", ""))

    def hobbies(self):
        self.profile["colour"] = str(input(colour.yellow + "> Colour : " + colour.end).replace(" ", ""))
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
        self.religion()
        self.birth()
        self.email()
        self.phone()
        self.education()
        self.address()
        self.politics()
        self.car()
        self.motorcycle()
        self.work()
        self.hobbies()

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
