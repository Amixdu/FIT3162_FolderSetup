import shutil
import os 

src_folder = "D:\Study\SEM_6\FIT3162\FolderPrep\data"

dest_folder_train = "D:\Study\SEM_6\FIT3162\FolderPrep\\result\\train"
dest_folder_test = "D:\Study\SEM_6\FIT3162\FolderPrep\\result\\val"

train_annotation = "D:\Study\SEM_6\FIT3162\FolderPrep\\anomaly_train_video.txt"
test_annotation = "D:\Study\SEM_6\FIT3162\FolderPrep\\anomaly_val_video.txt"

with open(train_annotation) as f:
    lines = f.readlines()

train_words = []
for i in range (len(lines)):
    word = lines[i].split()[0]
    train_words.append(word)

with open(test_annotation) as f:
    lines = f.readlines()

test_words = []
for i in range (len(lines)):
    word = lines[i].split()[0]
    test_words.append(word)


# COPYING TRAIN VIDS
for video in os.listdir(src_folder):
    if video in train_words:
        src = src_folder + "\\" + video
        shutil.copy(src, dest_folder_train)

# COPYING TEST VIDS
for video in os.listdir(src_folder):
    if video in test_words:
        src = src_folder + "\\" + video
        shutil.copy(src, dest_folder_test)

# FILES IN ANNOTATION THAT ARE NOT AVAILABLE (TEST)
# print("############FILES IN ANNOTATION THAT ARE NOT AVAILABLE (TRAIN)########")

train_not_available = []
for file in (train_words):
    if file not in (os.listdir(src_folder)):
        train_not_available.append(file)


test_not_available = []
for file in (test_words):
    if file not in (os.listdir(src_folder)):
        test_not_available.append(file)


# Creating New Annotation Files

# Train
with open(train_annotation) as f:
    lines = f.readlines()

file = open("result\\train.txt","w+")
for i in range (len(lines)):
    word = lines[i].split()[0]
    if word not in train_not_available:
        file.write(lines[i])

file.close()


# Test
with open(test_annotation) as f:
    lines = f.readlines()

file = open("result\\test.txt","w+")
for i in range (len(lines)):
    word = lines[i].split()[0]
    if word not in test_not_available:
        file.write(lines[i])

file.close()
        
        

