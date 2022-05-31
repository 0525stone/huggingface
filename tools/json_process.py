"""
정리 필요함
- argparse로 json 이름 받아오게
- savename 을 입력받은 이름을 기준으로 출력하게
- 함수화
"""

import argparse
import json


def json_formalize(filename):

    # filename = '../data/aihub/mrc/aihub_mrc_noa.json'

    with open (filename, 'r') as f:
        total = json.load(f)
        data = total['data']

    with open ('./data/aihub/mrc/aihub_mrc_clue_ar.json', 'w') as f:
        json.dump(total, f, indent=4, sort_keys=True)


def json_concat(filename1, filename2, savename):
    pass



def main():
    print('started')
    # json_formalize('./data/aihub/mrc/aihub_mrc_clue.json')
    filename1 = '../data/aihub/mrc/aihub_mrc_noa.json'
    filename2 = '../data/aihub/mrc/aihub_mrc_clue.json' 
    savename = '../data/aihub/mrc/aihub_mrc_noa_clue.json'
    json_concat(filename1, filename2, savename)



if __name__ =='__main__':
    main()