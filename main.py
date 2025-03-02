from solver import bfs_solve

def print_solution(solution):

    if solution:
        print("\nSolution Found:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")


solution = bfs_solve()
print_solution(solution)

