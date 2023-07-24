import csv
import itertools

def parse_txt(filepath):
    data=[]
    with open(filepath,'r',encoding='utf-8') as file:
        line=file.readline()
        while line:
            data.append(line)
            line=file.readline()
    return data

def divide_txt(data):
    Headings=[]
    Questions=[]
    for i in data:
        if(i[:2]=="# "):
            i=i.replace("\n","")
            i=i.replace("#","")
            Headings.append(i)
        if(i[:4]=="### "):
            i=i.replace("\n","")
            i=i.replace("#","")
            Questions.append(i)


    return Questions

        
            
