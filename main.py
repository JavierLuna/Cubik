from cubik import HeuristicSolver, RubikCube

solver = HeuristicSolver()
try:
	solver.solve()
except KeyboardInterrupt:
	pass
print(solver.solutions)