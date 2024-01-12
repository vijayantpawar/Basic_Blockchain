import sys
import os

project_path = '/Users/shrianshagarwal/Documents/projects/Basic_Blockchain'
sys.path.append(os.path.join(project_path, 'BChain'))

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
import time
import json

ZERO_HASH = "0" * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain =[]
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to jeo"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        block = Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction)
        self.chain.append(block.__dict__)
        print(json.dumps([block.__dict__], indent=4))

    def main(self, num_blocks):
        i = 0
        while i < num_blocks:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)
            i += 1

if __name__ == "__main__":
    blockchain = Blockchain()
    num_blocks = int(input("Enter the number of blocks to be mined: "))
    blockchain.main(num_blocks)


