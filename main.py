import argparse
from chain import Blockain
from block import Block
from writer import write_chain
import datetime as dt
from logger import event_logger
from chain_ops import establish_chain

def main():
   # Create new blockchain
   blockchain = Blockain()
   
   # Check that chain exists
   establish_chain()

   block = Block(4, dt.datetime.now(), "Transaction 4", "")
   block = block.return_dict()

   blockchain.add_block(Block(1, dt.datetime.now(), "Transaction 1", ""))

   # Convert chain object to dict

   dict = {
      "index":"" ,
      "timestamp": "",
      "data": "",
      "previous_hash": ""
   }


   # Convert dict to json and paste to file
   
if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
