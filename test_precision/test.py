from deepface import DeepFace
import cv2
import os
from glob import glob
import seaborn as sns

from pathlib import Path
import matplotlib.pyplot as plt

#


def ass4_dataset():
    folder_path = '../test_precision/Caltech_CropFaces'
    # folder_path='../dataset'
    image_files = glob(os.path.join(folder_path, '*.jpg'))
    count=0
    time=0
    for i in image_files:
        time+=1
        print("detecting "+str(time)+"th images in ass4")
        try:
            img=cv2.imread(i)
            DeepFace.extract_faces(img)
        except Exception:
            count+=1
    precise=(len(image_files)-count)/len(image_files)
    print(precise)
    return precise


def vgg_examples():
    folder_path="../test_precision/vgg_samples"
    count = 0
    time = 0
    image_files=glob(os.path.join(folder_path, "**/*.jpg"), recursive=True)

    for file_path in image_files:
        time+=1
        print("detecting "+str(time)+"th images in vgg")
        try:
            img=cv2.imread(file_path)
            DeepFace.extract_faces(img)
        except Exception:
            count+=1
    precise=(len(image_files)-count)/len(image_files)
    print(precise)
    return precise

def LFW_dataset():
    folder_path="../test_precision/LFW_dataset"
    count = 0
    time = 0
    image_files=glob(os.path.join(folder_path, "**/*.jpg"), recursive=True)

    for file_path in image_files:
        time+=1
        print("detecting "+str(time)+"th images in lfw")
        try:
            img=cv2.imread(file_path)
            DeepFace.extract_faces(img)
        except Exception:
            count+=1
    precise=(len(image_files)-count)/len(image_files)
    print(precise)
    return precise


if __name__=="__main__":

    precision_lfw = LFW_dataset()
    precision_ass4 = ass4_dataset()
    precision_vgg=vgg_examples()

    categories = ['ass4', 'vgg', 'LFW']
    values = [precision_ass4,precision_vgg,precision_lfw]

    ax = sns.barplot(x=categories, y=values)
    ax.set_title("precision based on different dataset")
    ax.set_ylabel("precision")
    ax.set_xlabel("dataset")

    # 在每个条形上显示数值标签
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.3f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                    va='center', xytext=(0, 10), textcoords='offset points')

    # 显示图形
    plt.savefig("precision.png")
    plt.show()


