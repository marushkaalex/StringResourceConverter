import argparse
import xml.etree.ElementTree as ET

def process(xmlfilename, outfilename):
	tree = ET.parse(xmlfilename)
	root = tree.getroot()

	fout = open(outfilename, 'w', encoding='utf-8')
	for child in root:
		if (child.tag == 'string'):
			fout.write('"' + child.attrib['name'] + '" = "' + child.text + '";\n')
	fout.close()

def main():
	parser = argparse.ArgumentParser(description='Android XML string resouces to IOS string resources converter')
	parser.add_argument('-i', '--input', help='path to input file', default='strings.xml')
	parser.add_argument('-o', '--output', help='path to output file', default='Localizable.strings')

	args = parser.parse_args()
	process(args.input, args.output)

main()