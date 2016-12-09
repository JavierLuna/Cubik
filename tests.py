import unittest

from Cubik import RubikCube


class TestRubikCube(unittest.TestCase):

	def test_RU_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.R()
			cube.U()
			cube.R1()
			cube.U1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_LU_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.L()
			cube.U()
			cube.L1()
			cube.U1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_RD_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.R()
			cube.D()
			cube.R1()
			cube.D1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_LD_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.L()
			cube.D()
			cube.L1()
			cube.D1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_RF_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.R()
			cube.F()
			cube.R1()
			cube.F1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_LF_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.L()
			cube.F()
			cube.L1()
			cube.F1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_RULD_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(3):
			cube.R()
			cube.U()
			cube.R1()
			cube.U1()
		for _ in range(3):
			cube.L()
			cube.D()
			cube.L1()
			cube.D1()
		for _ in range(3):
			cube.R()
			cube.U()
			cube.R1()
			cube.U1()
		for _ in range(3):
			cube.L()
			cube.D()
			cube.L1()
			cube.D1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_DB_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.B()
			cube.D()
			cube.B1()
			cube.D1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_MU_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(5):
			cube.U()
			cube.M()
			cube.U1()
			cube.M1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)

	def test_SU_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(5):
			cube.U()
			cube.S()
			cube.U1()
			cube.S1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)