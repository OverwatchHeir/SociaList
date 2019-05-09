import argparse
from utils.colour import Colour


class Cli:

    def __init__(self):
        self.colour = Colour()
        self.author = "Overwatch Heir"
        self.version = "v1.1.0"

        self.logo = r"""

                ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██╗███████╗████████╗
                ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██║██╔════╝╚══██╔══╝
                ███████╗██║   ██║██║     ██║███████║██║     ██║███████╗   ██║   
                ╚════██║██║   ██║██║     ██║██╔══██║██║     ██║╚════██║   ██║   
                ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║███████║   ██║   
                ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝ """ + '\n'

    def message(self, text, colour_choice):
        return colour_choice + str(text) + self.colour.end

    def banner(self):
        print(self.message(self.logo, self.colour.red))
        print(self.message('     * Version: ' + self.version + '\n', self.colour.red),
              self.message('    * Created by: ' + self.author + '\n', self.colour.red),
              self.message("    * Take a look at README.md file for more info about the program\n", self.colour.red))

    def parse_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("-o", "--output", required=True, help="path to output wordlist ")
        parser.add_argument("-c", "--combinations", default=3, type=int, help="maximum number of words combinations "
                                                                              "-- default 2")
        return parser.parse_args()
