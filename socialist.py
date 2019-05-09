from itertools import permutations
from tqdm import tqdm
from utils.cli import *
from profile import Profile
import string


info = []


def add_profile(name):
    profile = Profile()
    profile.create(name)
    profile_info = profile.batch()
    info.extend(profile_info)

    del profile


def run():
    output_file = open(args.output, 'w+')
    print(cli.message("\r\n[+] Now making a password list with the info you provided...", cli.colour.green))

    for n in range(1, args.combinations + 1):
        print(cli.message("\n" + str(n) + " words combinations", cli.colour.green))
        num_lines = sum(1 for _ in permutations(info, n))

        for group in tqdm(permutations(info, n), total=num_lines, ncols=100):
            if n == 1:
                output_file.write(''.join(group) + "\n")
            else:
                for element in string.punctuation:
                    output_file.write(element.join(group) + "\n")
                    output_file.write(element.join(group) + "\n")

    print(cli.message("\r\n[+] Password list successfully created!\n", cli.colour.green))


def socialist():
    add_profile('victim')

    more_questions = str(input(cli.colour.green + "\r\n[+] If you want, we will make YES or NO questions related to the "
                                              "victim's relatives to improve the password list... "
                                              "Do you agree ? (yes/no) : " + cli.colour.end))

    if more_questions == 'yes':

        has_partner = str(input(cli.colour.green + "\r\n[+] Does the victim have a partner ? (yes/no) : " + cli.colour.end))

        if has_partner == 'yes':
            add_profile('partner')

        has_expartners = str(
            input(cli.colour.green + "\r\n[+] Does the victim have a expartners ? (yes/no) : " + cli.colour.end))

        if has_expartners == 'yes':
            expartners_number = int(input(cli.colour.green + "  [+] How many expartners has the victim ? : " + cli.colour.end))
            while expartners_number == 0:
                print(cli.message("  [-] You must enter an integer for the number of expartners!", cli.colour.red))
                expartners_number = int(
                    input(cli.colour.green + "  [+] How many expartners has the victim ?  : " + cli.colour.end))

            for n in range(0, expartners_number):
                add_profile('expartner ' + str(n + 1))

        has_father = str(input(cli.colour.green + "\r\n[+] Does the victim have a father ? (yes/no) : " + cli.colour.end))

        if has_father == 'yes':
            add_profile('father')

        has_mother = str(input(cli.colour.green + "\r\n[+] Does the victim have a mother ? (yes/no) : " + cli.colour.end))

        if has_mother == 'yes':
            add_profile('mother')

        has_children = str(input(cli.colour.green + "\r\n[+] Does the victim have children ? (yes/no) : " + cli.colour.end))

        if has_children == 'yes':
            children_number = int(input(cli.colour.green + "  [+] How many children has the victim ? : " + cli.colour.end))

            while children_number == 0:
                print(cli.message("  [-] You must enter an integer for the number of children!", cli.colour.red))
                children_number = int(input(cli.colour.green + "  [+] How many children has the victim ?  : " + cli.colour.end))

            for n in range(0, children_number):
                add_profile('child ' + str(n + 1))

    run()


if __name__ == '__main__':
    cli = Cli()
    cli.banner()
    args = cli.parse_args()
    socialist()
