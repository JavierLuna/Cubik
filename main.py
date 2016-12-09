from cubik import RubikCube, RubikSolver
import json

cube = RubikCube(cube=RubikCube.SOLVED)
cube.display()
cube.U()
solver = RubikSolver(cube=cube)
solver.solve(movements_left=4)

with open('solution.json', 'w') as file:
	json.dump(solver.solved_solutions,file,  indent=4, sort_keys=True)