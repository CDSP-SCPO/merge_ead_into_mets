# !/usr/bin/env python
# -*- coding: utf8 -*-
# Execution example : python merge_ead_into_mets.py /path/to/file/ead.xml /path/to/file/mets.xml

#
# Libs
#

from lxml import etree
import os
import sys


#
# Config
#

result_file = 'merge_ead_into_mets.xml'
METS_URL = 'http://www.loc.gov/METS/'
NSMAP = {'mets' : METS_URL}
METS_PREFIX = '{' + METS_URL + '}'


#
# Functions
#

def merge(ead_file, mets_file) :
	# Open EAD file
	ead_tree = etree.parse(ead_file).getroot()
	# Open METS file
	mets_tree = etree.parse(mets_file).getroot()
	# Create a new node that will receive the EAD data
	dmdSec = etree.Element(METS_PREFIX + 'dmdSec', ID='ead', GROUPID='ead', nsmap=NSMAP)
	mdWrap = etree.SubElement(dmdSec, METS_PREFIX + 'mdWrap', {'MDTYPE' : 'EAD'})
	xmlData = etree.SubElement(mdWrap, METS_PREFIX + 'xmlData')
	# Include the EAD data into this node
	xmlData.insert(0, ead_tree)
	# Add the EAD node to the root node of the mets file as second child
	mets_tree.insert(1, dmdSec)
	# Write result into file
	result_tree = etree.ElementTree(mets_tree)
	result_tree.write(result_file, encoding='UTF-8', pretty_print=True, xml_declaration=True)


def main() :
	# Check that all args are here
	if len(sys.argv) != 3 :
		print "Check the number of arguments"
		exit()
	ead_file = sys.argv[1]
	mets_file = sys.argv[2]
	# Check that files exist
	if not os.path.isfile(ead_file) :
		print "EAD is not a file"
		exit()
	if not os.path.isfile(ead_file) :
		print "METS is not a file"
		exit()
	# Check that files are xml
	if not ead_file.lower().endswith('.xml') :
		print "EAD is not an XML file"
		exit()
	if not mets_file.lower().endswith('.xml') :
		print "METS is not an XML file"
		exit()
	merge(ead_file, mets_file)
	print 'Results writed into : ' + result_file
	print 'End script'

#
# Main
#

if __name__ == '__main__':
	main()