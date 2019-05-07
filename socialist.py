from itertools import permutations
from tqdm import tqdm
import argparse
from colour import *
from profile import Profile

__author__ = "Overwatch Heir"
__version__ = "v1.1.0"
__banner__ = r"""

        ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██╗███████╗████████╗
        ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██║██╔════╝╚══██╔══╝
        ███████╗██║   ██║██║     ██║███████║██║     ██║███████╗   ██║   
        ╚════██║██║   ██║██║     ██║██╔══██║██║     ██║╚════██║   ██║   
        ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║███████║   ██║   
        ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝ """ + '\n'


def message(text, colour_choice):
    return colour_choice + str(text) + colour.end


def display_banner():
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


def socialist(info):
    output_file = open(args.output, 'w+')
    print(message("\r\n[+] Now making a password list with the info you provided...", colour.green))

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


def main():
    info = []

    victim = Profile()
    victim.create('victim')
    victim_info = victim.process()
    info = info + victim_info

    more_questions = str(input(colour.green + "\r\n[+] If you want, we will make YES or NO questions related to the "
                                              "victim's relatives to improve the password list... "
                                              "Do you agree ? (yes/no) : " + colour.end))

    if more_questions == 'yes':

        has_partner = str(input(colour.green + "\r\n[+] Does the victim have a partner ? (yes/no) : " + colour.end))

        if has_partner == 'yes':
            partner = Profile()
            partner.create('partner')
            partner_info = partner.process()
            info = info + partner_info

        has_father = str(input(colour.green + "\r\n[+] Does the victim have a father ? (yes/no) : " + colour.end))

        if has_father == 'yes':
            father = Profile()
            father.create('father')
            father_info = father.process()
            info = info + father_info

        has_mother = str(input(colour.green + "\r\n[+] Does the victim have a mother ? (yes/no) : " + colour.end))

        if has_mother == 'yes':
            mother = Profile()
            mother.create('mother')
            mother_info = mother.process()
            info = info + mother_info

        has_children = str(input(colour.green + "\r\n[+] Does the victim have children ? (yes/no) : " + colour.end))

        if has_children == 'yes':
            children_number = int(input(colour.green + "  [+] How many children has the victim ? : " + colour.end))

            while children_number == 0:
                print(message("  [-] You must enter an integer for the number of children!", colour.red))
                children_number = int(input(colour.green + "  [+] How many children has the victim ?  : " + colour.end))

            for n in range(0, children_number):
                child = Profile()
                child.create('child ' + str(n + 1))
                child_info = child.process()
                info = info + child_info

                del child

    socialist(info)


if __name__ == '__main__':
    colour = Colour()
    display_banner()
    args = parse_args()
    main()
