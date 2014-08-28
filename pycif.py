# Description: Allows user to convert International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) files to JSON for use with external modules.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies
import argparse
import sys

from mineral import Mineral


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

	ProcessFile(rawFileContent)


# Parse the text file data
def ProcessFile(rawContent):
	filteredContent = []
	for line in rawContent:
		if " " in line:
			filteredContent.append(line.split())
		else:
			filteredContent.append(line)
	mineralData = Mineral()

	# Get chemical properties
	for data in filteredContent:
		if (data[0] == "_chemical_name_mineral"):
			mineralData.chemical_name = data[1]
		elif (data[0] == "_chemical_formula_sum"):
			mineralData.chemical_formula_sum = data[1]

	# Get journal params
	for data in filteredContent:
		if (data[0] == "_journal_name_full"):
			mineralData.journal_name = data[1]
		elif (data[0] == "_journal_volume"):
			mineralData.journal_volume = data[1]
		elif (data[0] == "_journal_year"):
			mineralData.journal_year = data[1]
		elif (data[0] == "_journal_page_first"):
			mineralData.journal_page_first = data[1]
		elif (data[0] == "_journal_page_last"):
			mineralData.journal_page_last = data[1]
		elif (data[0] == "_publ_section_title"):
			mineralData.journal_section_title = data[1]

	# Get database code
	for data in filteredContent:
		if (data[0] == "_database_code_amcsd"):
			mineralData.amcsd_database_code = data[1]

	# Get unit cell params
	for data in filteredContent:
		if (data[0] == "_cell_length_a"):
			mineralData.cell_length_a = data[1]
		elif (data[0] == "_cell_length_b"):
			mineralData.cell_length_b = data[1]
		elif (data[0] == "_cell_length_c"):
			mineralData.cell_length_c = data[1]
		elif (data[0] == "_cell_angle_alpha"):
			mineralData.cell_angle_alpha = data[1]
		elif (data[0] == "_cell_angle_beta"):
			mineralData.cell_angle_beta = data[1]
		elif (data[0] == "_cell_angle_gamma"):
			mineralData.cell_angle_gamma = data[1]

	# Get crystal density diffraction
	for data in filteredContent:
		if (data[0] == "_exptl_crystal_density_diffrn"):
			mineralData.exptl_crystal_density_diffrn = data[1]


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
