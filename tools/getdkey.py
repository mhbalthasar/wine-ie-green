import os
import sys

RegSystemFile="ie8-system-reg.diff"
RegUserDefFile="ie8-userdef-reg.diff"
RegUserFile="ie8-user-reg.diff"
Key1="HKEY_LOCAL_MACHINE"
Key2="HKEY_CURRENT_USER"

with open(RegSystemFile,"r") as f:
    line=f.readline()
    while line:
        if line.startswith("+"):
            if line.startswith("+["):
                lnr=line.replace("\n","")
                lnr=lnr.replace("+[","+["+Key1+"\\\\")
                arr=lnr.split(' ')
                sts=arr[len(arr)-1]
                if lnr.endswith(" "+sts):
                    lnr=lnr[:len(lnr)-len(sts)]
                lnr=lnr.replace("\\\\","\\")
                print(lnr[2:len(lnr)-2])
        line=f.readline()

with open(RegUserDefFile,"r") as f:
    line=f.readline()
    while line:
        if line.startswith("+"):
            if line.startswith("+["):
                lnr=line.replace("\n","")
                lnr=lnr.replace("+[","+["+Key2+"\\\\")
                arr=lnr.split(' ')
                sts=arr[len(arr)-1]
                if lnr.endswith(" "+sts):
                    lnr=lnr[:len(lnr)-len(sts)]
                lnr=lnr.replace("\\\\","\\")
                print(lnr[2:len(lnr)-2])
        line=f.readline()

with open(RegUserFile,"r") as f:
    line=f.readline()
    while line:
        if line.startswith("+"):
            if line.startswith("+["):
                lnr=line.replace("\n","")
                lnr=lnr.replace("+[","+["+Key2+"\\\\")
                arr=lnr.split(' ')
                sts=arr[len(arr)-1]
                if lnr.endswith(" "+sts):
                    lnr=lnr[:len(lnr)-len(sts)]
                lnr=lnr.replace("\\\\","\\")
                print(lnr[2:len(lnr)-2])
        line=f.readline()

