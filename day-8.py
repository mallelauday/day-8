import math
import random
import pandas as pd
import numpy as np
def generate_data(n):
    data=[]
    for i in range(n):
        marks=random.randint(0,100)
        attendance=random.randint(0,100)
        assignment =random.randint(0,50)
        performance=(marks*0.5+assignment*0.5)*(attendance/100)
        data.append([i+1,marks,attendance,assignment,round(performance,2)])
    return data
def classification(data):
    result={}
    for s in data:
        id,m,a,asg,p=s
        if m<40 or a<50:
            result[id]="at risk"
        elif m>90 and a>80:
            result[id]="top performance"
        elif m>=71:
            result[id]="good"
        else:
            result[id]="avg"
    return result
def analyzer(data,catagories):
    df=pd.DataFrame(data,columns=["id","marks","attendance","assignment","performance"])
    df["catagories"]=df["id"].map(catagories)
    marks=np.array(df["marks"])
    mean=sum(marks)/len(marks)
    std=np.std(marks)
    maxMarks=np.max(marks)
    mn=min(marks)
    mx=max(marks)
    df["normalized"]=[(x - mn)/(mx - mn) if mx != mn else 0 for x in marks]
    if std<15:
        insight="Stable academic system"
    else:
        insight="moderate academic system"
    return df,(round(mean,2),round(std,2),maxMarks),insight
n=5
data=generate_data(n)
catagories=classification(data)
df,stats,insight=analyzer(data,catagories)
print(df)
print(catagories)
print(stats)
print(insight)