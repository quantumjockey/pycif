# Description: Allows user to convert International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) files to JSON for use with external modules.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse


# script body for file processing
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	args = parser.parse_args()

	fileData = args.infile
	sourceFile = fileData.name


# Parse the text file data
def ProcessTextFile(sourceFile, targetFileDirectory, extension):
	lineOfData = []

	for line in sourceFile:
		lineOfData = line.split()


# Call main function
if __name__ == "__main__":
	main()
