import copy
import json
import random

import time


class RubikCube:
	SOLVED = [[num for _ in range(9)] for num in range(1, 7)]
	DEBUG = [
		['a0', 'a1', 'a2',
		 'a3', 'a4', 'a5',
		 'a6', 'a7', 'a8']
		,
		['b0', 'b1', 'b2',
		 'b3', 'b4', 'b5',
		 'b6', 'b7', 'b8']
		,
		['c0', 'c1', 'c2',
		 'c3', 'c4', 'c5',
		 'c6', 'c7', 'c8']
		,
		['d0', 'd1', 'd2',
		 'd3', 'd4', 'd5',
		 'd6', 'd7', 'd8']
		,
		['e0', 'e1', 'e2',
		 'e3', 'e4', 'e5',
		 'e6', 'e7', 'e8']
		,
		['f0', 'f1', 'f2',
		 'f3', 'f4', 'f5',
		 'f6', 'f7', 'f8']
	]

	POSSIBLE_MOVEMENTS = ['U', 'D', 'R', 'L', 'F', 'B', 'U1', 'D1', 'R1', 'L1', 'F1', 'B1', 'M', 'E', 'S', 'M1', 'E1',
	                      'S1']

	def __init__(self, cube=None):
		"""
		Creates a cube
		:param cube: List of 6 (cube's faces) lists with 9 elements each (cells per face).
					None to generate a random one
		"""
		self.cube = cube or copy.deepcopy(RubikCube.SOLVED)
		if not cube:
			self.generate_random_cube()
		self.initial_cube = copy.deepcopy(self.cube)
		self.movements_applied = []
		self.__functions = {'D': self.D}

	@property
	def solved(self):
		"""
		Returns if the cube has all faces solved
		:return: True if the cube is solved, False if it isn't
		"""
		for face in self.cube:
			color = face[0]
			for cell in face:
				if cell != color:
					return False
		return True

	@property
	def last_movement(self):
		"""
		Returns last movement applied to the cube
		:return: Last movement applied (remember, must be through do_movement() )
		"""
		if self.movements_applied:
			return self.movements_applied[-1]
		else:
			return None

	@property
	def json(self):
		"""
		Returns the cube in a json string
		:return: Cube in a JSON String
		"""
		return json.dumps({'cube': self.cube})

	@staticmethod
	def get_opposite_movement(movement):
		"""
		Returns the opposite movement of a movement. I.E: Given movement U it returns U1
		:param movement: (String) Movement you want the opposite of
		:return: (String) The opposite movement of the provided movement
		"""
		if len(movement) == 1:
			return movement + "1"
		else:
			return movement[0]

	def do_movement(self, movement):
		"""
		Performs the movement and registers the movement into the movements_applied cube's history.
		:param movement: (String) Movement to be done IE: U
		"""
		m = getattr(self, movement)
		if not m or (m and not callable(m)):
			raise KeyError('Invalid movement ' + movement)
		self.movements_applied.append(movement)
		m()

	def undo(self):
		"""
		Reverts last movement by applying the opposite movement
		"""
		if self.movements_applied:
			movement = self.movements_applied.pop()
			opposite_movement = getattr(self, RubikCube.get_opposite_movement(movement))
			opposite_movement()
		else:
			raise IndexError('No movements were made in the first place')

	def R(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		e0, e1, e2, e3, e4, e5, e6, e7, e8 = face5

		a2, a5, a8 = face1[2], face1[5], face1[8]
		b2, b5, b8 = face2[2], face2[5], face2[8]
		d2, d5, d8 = face4[2], face4[5], face4[8]
		f2, f5, f8 = face6[2], face6[5], face6[8]

		self.cube[0][2], self.cube[0][5], self.cube[0][8] = b2, b5, b8
		self.cube[1][2], self.cube[1][5], self.cube[1][8] = d2, d5, d8
		self.cube[3][2], self.cube[3][5], self.cube[3][8] = f2, f5, f8
		self.cube[5][2], self.cube[5][5], self.cube[5][8] = a2, a5, a8

		self.cube[4][0], self.cube[4][1], self.cube[4][2] = e6, e3, e0
		self.cube[4][3], self.cube[4][4], self.cube[4][5] = e7, e4, e1
		self.cube[4][6], self.cube[4][7], self.cube[4][8] = e8, e5, e2

	def R1(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		e0, e1, e2, e3, e4, e5, e6, e7, e8 = face5

		a2, a5, a8 = face1[2], face1[5], face1[8]
		b2, b5, b8 = face2[2], face2[5], face2[8]
		d2, d5, d8 = face4[2], face4[5], face4[8]
		f2, f5, f8 = face6[2], face6[5], face6[8]

		self.cube[0][2], self.cube[0][5], self.cube[0][8] = f2, f5, f8
		self.cube[1][2], self.cube[1][5], self.cube[1][8] = a2, a5, a8
		self.cube[3][2], self.cube[3][5], self.cube[3][8] = b2, b5, b8
		self.cube[5][2], self.cube[5][5], self.cube[5][8] = d2, d5, d8

		self.cube[4][0], self.cube[4][1], self.cube[4][2] = e2, e5, e8
		self.cube[4][3], self.cube[4][4], self.cube[4][5] = e1, e4, e7
		self.cube[4][6], self.cube[4][7], self.cube[4][8] = e0, e3, e6

	def L(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		c0, c1, c2, c3, c4, c5, c6, c7, c8 = face3

		a0, a3, a6 = face1[0], face1[3], face1[6]
		b0, b3, b6 = face2[0], face2[3], face2[6]
		d0, d3, d6 = face4[0], face4[3], face4[6]
		f0, f3, f6 = face6[0], face6[3], face6[6]

		self.cube[0][0], self.cube[0][3], self.cube[0][6] = f0, f3, f6
		self.cube[1][0], self.cube[1][3], self.cube[1][6] = a0, a3, a6
		self.cube[3][0], self.cube[3][3], self.cube[3][6] = b0, b3, b6
		self.cube[5][0], self.cube[5][3], self.cube[5][6] = d0, d3, d6

		self.cube[2][0], self.cube[2][1], self.cube[2][2] = c6, c3, c0
		self.cube[2][3], self.cube[2][4], self.cube[2][5] = c7, c4, c1
		self.cube[2][6], self.cube[2][7], self.cube[2][8] = c8, c5, c2

	def L1(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		c0, c1, c2, c3, c4, c5, c6, c7, c8 = face3

		a0, a3, a6 = face1[0], face1[3], face1[6]
		b0, b3, b6 = face2[0], face2[3], face2[6]
		d0, d3, d6 = face4[0], face4[3], face4[6]
		f0, f3, f6 = face6[0], face6[3], face6[6]

		self.cube[0][0], self.cube[0][3], self.cube[0][6] = b0, b3, b6
		self.cube[1][0], self.cube[1][3], self.cube[1][6] = d0, d3, d6
		self.cube[3][0], self.cube[3][3], self.cube[3][6] = f0, f3, f6
		self.cube[5][0], self.cube[5][3], self.cube[5][6] = a0, a3, a6

		self.cube[2][0], self.cube[2][1], self.cube[2][2] = c2, c5, c8
		self.cube[2][3], self.cube[2][4], self.cube[2][5] = c1, c4, c7
		self.cube[2][6], self.cube[2][7], self.cube[2][8] = c0, c3, c6

	def U(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		b0, b1, b2, b3, b4, b5, b6, b7, b8 = face2

		a6, a7, a8 = face1[6], face1[7], face1[8]
		c0, c1, c2 = face3[0], face3[1], face3[2]
		d0, d1, d2 = face4[0], face4[1], face4[2]
		e0, e1, e2 = face5[0], face5[1], face5[2]

		self.cube[0][6], self.cube[0][7], self.cube[0][8] = c2, c1, c0
		self.cube[2][0], self.cube[2][1], self.cube[2][2] = d0, d1, d2
		self.cube[3][0], self.cube[3][1], self.cube[3][2] = e0, e1, e2
		self.cube[4][0], self.cube[4][1], self.cube[4][2] = a8, a7, a6

		self.cube[1][0], self.cube[1][1], self.cube[1][2] = b6, b3, b0
		self.cube[1][3], self.cube[1][4], self.cube[1][5] = b7, b4, b1
		self.cube[1][6], self.cube[1][7], self.cube[1][8] = b8, b5, b2

	def U1(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		b0, b1, b2, b3, b4, b5, b6, b7, b8 = face2

		a6, a7, a8 = face1[6], face1[7], face1[8]
		c0, c1, c2 = face3[0], face3[1], face3[2]
		d0, d1, d2 = face4[0], face4[1], face4[2]
		e0, e1, e2 = face5[0], face5[1], face5[2]

		self.cube[0][6], self.cube[0][7], self.cube[0][8] = e2, e1, e0
		self.cube[2][0], self.cube[2][1], self.cube[2][2] = a8, a7, a6
		self.cube[3][0], self.cube[3][1], self.cube[3][2] = c0, c1, c2
		self.cube[4][0], self.cube[4][1], self.cube[4][2] = d0, d1, d2

		self.cube[1][0], self.cube[1][1], self.cube[1][2] = b2, b5, b8
		self.cube[1][3], self.cube[1][4], self.cube[1][5] = b1, b4, b7
		self.cube[1][6], self.cube[1][7], self.cube[1][8] = b0, b3, b6

	def D(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		f0, f1, f2, f3, f4, f5, f6, f7, f8 = face6

		a0, a1, a2 = face1[0], face1[1], face1[2]
		c6, c7, c8 = face3[6], face3[7], face3[8]
		d6, d7, d8 = face4[6], face4[7], face4[8]
		e6, e7, e8 = face5[6], face5[7], face5[8]

		self.cube[0][0], self.cube[0][1], self.cube[0][2] = e8, e7, e6
		self.cube[2][6], self.cube[2][7], self.cube[2][8] = a2, a1, a0
		self.cube[3][6], self.cube[3][7], self.cube[3][8] = c6, c7, c8
		self.cube[4][6], self.cube[4][7], self.cube[4][8] = d6, d7, d8

		self.cube[5][0], self.cube[5][1], self.cube[5][2] = f6, f3, f0
		self.cube[5][3], self.cube[5][4], self.cube[5][5] = f7, f4, f1
		self.cube[5][6], self.cube[5][7], self.cube[5][8] = f8, f5, f2

	def D1(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		f0, f1, f2, f3, f4, f5, f6, f7, f8 = face6

		a0, a1, a2 = face1[0], face1[1], face1[2]
		c6, c7, c8 = face3[6], face3[7], face3[8]
		d6, d7, d8 = face4[6], face4[7], face4[8]
		e6, e7, e8 = face5[6], face5[7], face5[8]

		self.cube[0][0], self.cube[0][1], self.cube[0][2] = c8, c7, c6
		self.cube[2][6], self.cube[2][7], self.cube[2][8] = d6, d7, d8
		self.cube[3][6], self.cube[3][7], self.cube[3][8] = e6, e7, e8
		self.cube[4][6], self.cube[4][7], self.cube[4][8] = a2, a1, a0

		self.cube[5][0], self.cube[5][1], self.cube[5][2] = f2, f5, f8
		self.cube[5][3], self.cube[5][4], self.cube[5][5] = f1, f4, f7
		self.cube[5][6], self.cube[5][7], self.cube[5][8] = f0, f3, f6

	def F(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		d0, d1, d2, d3, d4, d5, d6, d7, d8 = face4

		b6, b7, b8 = face2[6], face2[7], face2[8]
		c2, c5, c8 = face3[2], face3[5], face3[8]
		e0, e3, e6 = face5[0], face5[3], face5[6]
		f0, f1, f2 = face6[0], face6[1], face6[2]

		self.cube[1][6], self.cube[1][7], self.cube[1][8] = c8, c5, c2
		self.cube[2][2], self.cube[2][5], self.cube[2][8] = f0, f1, f2
		self.cube[4][0], self.cube[4][3], self.cube[4][6] = b6, b7, b8
		self.cube[5][0], self.cube[5][1], self.cube[5][2] = e6, e3, e0

		self.cube[3][0], self.cube[3][1], self.cube[3][2] = d6, d3, d0
		self.cube[3][3], self.cube[3][4], self.cube[3][5] = d7, d4, d1
		self.cube[3][6], self.cube[3][7], self.cube[3][8] = d8, d5, d2

	def F1(self):

		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		d0, d1, d2, d3, d4, d5, d6, d7, d8 = face4

		b6, b7, b8 = face2[6], face2[7], face2[8]
		c2, c5, c8 = face3[2], face3[5], face3[8]
		e0, e3, e6 = face5[0], face5[3], face5[6]
		f0, f1, f2 = face6[0], face6[1], face6[2]

		self.cube[1][6], self.cube[1][7], self.cube[1][8] = e0, e3, e6
		self.cube[2][2], self.cube[2][5], self.cube[2][8] = b8, b7, b6
		self.cube[4][0], self.cube[4][3], self.cube[4][6] = f2, f1, f0
		self.cube[5][0], self.cube[5][1], self.cube[5][2] = c2, c5, c8

		self.cube[3][0], self.cube[3][1], self.cube[3][2] = d2, d5, d8
		self.cube[3][3], self.cube[3][4], self.cube[3][5] = d1, d4, d7
		self.cube[3][6], self.cube[3][7], self.cube[3][8] = d0, d3, d6

	def B(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)

		b0, b1, b2 = face2[0], face2[1], face2[2]
		c0, c3, c6 = face3[0], face3[3], face3[6]
		e2, e5, e8 = face5[2], face5[5], face5[8]
		f6, f7, f8 = face6[6], face6[7], face6[8]

		a0, a1, a2, a3, a4, a5, a6, a7, a8 = face1

		self.cube[1][0], self.cube[1][1], self.cube[1][2] = e2, e5, e8
		self.cube[2][0], self.cube[2][3], self.cube[2][6] = b2, b1, b0
		self.cube[4][2], self.cube[4][5], self.cube[4][8] = f8, f7, f6
		self.cube[5][6], self.cube[5][7], self.cube[5][8] = c0, c3, c6

		self.cube[0][0], self.cube[0][1], self.cube[0][2] = a6, a3, a0
		self.cube[0][3], self.cube[0][4], self.cube[0][5] = a7, a4, a1
		self.cube[0][6], self.cube[0][7], self.cube[0][8] = a8, a5, a2

	def B1(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		b0, b1, b2 = face2[0], face2[1], face2[2]
		c0, c3, c6 = face3[0], face3[3], face3[6]
		e2, e5, e8 = face5[2], face5[5], face5[8]
		f6, f7, f8 = face6[6], face6[7], face6[8]

		a0, a1, a2, a3, a4, a5, a6, a7, a8 = face1

		self.cube[1][0], self.cube[1][1], self.cube[1][2] = c6, c3, c0
		self.cube[2][0], self.cube[2][3], self.cube[2][6] = f6, f7, f8
		self.cube[4][2], self.cube[4][5], self.cube[4][8] = b0, b1, b2
		self.cube[5][6], self.cube[5][7], self.cube[5][8] = e8, e5, e2

		self.cube[0][0], self.cube[0][1], self.cube[0][2] = a2, a5, a8
		self.cube[0][3], self.cube[0][4], self.cube[0][5] = a1, a4, a7
		self.cube[0][6], self.cube[0][7], self.cube[0][8] = a0, a3, a6

	def M(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		a1, a4, a7 = face1[1], face1[4], face1[7]
		b1, b4, b7 = face2[1], face2[4], face2[7]
		d1, d4, d7 = face4[1], face4[4], face4[7]
		f1, f4, f7 = face6[1], face6[4], face6[7]

		self.cube[0][1], self.cube[0][4], self.cube[0][7] = f1, f4, f7
		self.cube[1][1], self.cube[1][4], self.cube[1][7] = a1, a4, a7
		self.cube[3][1], self.cube[3][4], self.cube[3][7] = b1, b4, b7
		self.cube[5][1], self.cube[5][4], self.cube[5][7] = d1, d4, d7

	def M1(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		a1, a4, a7 = face1[1], face1[4], face1[7]
		b1, b4, b7 = face2[1], face2[4], face2[7]
		d1, d4, d7 = face4[1], face4[4], face4[7]
		f1, f4, f7 = face6[1], face6[4], face6[7]

		self.cube[0][1], self.cube[0][4], self.cube[0][7] = b1, b4, b7
		self.cube[1][1], self.cube[1][4], self.cube[1][7] = d1, d4, d7
		self.cube[3][1], self.cube[3][4], self.cube[3][7] = f1, f4, f7
		self.cube[5][1], self.cube[5][4], self.cube[5][7] = a1, a4, a7

	def E(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)

		a3, a4, a5 = face1[3], face1[4], face1[5]
		c3, c4, c5 = face3[3], face3[4], face3[5]
		d3, d4, d5 = face4[3], face4[4], face4[5]
		e3, e4, e5 = face5[3], face5[4], face5[5]

		self.cube[0][3], self.cube[0][4], self.cube[0][5] = e5, e4, e3
		self.cube[2][3], self.cube[2][4], self.cube[2][5] = a5, a4, a3
		self.cube[3][3], self.cube[3][4], self.cube[3][5] = c3, c4, c5
		self.cube[4][3], self.cube[4][4], self.cube[4][5] = d3, d4, d5

	def E1(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)

		a3, a4, a5 = face1[3], face1[4], face1[5]
		c3, c4, c5 = face3[3], face3[4], face3[5]
		d3, d4, d5 = face4[3], face4[4], face4[5]
		e3, e4, e5 = face5[3], face5[4], face5[5]

		self.cube[0][3], self.cube[0][4], self.cube[0][5] = c5, c4, c3
		self.cube[2][3], self.cube[2][4], self.cube[2][5] = d3, d4, d5
		self.cube[3][3], self.cube[3][4], self.cube[3][5] = e3, e4, e5
		self.cube[4][3], self.cube[4][4], self.cube[4][5] = a5, a4, a3

	def S(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		b3, b4, b5 = face2[3], face2[4], face2[5]
		c1, c4, c7 = face3[1], face3[4], face3[7]
		e1, e4, e7 = face5[1], face5[4], face5[7]
		f3, f4, f5 = face6[3], face6[4], face6[5]

		self.cube[1][3], self.cube[1][4], self.cube[1][5] = c7, c4, c1
		self.cube[2][1], self.cube[2][4], self.cube[2][7] = f3, f4, f5
		self.cube[4][1], self.cube[4][4], self.cube[4][7] = b3, b4, b5
		self.cube[5][3], self.cube[5][4], self.cube[5][5] = e7, e4, e1

	def S1(self):
		face1, face2, face3, face4, face5, face6 = copy.deepcopy(self.cube)
		b3, b4, b5 = face2[3], face2[4], face2[5]
		c1, c4, c7 = face3[1], face3[4], face3[7]
		e1, e4, e7 = face5[1], face5[4], face5[7]
		f3, f4, f5 = face6[3], face6[4], face6[5]

		self.cube[1][3], self.cube[1][4], self.cube[1][5] = e1, e4, e7
		self.cube[2][1], self.cube[2][4], self.cube[2][7] = b5, b4, b3
		self.cube[4][1], self.cube[4][4], self.cube[4][7] = f5, f4, f3
		self.cube[5][3], self.cube[5][4], self.cube[5][5] = c1, c4, c7

	def check(self, debug=False):  # Use only with numeric cube
		cells = {a: 0 for a in range(1, 7)}
		for face in self.cube:
			for cell in face:
				cells[cell] += 1

		for cell in cells:
			if cells[cell] != 9:
				if debug:
					print(cells)
					self.display()
				raise Exception('Corrupted rubik cube')

	@staticmethod
	def __get_random_cell(cell_list):
		random.shuffle(cell_list)
		return cell_list.pop()

	def generate_random_cube(self):
		self.cube = copy.deepcopy(RubikCube.SOLVED)
		movements = random.randint(200, 500)
		for _ in range(movements):
			movement = random.choice(RubikCube.POSSIBLE_MOVEMENTS)
			m = getattr(self, movement)
			m()

	def display(self):
		"""
		Displays the cube.
		Face1: Back face
		Face2: Upper face
		Face3: Left face
		Face4: Front face
		Face5: Right face
		Face6: Bottom face
		"""
		face1, face2, face3, face4, face5, face6 = self.cube

		print("     ", "\t", face1[0], face1[1], face1[2], "\t", "      ")
		print("     ", "\t", face1[3], face1[4], face1[5], "\t", "      ")
		print("     ", "\t", face1[6], face1[7], face1[8], "\t", "      ")
		print()
		# Cara 2
		print("     ", "\t", face2[0], face2[1], face2[2], "\t", "      ")
		print("     ", "\t", face2[3], face2[4], face2[5], "\t", "      ")
		print("     ", "\t", face2[6], face2[7], face2[8], "\t", "      ")
		print()
		# Caras 3, 4 y 5
		print(face3[0], face3[1], face3[2], "\t", face4[0], face4[1], face4[2], "\t", face5[0], face5[1], face5[2])
		print(face3[3], face3[4], face3[5], "\t", face4[3], face4[4], face4[5], "\t", face5[3], face5[4], face5[5])
		print(face3[6], face3[7], face3[8], "\t", face4[6], face4[7], face4[8], "\t", face5[6], face5[7], face5[8])
		print()
		# Cara 6
		print("     ", "\t", face6[0], face6[1], face6[2], "\t", "      ")
		print("     ", "\t", face6[3], face6[4], face6[5], "\t", "      ")
		print("     ", "\t", face6[6], face6[7], face6[8], "\t", "      ")


class BacktrackingSolver:

	def __init__(self, cube=None):
		self.cube = cube or RubikCube()
		self.n_movements_done = 0
		self.states = {}
		self.solved_solutions = {}
		self.smallest_solution = 40000
		self.n_solutions = 0

	@property
	def shortest_solution(self):
		if self.solved_solutions:
			shortest_solution = self.solved_solutions[sorted(self.solved_solutions.keys())[0]]
			return {'initial_cube': self.cube.initial_cube, 'solution': shortest_solution.pop()}
		else:
			raise IndexError('No solutions found yet')

	def solve(self, movements_left=20, debug=False):
		if debug:
			print(self.cube.movements_applied)
			self.cube.display()
			time.sleep(2)
			self.cube.check()

		# If there's a solution already with less movements than this try
		# Cut off the branch
		if len(self.cube.movements_applied) > self.smallest_solution:
			return False

		if self.cube.solved:  # If the cube is solved add it as a possible solution
			self.n_solutions += 1
			solution = copy.copy(self.cube.movements_applied)
			print("=======  !!!SOLUTION with", len(solution), "movements!!! ========")
			if len(solution) < self.smallest_solution:
				self.smallest_solution = len(solution)
			if len(solution) in self.solved_solutions:
				self.solved_solutions[len(solution)].append(solution)
			else:
				self.solved_solutions[len(solution)] = [solution]
			return True

		# If the cube has registered current state with more movements left than the current try
		# Cut off the branch
		if self.cube.movements_applied:
			position_of_past_state = self.states.get(self.cube.json, None)
			if position_of_past_state:
				if len(self.cube.movements_applied) >= position_of_past_state:
					return False
			self.states[self.cube.json] = len(self.cube.movements_applied)

		if movements_left:
			movements = self.generate_movements(self.cube.last_movement)
			for movement in movements:
				self.cube.do_movement(movement)
				print("Trying movement", movement, ",", movements_left, "movements left (", self.n_solutions,"solutions found)")
				self.solve(movements_left=movements_left - 1, debug=debug)
				self.cube.undo()
		return False

	def generate_movements(self, last_movement=None):
		all_movements = ['U', 'D', 'R', 'L', 'F', 'B', 'U1', 'D1', 'R1', 'L1', 'F1', 'B1', 'M', 'E', 'S', 'M1', 'E1',
		                 'S1']
		if not last_movement:
			return all_movements
		all_movements.remove(RubikCube.get_opposite_movement(last_movement))
		return all_movements

class HeuristicSolver:

	LIMIT = 20

	def __init__(self, cube=None):
		self.cube = cube or RubikCube()
		self.n_movements_done = 0
		self.solutions = {}
		self.past_states = set()
		self.possible_solutions = {} #Heuristic -> [movements]
		self.smallest_solution = 40000
		self.n_solutions = 0
		self.randomizer_probability = 1

	def get_heuristic(self, cube):
		heuristic = 0
		for i, face in enumerate(cube):
			for j, cell in enumerate(face):
				if j != 4 and cell == i+1:
					heuristic += 1
		return heuristic

	def __randomizer(self):
		if random.randint(0, 100) < self.randomizer_probability:
			return 0
		else:
			return -1

	def solve(self):
		if self.cube.solved:
			print("Cube was already solved!!")
			self.solutions[0] = []
			return
		print("Generating first movement's heuristics")
		#Init first heuristics
		for movement in self.generate_movements():
			self.cube.do_movement(movement)
			heuristic = self.get_heuristic(self.cube.cube)
			if heuristic in self.possible_solutions:
				self.possible_solutions[heuristic].append([movement])
			else:
				self.possible_solutions[heuristic] = [[movement]]
			self.cube.undo()

		print("Starting...")

		while self.possible_solutions:

			greater_heuristic = sorted(self.possible_solutions.keys())[self.__randomizer()]
			random.shuffle(self.possible_solutions[greater_heuristic])
			possible_solution = self.possible_solutions[greater_heuristic].pop()
			print("Solutions:", self.n_solutions, "\tScore:", greater_heuristic, "\tPossible solution:", possible_solution)

			#If no more solutions with that heuristic score delete key
			if not self.possible_solutions[greater_heuristic]:
				del self.possible_solutions[greater_heuristic]

			#If possible solution is longer than smallest solution found, cut off branch
			if len(possible_solution) >= self.smallest_solution:
				continue



			#Performs movements of possible solution to the cube
			for movement in possible_solution:
				self.cube.do_movement(movement)

			# If current state has been already reached before, cut off branch
			if self.cube.json in self.past_states:
				continue

			#Check if cube is solved
			if self.cube.solved:
				print("Found solution in", len(possible_solution), "movements!!")
				self.n_solutions += 1
				if len(possible_solution) < self.smallest_solution:
					self.smallest_solution = len(possible_solution)

				if not self.solutions.get(len(possible_solution), False):
					self.solutions[len(possible_solution)] = [copy.deepcopy(possible_solution)]
				else:
					self.solutions[len(possible_solution)].append(copy.deepcopy(possible_solution))

			# If ongoing possible solutions are longer than the smallest solution, cut off branch
			if len(possible_solution) + 1 > self.smallest_solution or len(possible_solution) > HeuristicSolver.LIMIT:
				continue

			current_heuristic = self.get_heuristic(self.cube.cube)

			if not self.possible_solutions.get(current_heuristic, False):
				self.possible_solutions[current_heuristic] = []

			for new_movement in self.generate_movements(possible_solution[-1]):
				new_solutions = copy.copy(possible_solution)
				new_solutions.append(new_movement)
				self.possible_solutions[current_heuristic].append(new_solutions)

			for _ in possible_solution:
				self.cube.undo()




	def generate_movements(self, last_movement=None):
		all_movements = ['U', 'D', 'R', 'L', 'F', 'B', 'U1', 'D1', 'R1', 'L1', 'F1', 'B1', 'M', 'E', 'S', 'M1', 'E1',
		                 'S1']
		random.shuffle(all_movements)
		if not last_movement:
			return all_movements
		all_movements.remove(RubikCube.get_opposite_movement(last_movement))
		return all_movements