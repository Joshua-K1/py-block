from writer import write_chain
from logger import event_logger
import datetime as date
import json
import os 

chain_file = './chain/chain_test.json'


def establish_chain() -> bool:
   event_logger.info("Establishing if chain exists")

   if os.path.exists(chain_file) and os.path.getsize(chain_file) == 0:
      event_logger.info("Chain file exists but is empty")
      # Read in file and create genesis block

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


def create_genesis_block():
   initial_block = {
      "blocks": [
         {"index": 0, "date": str(date.datetime.now()), "data": "Genesis Block", "prev_hash": "0"}
      ]
   }

   return initial_block


def validate_chain_json(chain_data):
   event_logger.info("Validating chain")
   try:
      with open(chain_data, 'r') as data:
         contents = json.loads(data.read())
         event_logger.info("Chain is valid")

   except ValueError as err:
      event_logger.error(err)
      event_logger.info("Chain is invalid")
      return False # @TODO: Maybe not return False and an object in the same func? Bad Practice?

   return contents


def list_chain_blocks():
   event_logger.info("Listing blocks currently in chain")

   try:
      with open(chain_file, 'r') as data:
         contents = json.loads(data.read())
         event_logger.info("Opening chain file")


      for block in contents["blocks"]:
         print(block)

   except ValueError as err:
      event_logger.error(err)
      event_logger.info("Unable to read chain, chain is invalid")


def return_last_block():
   event_logger.info("Getting last block in chain")
   try:
      with open(chain_file, 'r') as data:
         contents = json.loads(data.read())
         event_logger.info("Opening chain file")

   except ValueError as err:
      event_logger.error(err)
      event_logger.info("Unable to read chain, chain is invalid")
      return False # @TODO: Maybe not return False and an object in the same func? Bad Practice?

   last_block = contents["blocks"][-1]

   return last_block

