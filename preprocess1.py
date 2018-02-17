import json
import pandas as pd
context_data=[]
title_data=[]
question_data=[]
answer_data=[]
questionid_data=[]
with open(r'C:/Users/Shree/Desktop/train-v1.1.json') as file:
    json_file=json.loads(file.read())
    
    for article in json_file['data']:
        title_data.append(article['title'])
    
    
    for article in json_file['data']:
        for i,paragraphs in enumerate(article['paragraphs']):
            context_data.append(paragraphs['context'])
            
    for article in json_file['data']:
        for paragraphs in article['paragraphs']:
            for qas in paragraphs['qas']:
                question_data.append(qas['question'])
                questionid_data.append(qas['id'])
   
    for article in json_file['data']:
        for paragraphs in article['paragraphs']:
            for qas in paragraphs['qas']:
                for answers in qas['answers']:
                    answer_data.append(answers['text'])
    
                

question_answer=pd.DataFrame({'question':question_data,'ques_id':questionid_data})
print(question_answer)