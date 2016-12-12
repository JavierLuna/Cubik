from cubik import HeuristicSolver
import json

solver = HeuristicSolver()
try:
	solver.solve()
except KeyboardInterrupt:
	pass

try:
	with open("solution.json", 'w') as file:
		json.dump(solver.solutions, file, indent=4)
	print(solver.solutions)
except Exception as e:
	with open('solution.json', 'w') as file:
		file.write("Error :(\n")
		file.write(str(e))