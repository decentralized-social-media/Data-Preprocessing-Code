from datetime import timedelta
import time
import io
import pprint
from pick import pick
import pandas as pd

# steem-python is the official STEEM library for Python
from steem import Steem
## first, we initialize Steem class with Steemit API
stm = Steem(nodes=["https://api.steemit.com"])
from steem.blockchain import Blockchain
from steem.account import Account
#create a new data frame for the collected data
columnlist =['parent author', 'parent permlink',
                             'author','permlink','title','body','json metadata',
                             'timestamp','block num','profile json metadata','profile posting json metadata']
data_generate = pd.DataFrame(columns = columnlist)


class Find_comment(object):
    def comment(self, comment_event):
        account_name = comment_event['author']
        #find corresponding author's account profile
        account_profile = Account(account_name)
        #data extracted from comment and user profile
        data = [comment_event['parent_author'],
                comment_event['parent_permlink'],
                comment_event['author'],
                comment_event['permlink'],
                comment_event['title'],
                comment_event['body'],
                comment_event['json_metadata'],
                comment_event['timestamp'].isoformat(),
                comment_event['block_num'],
                account_profile['json_metadata'],
                account_profile['posting_json_metadata']]
        #add the piece of comment into the data file
        data_generate.loc[len(data_generate.index)+1] = data

if __name__ == "__main__":
    fc = Find_comment()
    blockchain = Blockchain(steemd_instance=stm)
    duration_s = 60 * 60 * 24
    #calculate the number of blocks per day
    blocks_per_day = int(duration_s / 3)
    #get the block number for current comment
    current_block_num = blockchain.get_current_block_num()
    last_block_id = current_block_num + blocks_per_day
    for block in blockchain.history(start_block =  current_block_num, end_block = last_block_id,filter_by=["comment"]):
        fc.comment(block)
    #export to local file
    data_generate.to_excel('filename')
