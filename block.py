import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        sha = hasher.sha256()
        data_string = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(data_string)
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genisis block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
 


