"""
    Implemented by Aidar Ahmetshin BS17-RO-01
"""

import glob
import matplotlib.pyplot as plt
import numpy as np


# function to plot histogram (amount distribution for each byte)
def plot_hist(arr, file, entropy):
    plt.style.use('ggplot')
    plt.title(str("Histogram of bytes distribution in file {0} with entropy {1}".format(file, entropy)))
    plt.xlabel("Byte")
    plt.ylabel("Amount of byte")
    plot = plt.gca()
    plot.bar(range(len(arr)), arr)
    plt.show()


# input: byte array of the file and amount of bytes in this file
# output: the score of entropy for the file
def calculate_entropy(arr, bytes_count):
    # array with probability of each byte
    probability_bytes = [0 for _ in range(256)]
    # additional array for calculating entropy
    entropy_byte_list = [0 for _ in range(256)]

    # calculate probability for each byte
    for i in range(len(arr)):
        probability_bytes[i] = arr[i] / bytes_count

    # calculate entropy for the file
    for i in range(len(probability_bytes)):
        if probability_bytes[i] != 0:
            entropy_byte_list[i] = probability_bytes[i] * np.log2(probability_bytes[i])

    # print("Amount of bytes in file: {0}".format(bytes_count))

    # the final score for entropy for the file
    entropy = sum(entropy_byte_list) * (-1)

    # print("Entropy of this file: {0}".format(entropy))
    return entropy


# file processing function, input: list of files for calculating entropy
def files_reading(list_files):
    # array with entropies for corresponded group of files
    entropy_group = []
    for f in list_files:
        arr = [0 for _ in range(256)]
        file = open(f, 'rb').read()
        # count amount of repetitions of bytes
        for i in file:
            arr[i] += 1

        # the whole amount of bytes in one file
        byte_count = sum(arr)
        entropy_group.append(calculate_entropy(arr, byte_count))
        # you can plot for each file its plot (distribution) and see how bytes distributed in corresponded file
        # plot_hist(arr, f, calculate_entropy(arr, byte_count))

    print("Min entropy: {0}".format(min(entropy_group)))
    print("Max entropy: {0}".format(max(entropy_group)))
    print("Avg entropy: {0}".format(sum(entropy_group) / len(entropy_group)))


# main method
if __name__ == '__main__':
    # read files from directory
    doc_list = glob.glob("dataset/doc/*")
    print("Amount of files on this directory: {0}".format(len(doc_list)))
    print("DOC: ")
    # print result for 1) min score 2) max score 3) average score of entropy for corresponded group of files
    files_reading(doc_list)
    # ----------------------------------------
    exe_list = glob.glob("dataset/exe/*")
    print("Amount of files on this directory: {0}".format(len(exe_list)))
    print("EXE: ")
    files_reading(exe_list)
    # ----------------------------------------
    jpg_list = glob.glob("dataset/jpg/*")
    print("Amount of files on this directory: {0}".format(len(jpg_list)))
    print("JPG: ")
    files_reading(jpg_list)
    # ----------------------------------------
    pdf_list = glob.glob("dataset/pdf/*")
    print("Amount of files on this directory: {0}".format(len(pdf_list)))
    print("PDF: ")
    files_reading(pdf_list)
    # ----------------------------------------
    png_list = glob.glob("dataset/png/*")
    print("Amount of files on this directory: {0}".format(len(png_list)))
    print("PNG: ")
    files_reading(png_list)

    # Also you can add zip dir in dataset directory with zip files and see what entropy the have
    '''zip_list = glob.glob("dataset/zip/*")
    print(len(zip_list))
    print("ZIP: ")
    files_reading(zip_list)'''
