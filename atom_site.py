# Description: Representation of International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) atomic site data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies


# Expected types
# - label :: String
# - fract_x :: Float
# - fract_y :: Float
# - fract_z :: Float
# - occupancy :: Float

# script body for file processing
class AtomSite:
	def __init__(self, label, fract_x, fract_y, fract_z, occupancy):
		self.label = label

		self.fract_x = fract_x
		self.fract_y = fract_y
		self.fract_z = fract_z
		self.occupancy = occupancy
