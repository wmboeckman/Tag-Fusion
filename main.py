import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

TRAIN_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.realpath('/training_data/'))
TAG_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.realpath('tags.txt'))


def main():
    # load tag list :)
    with open(TAG_FILE_PATH) as txt_file:
        i = 1
        for line in txt_file:
            print(line.strip('\n'), end=', ' if i % 2 else ',\n')
            i += 1


if __name__ == '__main__':
    main()
