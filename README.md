# cv-final-project

## Introduction

This is a Final project of 2023 spring CS308(Computer Vision) course. It includes a GUI implement of [`Deepface`](https://github.com/serengil/deepface)(a lightweight face recognition and facial attribute analysis framework) and some experiments of [`Deepface`](https://github.com/serengil/deepface).

The GUI program has implemented some main features of [`Deepface`](https://github.com/serengil/deepface) such as `Face detect`, `Face attribute`, `Face matching` and `Face verification`.

The detail of experiments can be found in our project [`report`](https://github.com/Fae42/cv-final-project/blob/main/CV_Final_report.pdf).

## Set up

You can run the following command to import the required environment by `conda`:

```shell
conda env create -f environment.yml
```

_Note: some of the pip dependencies might not be a must. You can try to ignore some warnings or errors while importing them._


After importing the environment, you can run `main.py` in the environment to enter the main page.

## Usage

Let's take `Face attribute` as an example to show the usage of GUI program.

Here's the main page which you would see after running `main.py`. You can click the "Face attribute(image)" bottom in the middle to enter the `Face attribute` page.
![](https://github.com/Fae42/cv-final-project/blob/main/pics/main%20page.png?raw=true)

This is the `Face attribute` page.
![](https://github.com/Fae42/cv-final-project/blob/main/pics/attribute1.png?raw=true)

Click `Select picture/video` and choose picture or video you want to test attribute with. Here's the example image.
![](https://github.com/Fae42/cv-final-project/blob/main/pics/attribute2.png?raw=true)

After choosing a picture or video, click the `Start` bottom. The result will display on the right.
![](https://github.com/Fae42/cv-final-project/blob/main/pics/attribute3.png?raw=true)

Other functions have similar usage.

_Note: this program needs some pre-train weight files to run. These files are large (~500 MB each) and require some time to download, which depends on your network state._