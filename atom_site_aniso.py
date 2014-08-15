# Description: Representation of International Union of Crystallography (IUCr) Crystallographic Information Format (CIF) atomic site anisotropic data.
# Developer: Nicola B. DiPalma
# Scripted using Python v3.4.1
# For use with Python v3.x

# Dependencies


# Expected types
# - label :: String
# - U_11 :: Float
# - U_22 :: Float
# - U_33 :: Float
# - U_12 :: Float
# - U_13 :: Float
# - U_23 :: Float

# object body
class AtomSiteAnisotropic:
	def __init__(self, label, U_11, U_22, U_33, U_12, U_13, U_23):
		self.label = label

		self.U_11 = U_11
		self.U_22 = U_22
		self.U_33 = U_33
		self.U_12 = U_12
		self.U_13 = U_13
		self.U_23 = U_23
