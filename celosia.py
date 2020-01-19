# include standard modules
import argparse
SW_VER='0.1.0'
SW_DATE='19-Jan-2020'
VERSION_STR=f'Celosia version {SW_VER}, {SW_DATE}'

def add_arguments(parser):
  parser.add_argument("-v", "--version", help="show program version", action="store_true")
  #parser.add_argument("-v", "--version", help="show program version", action="store_true")


if __name__ == '__main__':
  # initiate the parser
  parser = argparse.ArgumentParser()
  add_arguments(parser)

  # read arguments from the command line
  args = parser.parse_args()

  # check for --version or -V
  if args.version:
    print(VERSION_STR)