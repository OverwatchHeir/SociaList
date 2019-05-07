import colour
from colour import *
import calendar

colour = Colour()


class Profile:

    def __init__(self):
        self.profile = {}

    def message(self, text, colour_choice):
        return colour_choice + str(text) + colour.end

    def create(self, relative):
        print(self.message("\n[+] Insert the information about the " + relative + " to make a dictionary\n"
                      "[+] If you don't know all the info, just hit enter when asked!\n", colour.green))

        self.profile["first_name"] = str(input(colour.yellow + "> First Name : " + colour.end).replace(" ", ""))
        self.profile["last_name"] = str(input(colour.yellow + "> Last Name : " + colour.end).replace(" ", ""))

        birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)
        while len(birthdate) == 0 or len(birthdate) != 8:
            print( self.message("\r\n[-] You must enter 8 digits for birthday!\n", colour.red))
            birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end)

        self.profile["birth_day"] = str(birthdate[0:2])
        self.profile["birth_month"] = str(birthdate[2:4])
        self.profile["birth_year"] = str(birthdate[-4:])

        self.profile["pet"] = str(input(colour.yellow + "> Pet Name : " + colour.end).replace(" ", ""))
        self.profile["music"] = str(input(colour.yellow + "> Music Group : " + colour.end).replace(" ", ""))
        self.profile["artist"] = str(input(colour.yellow + "> Music Artist : " + colour.end).replace(" ", ""))
        self.profile["film"] = str(input(colour.yellow + "> Film  : " + colour.end).replace(" ", ""))
        self.profile["tvshow"] = str(input(colour.yellow + "> TV Show  : " + colour.end).replace(" ", ""))
        self.profile["sport"] = str(input(colour.yellow + "> Sport : " + colour.end).replace(" ", ""))
        self.profile["team"] = str(input(colour.yellow + "> Sport Team: " + colour.end).replace(" ", ""))
        self.profile["city"] = str(input(colour.yellow + "> City : " + colour.end).replace(" ", ""))
        self.profile["food"] = str(input(colour.yellow + "> Food : " + colour.end).replace(" ", ""))
        self.profile["car"] = str(input(colour.yellow + "> Car Model : " + colour.end).replace(" ", ""))
        self.profile["carbrand"] = str(input(colour.yellow + "> Car Brand : " + colour.end).replace(" ", ""))
        self.profile["celebrity"] = str(input(colour.yellow + "> Celebrity : " + colour.end).replace(" ", ""))

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
                self.profile["birth_year"][-2:]]

        del self.profile["birth_day"]
        del self.profile["birth_month"]
        del self.profile["birth_year"]

        for value in self.profile.values():
            if value != "":
                info.append(value.upper())
                info.append(value.lower())
                info.append(value.capitalize())

        return info
