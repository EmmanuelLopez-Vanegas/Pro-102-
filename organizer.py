import os
import shutil
source = "C:\\Coding\\Python\\C102_assets-main\\C102_assets-main"
destination = "C:\\Coding\\also class 102"
listOfFiles = os.listdir(source)
print(listOfFiles)
for i in listOfFiles:
    name, extension = os.path.splitext(i)
    print(name)
    print(extension)
    if extension == " ":
        continue
    if extension in [".gif",".png",".jpeg",".jpg",".jfif"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "image files"
        path3 = destination + '/' + "image files" + "/" + i
    if os.path.exists(path2):
        print(i)
        shutil.move(path1, path3)
    else:
        os.mkdir(path2)
        shutil.move(path1, path3)
        print(i)