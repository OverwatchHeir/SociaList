from itertools import permutations
from tqdm import tqdm
import argparse
import calendar
from colour import *

__author__ = "Overwatch Heir"
__version__ = "v1.1.0"
__banner__ = r"""

        ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██╗███████╗████████╗
        ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██║██╔════╝╚══██╔══╝
        ███████╗██║   ██║██║     ██║███████║██║     ██║███████╗   ██║   
        ╚════██║██║   ██║██║     ██║██╔══██║██║     ██║╚════██║   ██║   
        ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║███████║   ██║   
        ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝ """ + '\n'

colour = Colour()
profile = {}
info = []


def message(text, colour_choice):
    return colour_choice + str(text) + colour.end


def display():
    print(message(__banner__, colour.red))
    print(message('     * Version: ' + __version__ + '\n', colour.red),
          message('    * Created by: ' + __author__ + '\n', colour.red),
          message("    * Take a look at README.md file for more info about the program\n", colour.red))


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", required=True, help="path to output wordlist ")
    parser.add_argument("-c", "--combinations", default=3, type=int, help="maximum number of words combinations "
                                                                          "-- default 2")
    return parser.parse_args()


def create_profile():

    print(message("[+] Insert the information about the victim to make a dictionary\n"
                  "[+] If you don't know all the info, just hit enter when asked!\n", colour.green))

    profile["first_name"] = str(input(colour.yellow + "> First Name : " + colour.end).replace(" ", ""))
    profile["last_name"] = str(input(colour.yellow + "> Last Name : " + colour.end).replace(" ", ""))

    birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end).replace(" ", "")
    while len(birthdate) != 0 and len(birthdate) != 8:
        print(message("\r\n[-] You must enter 8 digits for birthday!", colour.yellow))
        birthdate = input(colour.yellow + "> Birthdate (DDMMYYYY): " + colour.end).replace(" ", "")

    profile["birth_day"] = str(birthdate[0:2])
    profile["birth_month"] = str(birthdate[2:4])
    profile["birth_year"] = str(birthdate[-4:])

    profile["pet"] = str(input(colour.yellow + "> Pet Name : " + colour.end).replace(" ", ""))
    profile["music"] = str(input(colour.yellow + "> Music Group : " + colour.end).replace(" ", ""))
    profile["artist"] = str(input(colour.yellow + "> Music Artist : " + colour.end).replace(" ", ""))
    profile["film"] = str(input(colour.yellow + "> Film  : " + colour.end).replace(" ", ""))
    profile["tvshow"] = str(input(colour.yellow + "> TV Show  : " + colour.end).replace(" ", ""))
    profile["sport"] = str(input(colour.yellow + "> Sport : " + colour.end).replace(" ", ""))
    profile["team"] = str(input(colour.yellow + "> Sport Team: " + colour.end).replace(" ", ""))
    profile["city"] = str(input(colour.yellow + "> City : " + colour.end).replace(" ", ""))
    profile["food"] = str(input(colour.yellow + "> Food : " + colour.end).replace(" ", ""))
    profile["car"] = str(input(colour.yellow + "> Car Model : " + colour.end).replace(" ", ""))
    profile["carbrand"] = str(input(colour.yellow + "> Car Brand : " + colour.end).replace(" ", ""))
    profile["celebrity"] = str(input(colour.yellow + "> Celebrity : " + colour.end).replace(" ", ""))


def process_info():
    info.append(profile["birth_day"])
    info.append(profile["birth_month"])
    info.append(calendar.month_name[int(profile["birth_month"])].lower())
    info.append(calendar.month_name[int(profile["birth_month"])].capitalize())
    info.append(calendar.month_name[int(profile["birth_month"])].upper())
    info.append(calendar.month_abbr[int(profile["birth_month"])].lower())
    info.append(calendar.month_abbr[int(profile["birth_month"])].capitalize())
    info.append(calendar.month_abbr[int(profile["birth_month"])].upper())
    info.append(profile["birth_year"])
    info.append(profile["birth_year"][-2:])

    del profile["birth_day"]
    del profile["birth_month"]
    del profile["birth_year"]

    for value in profile.values():
        if value != "":
            info.append(value.upper())
            info.append(value.lower())
            info.append(value.capitalize())

    return info


def socialist(info):
    output_file = open(args.output, 'w+')
    print(message("\r\n[+] Now making a password list...", colour.green))

    for n in range(1, args.combinations + 1):
        print(message("\n" + str(n) + " words combinations", colour.green))
        num_lines = sum(1 for line in permutations(info, n))

        for group in tqdm(permutations(info, n), total=num_lines, ncols=100):
            if n == 1:
                output_file.write(''.join(group) + "\n")
            else:
                output_file.write('.'.join(group) + "\n")
                output_file.write('_'.join(group) + "\n")
                output_file.write('$'.join(group) + "\n")
                output_file.write('%'.join(group) + "\n")
                output_file.write('&'.join(group) + "\n")
                output_file.write('-'.join(group) + "\n")

    print(message("\r\n[+] Password list successfully created!\n", colour.green))


if __name__ == '__main__':
    display()
    args = parse_args()
    create_profile()
    socialist(process_info())
