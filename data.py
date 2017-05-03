# coding=utf-8
import os

from file_helper import read_lines

caltch_path = '/Users/cwh/Mission/scut/lesson/PR/project/PR_dataset/'
caltech_train_path = caltch_path + 'train/'
caltech_test_path = caltch_path + 'test/'
caltech_train_pos_path = caltech_train_path + 'pos/'
caltech_train_neg_path = caltech_train_path + 'neg/'
caltech_test_pos_path = caltech_test_path + 'pos/'
caltech_test_neg_path = caltech_test_path + 'neg/'


def read_caltech():
    pos_train_features = list()
    pos_train_labels = list()
    neg_train_features = list()
    neg_train_labels = list()
    pos_test_features = list()
    pos_test_labels = list()
    neg_test_features = list()
    neg_test_labels = list()
    for files in os.listdir(caltech_train_pos_path):
        path = os.path.join(caltech_train_pos_path, files)
        features = read_lines(path)
        print(path)
        pos_train_features.append(features)
        pos_train_labels.append(1)
    for files in os.listdir(caltech_train_neg_path):
        path = os.path.join(caltech_train_neg_path, files)
        print(path)
        features = read_lines(path)
        neg_train_features.append(features)
        neg_train_labels.append(0)
    for files in os.listdir(caltech_test_neg_path):
        path = os.path.join(caltech_test_neg_path, files)
        print(path)
        features = read_lines(path)
        pos_test_features.append(features)
        pos_test_labels.append(1)
    for files in os.listdir(caltech_test_neg_path):
        path = os.path.join(caltech_test_neg_path, files)
        print(path)
        features = read_lines(path)
        neg_test_features.append(features)
        neg_test_labels.append(0)


if __name__ == '__main__':
    read_caltech()