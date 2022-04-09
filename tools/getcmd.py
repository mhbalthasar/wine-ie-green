import os
import sys

with open("ie8-regpath.txt","r") as f:
    line=f.readline()
    i=0
    while line:
        print("reg export \""+line.strip()+"\" export\\ie8-reg-"+str(i)+".reg")
        i=i+1
        line=f.readline()

