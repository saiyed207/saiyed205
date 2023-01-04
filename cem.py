import csv
import numpy as np
with open("dataset.csv","r") as f:
    reads= csv.reader (f)
    tmp_lst=np.array(list(reads))
    #print(tmp_lst)
concept=np.array(tmp_lst[:,:-1])
target=np.array(tmp_lst[:,-1])
for i in range (len(target)):
    if(target[i]=="yes"):
        specific_h=concept[i]
        break
h=[]
generic_h=[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
print(generic_h)
for i in range (len(target)):
    if(target[i]=="yes"):
        for j in range(len(specific_h)):
            if (specific_h[j]!=concept[i][j]):
                specific_h[j]="?"
                generic_h[j][j]="?"
    else:
        for j in range(len(specific_h)):
            if(specific_h[j]!=concept[i][j]):
                generic_h[i][j]=specific_h[j]
                #print(generic_h)
            else:
                generic_h[j][j]="?"
                #print(j,generic_h)
    print("step",i+1)
    print("The Most Generic is :",generic_h)
    print("The Most Specific is : ", specific_h)
