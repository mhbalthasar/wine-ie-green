import os
import sys
import string

RegSystemFile="ie7-reg-"
MinF=0
MaxF=5323
Key2="HKEY_CURRENT_USER"

def readF(FL):
    with open(FL,"rb") as f:
        tmx=f.read()
        st=2
        x=tmx[st]
        dat=""
        while x:
            dat+=chr(x)
            st=st+2
            try:
                x=tmx[st]
            except:
                break;
        fmxr=dat.split("\r")
        InReg=False
        for liner in fmxr:
             line=(liner.replace("\n","").strip())
             #aprint(line)
             if line.startswith("[") and line.endswith("]"):
                 if not InReg:
                     InReg=True
                 else:
                     InReg=False
                     break
             if InReg:
                 print(line)

lst=[]
with open("ie7-regpath.txt","r") as f:
    line=f.readline()
    while line:
        lst.append(line.strip())
        line=f.readline()

for i in range(MinF,MaxF):
    try:
        #readF("export/"+RegSystemFile+str(i)+".reg")
        with open("export/"+RegSystemFile+str(i)+".reg","rb") as f:
            pass
    except:
        print("export/"+RegSystemFile+str(i)+".reg")
        print(lst[i])
        pass
