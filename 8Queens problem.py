import numpy as np

def is_safe(board, row, col, n):
    # Check same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n, solutions, max_solutions=None):
    if col >= n:
        solutions.append(np.copy(board))
        return max_solutions is None or len(solutions) < max_solutions

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if not solve_n_queens(board, col + 1, n, solutions, max_solutions):
                return False
            board[i][col] = 0  # Backtrack
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print("\n")

def main():
    n = 8
    board = np.zeros((n, n), dtype=int)
    solutions = []
    max_solution = 3  # You can increase this number to see more solutions

    solve_n_queens(board, 0, n, solutions, max_solutions=max_solution)

    print(f"Showing up to {max_solution if max_solution else 'all'} solutions:\n")
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        print_board(solution)

if __name__ == "__main__":
    main()
