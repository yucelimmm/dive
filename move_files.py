import os

source = "D:\\python\\test.txt"
dest = "C:\\Users\\hacim1\\Desktop\\test.txt"

if os.path.exists(dest):
    print("There is already a file in there")
elif os.path.isfile == False:
    print("no path")
else:
    os.replace(source, dest)
    print(source + "was moved to new destination.")

