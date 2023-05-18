from utils import parse_raw_data as prd
from utils import db as mdb


db = mdb.setup_from_cfg('config.json')
coll = db.get_collection('protein')

queue = []

for p in prd.process_plus('./raw_data/plus.txt'):
    queue.append({'data': p, 'render': None, 'valid': True})

for p in prd.process_minus('./raw_data/minus.txt'):
    queue.append({'data': p, 'render': None, 'valid': False})

print("Adding new documents to db ({})".format(len(queue)))
coll.insert_many(queue, ordered=False)