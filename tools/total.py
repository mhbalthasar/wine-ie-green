import os
import sys
import string

RegSystemFile="ie8-reg-"
MinF=0
MaxF=6571
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
        NextIsHEX=False
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
                 if NextIsHEX:
                     print("  "+line)
                 else:
                     print(line)
                 if line.endswith(",\\"):
                    NextIsHEX=True
                 else:
                    NextIsHEX=False


for i in range(MinF,MaxF):
    try:
        readF("export/"+RegSystemFile+str(i)+".reg")
    except:
        pass
