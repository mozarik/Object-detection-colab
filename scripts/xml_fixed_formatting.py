# Iterate through test and main folder
# Search for *.XML file
# Get that *.XML file name example "image01.xml" would be "image01"

import glob
import xml.etree.ElementTree as ET
import os

PATH = "./Tensorflow/workspace/images/**"


def format_csv_filename(path):
    for xml_file in glob.glob(path + '/*.xml', recursive=True):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        new_filename = xml_file.split(os.sep)[-1]
        new_filename = new_filename[:-4] + ".jpg"
        for filename in root.iter('filename'):
            # update the filename
            filename.text = str(new_filename)
        tree.write(xml_file)


if __name__ == '__main__':
    format_csv_filename(PATH)
