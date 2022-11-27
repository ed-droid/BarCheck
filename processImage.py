from sys import argv
import easyocr
import re
import cv2
import numpy as np

script, first = argv

print ("Этот скрипт называется: ", script)
print ("Значение первой переменной: ", first)
# print ("Значение второй переменной: ", second)
# print ("Значение третьей переменной: ", third)