# Verify if the environment is good and all dependencies are installed
import sys

def verify_environment():
  if sys.version_info[0] != 2 or sys.version_info[1] < 7:
    raise Exception("This program requires Python version 2.7")
  print("Success! Python {} is installed.".format(sys.version_info))
