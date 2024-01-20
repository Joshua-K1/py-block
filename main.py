import argparse
from chain import Blockain
from block import Block
from writer import write_chain
import datetime as dt
from logger import event_logger

def main():
   # Create new blockchain
   blockchain = Blockain()

   block = Block(4, dt.datetime.now(), "Transaction 4", "")
   block = block.return_dict()

   blockchain.add_block(Block(1, dt.datetime.now(), "Transaction 1", ""))

   for block in blockchain.chain: 
    print("Block #: " + str(block.index)) 
    print("Timestamp: " + str(block.timestamp)) 
    print("Data: " + str(block.data)) 
    print("Prev Hash: " + str(block.previous_hash)) 

   # Print as CSV
    print(str(block.index) + "," + str(block.timestamp) + "," + str(block.data) + "," + str(block.previous_hash))
    log_entry = str(block.index) + "," + str(block.timestamp) + "," + str(block.data) + "," + str(block.previous_hash)

   chain_log_test = ('this', 'is', 'a', 'test')

   # Convert chain object to dict

   dict = {
      "index":"" ,
      "timestamp": "",
      "data": "",
      "previous_hash": ""
   }


   # Convert dict to json and paste to file
   
   write_chain(chain_log_test)
   event_logger.info('Written to chain file')


if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
