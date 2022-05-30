"""
aihub에 있는 korquad 형식의 데이터셋들을 json 으로 바꾸는 과정

"""
import os
import json
import random
import copy

random.seed(25)


def read_file(filename):
    with open (filename, 'r') as f:
        total = json.load(f)
        data = total['data']
        del total['data']
    return data, total


def split_json(data, total, n_split=0):
    if not n_split:
        n_split = int(len(data)*0.1)
        print(f'total number : {len(data)}\tsplit number : {n_split}')
    
    shuffled_data = random.shuffle(data)
    train = copy.deepcopy(total)    
    train['data'] = data[n_split:]

    val = copy.deepcopy(total)
    val['data'] = data[:n_split]

    small = copy.deepcopy(total)
    small['data'] = data[:100]

    print(f'train\t{len(train["data"])}\nval\t{len(val["data"])}\nsmall\t{len(small["data"])}')

    return train, val, small



def main():
    filename = './data/raw/aihub_nor_know.json'
    data, total = read_file(filename)

    train, val, small = split_json(data,total)

    savename = filename.split('/')[-1].split('.')[0]
    print(savename)

    trainname = os.path.join('./data/refined',savename+'_train.json')
    valname = os.path.join('./data/refined',savename+'_val.json')
    smallname = os.path.join('./data/refined',savename+'_small.json')
    
    with open(trainname,'w') as f:
        json.dump(train, f, indent=4, sort_keys=True)
    with open(valname,'w') as f:
        json.dump(val, f, indent=4, sort_keys=True)
    with open(smallname,'w') as f:
        json.dump(small, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()