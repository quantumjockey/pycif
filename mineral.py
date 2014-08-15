# Description: Representation of International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) mineral data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies


# script body for file processing
class Mineral:
	def __init__(self):
		self.author_name = []

		self.journal_name = ""
		self.journal_volume = ""
		self.journal_year = 0
		self.journal_page_first = 0
		self.journal_page_last = 0
		self.journal_section_title = ""

		self.amcsd_database_code = 0

		self.chemical_name = ""
		self.chemical_formula_sum = ""

		self.cell_length_a = 0.0
		self.cell_length_b = 0.0
		self.cell_length_c = 0.0

		self.cell_angle_alpha = 0
		self.cell_angle_beta = 0
		self.cell_angle_gamma = 0
		self.cell_volume = 0.0

		self.exptl_crystal_density_diffrn = 0.0

		self.symmetry_space_group_name_H_M = ""

		self.space_group_symop_operation_xyz = []

		self.atom_sites = []

		self.atom_sites_aniso = []
