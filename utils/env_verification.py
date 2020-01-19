# Verify if the environment is good and all dependencies are installed
import sys

def verify_environment(args):
  if sys.version_info[0] != 3 or sys.version_info[1] < 7:
    raise Exception("This script requires Python version 3.7")
  print(f"Success! Python {sys.version_info} is installed.")
