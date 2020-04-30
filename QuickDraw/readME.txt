G32 Pictionary ReadME

Compilation 
Following packages are required:
numpy
matplotlib
Cv2 ( you can use "pip install opencv-python" to install)
keras
tensorflow
pandas
h5py
scipy
Pygame


Dataset

https://github.com/googlecreativelab/quickdraw-dataset
Labels
0) Apple
1) Bowtie
2) Door
3) Envelope
4) Fish
5) Ice Cream
6) Lightning
7) Mountain
8) Star
9) Toothbrush


Please download the dataset into ./data folder

# that's the address of the open source
https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap

# that's the download link to the npy files please download the ten labels of item.
https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap

#LoadData.py - ZHANG ZI CUHAN
This is the program for loading the dataset from the ./data and generate pickle files
If you want to run it , please provide the data first.

#QD_trainer - PAN FNEG
This is the training program to train the model. If you want to run it, it is necessary that both labels and features pickle files are exist (Both of them are in the submission) but after run it , it will recover the QuickDraw.h5 that the model will be changed, so please do the backup first.

#QuickSketch.py - XIE CHU YANG & WU ZE ZHEN & PAN FENG
This is the implementation of sketching board and assemble the UI and ML. To run this program, the *.h5 file and the images in qd_emo are required. 