# Description: Allows user to convert International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) files to JSON for use with external modules.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import sys


# script body for file processing
def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='File to be parsed.')
	parser.add_argument("-r", "--raw", help="Prints raw file data (unformatted) before processing.", action="store_true")
	parser.add_argument("-rf", "--rawFormatted", help="Prints raw file data (formatted) before processing.", action="store_true")

	args = parser.parse_args()

	fileData = args.infile
	sourceFile = fileData.name

	rawFileContent = GetRawData(fileData)
	if args.raw:
		PrintRawData(rawFileContent, False)
	if args.rawFormatted:
		PrintRawData(rawFileContent, True)


# Parse the text file data
def ProcessTextFile(sourceFile):
	fileContent = []


# Reads raw file data and retrieves each line in string format
def GetRawData(fileStream):
	fileContent = []
	for line in fileStream:
		filteredLine = line.strip()
		if filteredLine != "":
			fileContent.append(filteredLine)
	return fileContent


# Prints raw file data obtained from a string array
def PrintRawData(rawDataArray, shouldFormat):
	print("Raw file data:")
	if shouldFormat:
		print("------------------------------------------")
		for data in rawDataArray:
			print(data)
		print("------------------------------------------")
	else:
		print(rawDataArray)


# Call main function
if __name__ == "__main__":
	main()
