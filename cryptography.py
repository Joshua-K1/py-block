import hashlib

def calc_hash(index, date, data, prev_hash):
   hash_string = (index + date + data + prev_hash)

   return hashlib.sha256(hash_string.encode()).hexdigest()
