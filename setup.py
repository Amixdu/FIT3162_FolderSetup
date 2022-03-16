import os
def createFolder(name):
    d = "D:\Study\SEM_6\FIT3162\FolderPrep\\result"
    p = (r'{}/'+str(name)).format(d) # path to be created

    try:
        os.makedirs(p)
    except OSError:
        pass


name = "train"
createFolder(name)
name = "val"
createFolder(name)