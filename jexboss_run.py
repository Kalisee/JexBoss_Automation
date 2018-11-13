import os
import sys

user = input("Enter file name: ")
os.system('python jexboss.py -mode file-scan -file ' + user + ' -out report_file_scan.log')