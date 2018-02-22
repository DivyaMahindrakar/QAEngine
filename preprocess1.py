import json
import pandas as pd
context_data=[]
title_data=[]
question_data=[]
answer_data=[]
questionid_data=[]
answerstart_data=[]
mainparagraph_data=[]
counter=list()

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
				answerstart_data.append(answers['answer_start'])
    
for article in json_file['data']:
	for paragraphs in article['paragraphs']:
		counter.append(len(paragraphs['qas']))
     
for i in range(len(context_data)):
	mainparagraph_data.extend([context_data[i]]*counter[i])
     
#print(mainparagraph_data[31])   
answer_startdata=pd.DataFrame({'answer':answer_data,'answer_start':answerstart_data,'question_id':questionid_data,'questions':question_data,'paragraphs':mainparagraph_data})
print(answer_startdata.head(3))
                
