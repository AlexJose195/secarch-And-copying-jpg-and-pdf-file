import os
folder_path = r"C:\Users\acer\New folder"

#print(os.getcwd())
os.chdir(folder_path)
#print(os.getcwd())

os.listdir()
# print(os.listdir())

list_extension = []

for fl in os.listdir():
    # print(fl)
    extension = fl.split(".")[-1]
    list_extension.append(extension)

# print(list_extension)

list_extension =list(set(list_extension))
# print(list_extension)

import shutil
path = os.environ["UserProfile"]+"\\"+"Desktop"+"\\"+"new Folder"
# os.mkdir(path)

try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

for ex in list_extension:
    # print(ex,end=" ")
    if ex == 'pdf' or ex == 'jpg':
        os.mkdir(path+"\\"+ex)
    for fl in os.listdir():
        if ex in fl.split(".")[-1] == 'pdf' or ex in fl.split(".")[-1] == 'jpg':
            shutil.copy(fl,path+"\\"+ex)
