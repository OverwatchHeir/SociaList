from utils.colour import *
from utils.cli import Cli
import datetime
import phonenumbers
from validate_email import validate_email
import calendar


class Profile:

    def __init__(self):
        self.profile = {}
        self.now = datetime.datetime.now()
        self.cli = Cli()

    def identification(self):
        self.profile["first_name"] = str(
            input(self.cli.colour.yellow + "> First Name : " + self.cli.colour.end).replace(" ", ""))
        self.profile["last_name"] = str(
            input(self.cli.colour.yellow + "> Last Name : " + self.cli.colour.end).replace(" ", ""))
        self.profile["nickname"] = str(
            input(self.cli.colour.yellow + "> Nickname : " + self.cli.colour.end).replace(" ", ""))
        self.profile["Id_number"] = str(
            input(self.cli.colour.yellow + "> ID-Number : " + self.cli.colour.end).replace(" ", ""))

    def religion(self):
        religions = ['christianism', 'islam', 'judaism', 'budism', 'hinduism', 'none', 'other']
        religion_choice = str(
            input(self.cli.colour.yellow + "> Religion (christianism, islam, judaism, budism, hinduism, "
                                           "none, other): " + self.cli.colour.end).replace(" ", ""))
        if religion_choice != "":
            while religion_choice not in religions:
                print(self.cli.message("\r\n[-] You must enter one of the options above!\n", self.cli.colour.red))
                religion_choice = str(
                    input(self.cli.colour.yellow + "> Religion (christianism, muslim, judaism, budism, "
                                                   "hinduism, none, other): " + self.cli.colour.end).replace(" ", ""))
            if religion_choice != 'none' or religion_choice != 'other':
                self.profile["religion"] = religion_choice

    def birth(self):
        birthdate = input(self.cli.colour.yellow + "> Birthdate (DDMMYYYY): " + self.cli.colour.end)

        while len(birthdate) == 0 or len(birthdate) != 8:
            print(self.cli.message("\r\n[-] You must enter 8 digits for birthday!\n", self.cli.colour.red))
            birthdate = input(self.cli.colour.yellow + "> Birthdate (DDMMYYYY): " + self.cli.colour.end)

        self.profile["birth_day"] = str(birthdate[0:2])
        self.profile["birth_month"] = str(birthdate[2:4])
        self.profile["birth_year"] = str(birthdate[-4:])
        self.profile["age"] = str(self.now.year - int(birthdate[-4:]))

    def email(self):
        email_address = str(input(self.cli.colour.yellow + "> Email address : " + self.cli.colour.end).replace(" ", ""))

        if email_address != "":
            while not validate_email(email_address, verify=True):
                print(self.cli.message("\r\n[-] Not valid! Email address does not exists!\n", self.cli.colour.red))
                email_address = str(
                    input(self.cli.colour.yellow + "> Email address : " + self.cli.colour.end).replace(" ", ""))

            self.profile["email_user"] = str(email_address.split('@')[0])

    def phone(self):
        phone = str(input(self.cli.colour.yellow + "> Phone Number : " + self.cli.colour.end))
        if phone != "":
            phone_parsed = phonenumbers.parse(phone, None)

            while not phonenumbers.is_valid_number(phone_parsed):
                print(self.cli.message("\r\n[-] You must enter a correct phone number!\n", self.cli.colour.red))
                phone = str(input(self.cli.colour.yellow + "> Phone Number : " + self.cli.colour.end))
                phone_parsed = phonenumbers.parse(phone, None)

            self.profile["phone_country"] = str(phone_parsed.country_code)
            self.profile["phone_number"] = str(phone_parsed.national_number)

    def education(self):
        self.profile["prim_school"] = str(
            input(self.cli.colour.yellow + "> Primary school : " + self.cli.colour.end).replace(" ", ""))
        self.profile["sec_school"] = str(
            input(self.cli.colour.yellow + "> Secondary school : " + self.cli.colour.end).replace(" ", ""))
        self.profile["university"] = str(
            input(self.cli.colour.yellow + "> University : " + self.cli.colour.end).replace(" ", ""))

    def address(self):
        self.profile["street"] = str(
            input(self.cli.colour.yellow + "> Street address: " + self.cli.colour.end).replace(" ", ""))
        self.profile["street_number"] = str(
            input(self.cli.colour.yellow + "> Street Number address: " + self.cli.colour.end).replace(" ", ""))
        self.profile["floor"] = str(
            input(self.cli.colour.yellow + "> Floor adress : " + self.cli.colour.end).replace(" ", ""))
        self.profile["door"] = str(
            input(self.cli.colour.yellow + "> Door adress : " + self.cli.colour.end).replace(" ", ""))
        self.profile["post_code"] = str(
            input(self.cli.colour.yellow + "> Post Code : " + self.cli.colour.end).replace(" ", ""))

    def politics(self):
        politics = ['liberal', 'conservative', "socialist ", "comunist", "anarchist", "christian-democrat",
                    "socialdemocrat", "other", "none"]
        orientation = str(input(self.cli.colour.yellow + "> Political orientation (liberal, conservative, "
                                                         "socialist,"
                                                         "comunist, anarchist, christian-democrat, socialdemocrat,"
                                                         "other, none ): "
                                + self.cli.colour.end).replace(" ", ""))
        if orientation != "":
            while orientation not in politics:
                print(self.cli.message("\r\n[-] You must enter one of the above options!\n", self.cli.colour.red))
                orientation = str(input(self.cli.colour.yellow + "> Political orientation (liberal, conservative, "
                                                                 "socialist,"
                                                                 "comunist, anarchist, christian-democrat, socialdemocrat,"
                                                                 "other, none ): "
                                        + self.cli.colour.end).replace(" ", ""))
            if orientation != 'none' or orientation != 'other':
                self.profile["politics"] = orientation

    def car(self):
        self.profile["car_model"] = str(
            input(self.cli.colour.yellow + "> Car Model : " + self.cli.colour.end).replace(" ", ""))
        self.profile["car_brand"] = str(
            input(self.cli.colour.yellow + "> Car Brand : " + self.cli.colour.end).replace(" ", ""))
        self.profile["license_plate"] = str(
            input(self.cli.colour.yellow + "> License Plate : " + self.cli.colour.end).replace(" ", ""))

    def motorcycle(self):
        self.profile["motorcycle_model"] = str(
            input(self.cli.colour.yellow + "> Motorcycle Model : " + self.cli.colour.end).replace(" ", ""))
        self.profile["motorcycle_brand"] = str(
            input(self.cli.colour.yellow + "> Motorcycle Brand : " + self.cli.colour.end).replace(" ", ""))
        self.profile["motorcycle_plate"] = str(
            input(self.cli.colour.yellow + "> Motorcycle License Plate : " + self.cli.colour.end).replace(" ", ""))

    def work(self):
        self.profile["company"] = str(
            input(self.cli.colour.yellow + "> Company : " + self.cli.colour.end).replace(" ", ""))
        self.profile["employee_id"] = str(
            input(self.cli.colour.yellow + "> Employee-ID : " + self.cli.colour.end).replace(" ", ""))
        self.profile["position"] = str(
            input(self.cli.colour.yellow + "> Position : " + self.cli.colour.end).replace(" ", ""))

    def hobbies(self):
        self.profile["colour"] = str(
            input(self.cli.colour.yellow + "> Colour : " + self.cli.colour.end).replace(" ", ""))
        self.profile["pet"] = str(
            input(self.cli.colour.yellow + "> Pet Name : " + self.cli.colour.end).replace(" ", ""))
        self.profile["music"] = str(
            input(self.cli.colour.yellow + "> Music Group : " + self.cli.colour.end).replace(" ", ""))
        self.profile["artist"] = str(
            input(self.cli.colour.yellow + "> Music Artist : " + self.cli.colour.end).replace(" ", ""))
        self.profile["film"] = str(input(self.cli.colour.yellow + "> Film  : " + self.cli.colour.end).replace(" ", ""))
        self.profile["tv_show"] = str(
            input(self.cli.colour.yellow + "> TV Show  : " + self.cli.colour.end).replace(" ", ""))
        self.profile["sport"] = str(input(self.cli.colour.yellow + "> Sport : " + self.cli.colour.end).replace(" ", ""))
        self.profile["team"] = str(
            input(self.cli.colour.yellow + "> Sport Team: " + self.cli.colour.end).replace(" ", ""))
        self.profile["city"] = str(input(self.cli.colour.yellow + "> City : " + self.cli.colour.end).replace(" ", ""))
        self.profile["food"] = str(input(self.cli.colour.yellow + "> Food : " + self.cli.colour.end).replace(" ", ""))
        self.profile["celebrity"] = str(
            input(self.cli.colour.yellow + "> Celebrity : " + self.cli.colour.end).replace(" ", ""))

    def create(self, relative):
        print(self.cli.message("\n[+] Insert the information about the " + relative + " to make a dictionary\n"
                                                                                      "[+] If you don't know all the "
                                                                                      "info, just hit enter when asked!\n",
                               self.cli.colour.green))

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

    def batch(self):
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
                self.profile["age"]]

        del self.profile["birth_day"]
        del self.profile["birth_month"]
        del self.profile["birth_year"]
        del self.profile["age"]

        for value in self.profile.values():
            if value != "":
                info.append(value.upper())
                info.append(value.lower())
                info.append(value.capitalize())

        return info
