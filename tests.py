import unittest

from Cubik import RubikCube


class TestRubikCube(unittest.TestCase):

	def test_U_fingertrick(self):
		cube = RubikCube()
		first_state = cube.json
		for _ in range(6):
			cube.R()
			cube.U()
			cube.R1()
			cube.U1()
		last_state = cube.json
		self.assertEqual(first_state, last_state)