from sys import path
from os import listdir
from os.path import split,join,isdir

folder_name=[]

rmfolder=[
    'School_project',
    '',
]

ignore=['lawlgz.logzz','log.txt','.git']

for i in range(len(rmfolder)):
    rmfolder[i]=split(rmfolder[i])[len(split(rmfolder[i]))-1]

for i in listdir(split(path[0])[0]):
    if i not in rmfolder and isdir(join(split(path[0])[0],i)): 
        folder_name.append(join(split(path[0])[0],i))
    else: pass
a=[]
a.extend(folder_name)
prostitute=[]
for i in a:
    for j in listdir(i):
        if j not in ignore and (j not in ignore or join(folder_name[folder_name.index(i)],j) not in ignore):
            prostitute.append(join(folder_name[folder_name.index(i)],j))
        else: pass
folder_name=prostitute
