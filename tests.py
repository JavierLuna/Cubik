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