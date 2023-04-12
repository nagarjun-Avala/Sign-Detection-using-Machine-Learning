import cv2
import os
from image_processing import func

path = "data/train"
path_processed = "data2"

label = 0
total_iamges_num = 0
train_num = 0
test_num = 0

if not os.path.exists(path_processed):
    os.makedirs(path_processed)
if not os.path.exists(path_processed + "/train"):
    os.makedirs(path_processed + "/train")
if not os.path.exists(path_processed + "/test"):
    os.makedirs(path_processed + "/test")

for (dirpath, dirnames, filenames) in os.walk(path):
       
    for dirname in dirnames:
        for (direcpath, direcnames, files) in os.walk(path+"/"+dirname):
            
            if not os.path.exists(path_processed+"/train/"+dirname):
                os.makedirs(path_processed+"/train/"+dirname)
            if not os.path.exists(path_processed+"/test/"+dirname):
                os.makedirs(path_processed+"/test/"+dirname)

            num=0.75*len(files)
            
            i = 0
            for file in files:
                total_iamges_num += 1
                actual_path = path+"/"+dirname+"/"+file
                actual_path_train = path_processed+"/"+"train/"+dirname+"/"+file
                actual_path_test = path_processed+"/"+"test/"+dirname+"/"+file
                
                img = cv2.imread(actual_path, 0)
                bw_image = func(actual_path)
                if i < num:
                    train_num += 1
                    cv2.imwrite(actual_path_train, bw_image)
                else:
                    test_num += 1
                    cv2.imwrite(actual_path_test, bw_image)

                i = i+1
        print(dirname," - Done")
        label = label+1
print("Total images : ",total_iamges_num)
print("Total train images : ",train_num)
print("Total test images : ",test_num)