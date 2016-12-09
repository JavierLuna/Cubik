from cubik import RubikSolver
import json

solver = RubikSolver()
solver.solve()

with open('solution.json', 'w') as file:
	json.dump(solver.shortest_solution, file,  indent=4, sort_keys=True)