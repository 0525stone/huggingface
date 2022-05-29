#-*- coding: utf-8 -*-
import re
import os
import json
import pandas as pd

def read_file(filename=''):
    if '.json' in filename:
        with open(filename, 'r') as f:
            data = json.load(f)
            data = data['data'] # aihub 기계독해의 경우
            # print(data[0].keys())
            # print(json.dumps(data[0], indent='\t', ensure_ascii=False))

    return data
            

def aihub_mrc(json_data):
    """
    aihub 에 해당됨
    - 기계독해
    - 도서자료 기계독해
    - 일반상식

    Objective 
    - id : 6513252-10-1
    - context : 지문(텍스트)
    - question : TMT 사가 에이 위일 호를 어떠한 배로 개조했는가?
    - answer_text : 기름제거선
    - answer_start : 165

    aihub_mrc json

    """
    print(f'{len(json_data)}')
    
    save_df = pd.DataFrame(columns=['id','context','question','answer_text','answer_start'])
    for idx, data in enumerate(json_data):
        # if idx<3:
        if idx%100==0:
            print(f'{idx} just passed')

        for d in data['paragraphs'][0]['qas']:
            # print(d)
            save_df = save_df.append({'id':d['id'],
                'context':data['paragraphs'][0]['context'],
                'question' : d['question'],
                'answer_text':d['answers'][0]['text'],
                'answer_start':d['answers'][0]['answer_start']},
                ignore_index=True)
    print('Done converting data format')
    return save_df



def main():

    print(f'{"*"*50}    start    {"*"*50}')
    filename = './data/aihub_mrc/ex2.json'
    data = read_file(filename)

    # aihub mrc
    save_df = aihub_mrc(data)
    # others



    savename = filename.split('/')[-1].split('.')[0]
    savename = os.path.join('./data/refined',savename+'.tsv')
    print(savename)
    save_df.to_csv(savename, sep='\t', index=False)

    check_df = pd.read_csv(savename, sep='\t')
    print(check_df.head())
    
    

    # 최종 파일은 tsv 형식
    # # id, context, question, answer_text, answer_start




if __name__=="__main__":
    main()