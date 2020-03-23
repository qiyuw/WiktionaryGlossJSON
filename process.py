import os
import json
from tqdm import tqdm
from datetime import datetime

def stream_read_json(fn):
    '''
    Deprecated.
    In case the dump file is stream JSON
    '''
    total_size = os.path.getsize(fn)
    start_time = datetime.now()
    import json
    import re
    start_pos = 0
    with open(fn, 'r') as f:
        while True:
            try:
                obj = json.load(f)
                yield obj
                return
            except ValueError as e:
                f.seek(start_pos)
                end_pos = int(re.match('Extra data: line \d+ column \d+ .*\(char (\d+).*\)',
                                    e.args[0]).groups()[0])
                json_str = f.read(end_pos)
                obj = json.loads(json_str)
                start_pos += end_pos
                print("\rLoading stream file, {}/{}, {}%, time cost {}.".format(start_pos, total_size, (start_pos/total_size)*100, datetime.now()-start_time), end="")
                yield obj

def get_gloss(words):
    print('# of words to be processed to dict', len(words))
    print('processing...')
    res = {}
    for w in tqdm(words):
        try:
            word = w['word'].lower()
            defs = [d['glosses'] for d in w['senses']]
            defs = [d for d_li in defs for d in d_li]
            if word not in res.keys():
                res[word] = defs
            else:
                # in case duplicate
                # print('duplicated words:', word)
                res[word] = defs + res[word]
        except:
            pass
    print('# of valid words', len(res.keys()))
    return res

if __name__ == '__main__':
    pre_fn = '<relativePath>/'
    json_fn = pre_fn + 'wikt.words'
    out_fn = pre_fn + 'wikt.dict.sample'
    print('loading data...')
    # load word by lines
    with open(json_fn, 'r') as f:
        w_li = f.readlines()
    word_jsons = []
    for w in w_li:
        word_jsons.append(json.loads(w[:-1]))
    # extract glosses
    word_dict = get_gloss(word_jsons)
    with open(out_fn, 'w') as f:
        f.write(json.dumps(word_dict))