import os
import sys

RegFile="ie7-system-reg.diff"
Key="HKEY_LOCAL_MACHINE"

#HKEY_CURRENT_USER

print("Windows Registry Editor Version 5.00\n")

with open("ie7-system-reg.diff","r") as f:
    line=f.readline()
    while line:
        if line.startswith("+"):
            if line.startswith("+#time="):
                pass
            elif line.startswith("++"):
                pass
            elif line.startswith("+["):
                lnr=line.replace("\n","")
                lnr=lnr.replace("+[","+["+Key+"\\\\")
                arr=lnr.split(' ')
                sts=arr[len(arr)-1]
                if lnr.endswith(" "+sts):
                    lnr=lnr[:len(lnr)-len(sts)]
                lnr=lnr.replace("\\\\","\\")
                print(lnr[1:])
            else:
                print(line.replace("\n","")[1:])
        line=f.readline()

