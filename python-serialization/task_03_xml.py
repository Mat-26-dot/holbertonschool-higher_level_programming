#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data") #create root - data
    for key, value in dictionary.items(): #loop through dictionary items
        child = ET.SubElement(root, key) #create sub-ele with key as tag
        child.text = str(value) # set text to string of rep value
    tree = ET.ElementTree(root)#build xml tree and write to file
    tree.write(filename)

def deserialize_from_xml(filename):#parse the xml file
    tree = ET.parse(filename) #uses ET.parse to read the file
    root = tree.getroot() #gets thr root element (<data> in this case)
    result_dict = {} # reconstruct the dictionary
    for child in root: #iterate through elements like <name, <age>
        result_dict[child.tag] = child.text #Tag becomes key, text becomes value
    
    return result_dict