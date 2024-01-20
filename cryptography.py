import hashlib
from chain_ops import return_last_block

def calc_hash(block):

   hash_string = (str(block["index"]) + str(block["date"]) + str(block["data"]) + str(block["prev_hash"]))

   return hashlib.sha256(hash_string.encode()).hexdigest()

