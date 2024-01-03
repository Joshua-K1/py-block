import argparse
from chain import Blockain

def main(args):
   print(args.message)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Process external arguments")
   parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   
   args = parser.parse_args()

   main(args)
