#-*- coding: utf-8 -*-
import re
import json

def read_file(filename=''):
    if '.json' in filename:
        with open(filename, 'r') as f:
            data = json.load(f)
            data = data['data'] # aihub 기계독해의 경우
            print(f'type\t{type(data)}\nkeys\t{data[0]}')
            print(json.dumps(data[0], indent='\t', ensure_ascii=False))



def main():

    print(f'{"*"*50}    start    {"*"*50}')
    filename = './data/aihub_mrc/ex1.json'
    read_file(filename)
    

    # 최종 파일은 tsv 형식
    # # id, context, question, answer_text, answer_start




if __name__=="__main__":
    main()