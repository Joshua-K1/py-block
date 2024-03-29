from cryptography import calc_hash
from logger import event_logger
import datetime as date
from typing import Dict
import json
import os 

# @TODO: Function to search chain items for specific phrases

chain_file = './chain/chain.json'

def establish_chain() -> bool:
   event_logger.info("Establishing if chain exists")

   if os.path.exists(chain_file) and os.path.getsize(chain_file) == 0:
      event_logger.info("Chain file exists but is empty")
      event_logger.info("Creating Genesis block.")

      with open(chain_file, 'a') as file:
         json.dump(create_genesis_block(), file, indent=4)

      event_logger.info("Written genesis block to chain file")

      return True

   elif os.path.exists(chain_file) and os.path.getsize(chain_file) > 0:
      event_logger.info("Chain exists and has a size greater than 0")

      # Read in file, validate that json is valid
      chain_file_data = validate_chain_json(chain_file)
      if (chain_file_data):
         list_chain_blocks()

      return True

   else: 
      event_logger.info("Chain file does not exist")

      return False


def create_genesis_block() -> Dict:
   initial_block = {
      "blocks": [
         {"index": 0, "date": str(date.datetime.now()), "data": "Genesis Block", "hash": "0"}
      ]
   }

   return initial_block


def validate_chain_json(chain_data) -> bool:
   event_logger.info("Validating chain")
   try:
      with open(chain_data, 'r') as data:
         _ = json.loads(data.read())
         event_logger.info("Chain is valid")

         return True

   except (ValueError, FileNotFoundError) as err:
      event_logger.error(err)
      event_logger.info("Chain is invalid")
      return False


def list_chain_blocks():
   event_logger.info("Listing blocks currently in chain")
   try:
      with open(chain_file, 'r') as data:
         contents = json.loads(data.read())
         event_logger.info("Opening chain file")

      for block in contents["blocks"]:
         print(block)

   except (ValueError, FileNotFoundError) as err:
      event_logger.error(err)
      event_logger.error("Failed to read chain file, chain structure is invalid or file does not exist.")

def return_last_block():
   event_logger.info("Getting last block in chain")
   try:
      with open(chain_file, 'r') as data:
         contents = json.loads(data.read())
         event_logger.info("Opening chain file")
         last_block = contents["blocks"][-1]

         return last_block

   except (ValueError, FileNotFoundError) as err:
      event_logger.error(err)
      event_logger.error("Failed to read chain file, chain structure is invalid or file does not exist.")


def add_block(blockData):
   event_logger.info("Adding new block to chain.")
   last_block = return_last_block()

   if last_block is not None:
      last_block_index = last_block["index"]
      new_block_index = last_block_index + 1
      new_block_data = str(blockData)
      new_block_date = str(date.datetime.now())
      previous_block_hash = last_block["hash"]
      new_block_hash = calc_hash(str(new_block_index), new_block_data, new_block_date, previous_block_hash)
      new_block = {
         "index": new_block_index,
         "date": new_block_date,
         "data": new_block_data,
         "hash": new_block_hash
      }

      try:
         with open(chain_file, 'r') as file:
            blockchain = json.load(file)
            blockchain['blocks'].append(new_block)

         with open(chain_file, 'w') as file:
            json.dump(blockchain, file, indent=4)

      except (ValueError, FileNotFoundError) as err:
         event_logger.error(err)
         event_logger.error("Failed to read chain file, chain structure is invalid or file does not exist.")

