#copyfile()= copies content of a file
#copy() = copyfile() + permission mode+ destination can ne a directory
#copy2() = copy() +metadata
import shutil


shutil.copyfile("test.txt", "copy.txt") #src, dst.