from cubik import RubikCube, RubikSolver
import time

cube = RubikCube(cube=RubikCube.SOLVED)
cube.display()
cube.U()
solver = RubikSolver(cube=cube)
solver.solve(debug=True)