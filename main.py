import numpy as np
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

# Initialize rich console
console = Console()

# Function to create the matrix
def create_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = Prompt.ask(f"Enter a_{i+1}{j+1}", default="0")
            row.append(int(entry))
        matrix.append(row)
    return np.array(matrix)

# Function to perform matrix operations
def perform_operation(matrix, operation):
    if operation == "determinant":
        determinant = np.linalg.det(matrix)
        console.print(Panel(f"Determinant of the matrix is: {determinant}", title="Determinant"))

    elif operation == "minor":
        cij = Prompt.ask("Enter the position of the matrix in the form of ij (e.g., 11 for a_11)")
        row = int(cij[0]) - 1
        col = int(cij[1]) - 1
        minor_matrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
        minor = np.linalg.det(minor_matrix)
        console.print(Panel(f"Minor of element at position {cij} is: {minor}", title="Minor"))

    elif operation == "cofactor":
        cofactor_matrix = np.zeros_like(matrix, dtype=float)
        for i in range(3):
            for j in range(3):
                minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor_matrix[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor_matrix)
        console.print(Panel(f"Cofactor matrix is:\n{cofactor_matrix}", title="Cofactor"))

    elif operation == "transpose":
        transpose_matrix = np.transpose(matrix)
        console.print(Panel(f"Transpose of the matrix is:\n{transpose_matrix}", title="Transpose"))

    elif operation == "eigenvalues":
        eigenvalues = np.linalg.eigvals(matrix)
        console.print(Panel(f"Eigenvalues of the matrix are:\n{eigenvalues}", title="Eigenvalues"))

    elif operation == "rank":
        rank = np.linalg.matrix_rank(matrix)
        console.print(Panel(f"Rank of the matrix is: {rank}", title="Rank"))

    elif operation == "inverse":
        try:
            inverse_matrix = np.linalg.inv(matrix)
            console.print(Panel(f"Inverse of the matrix is:\n{inverse_matrix}", title="Inverse"))
        except:
            console.print(Panel("The matrix is singular and does not have an inverse.", title="Error", style="red"))

# Main function to run the application
def main():
    matrix = None

    while True:
        console.print(Panel("Matrix Operations", style="bold white on black"))
        console.print("1. Create Matrix")
        console.print("2. Determinant")
        console.print("3. Minor")
        console.print("4. Cofactor")
        console.print("5. Transpose")
        console.print("6. Eigenvalues")
        console.print("7. Rank")
        console.print("8. Inverse")
        console.print("9. Exit")

        option = Prompt.ask("Select an option (1-9)", choices=[str(i) for i in range(1, 10)])

        if option == "1":
            matrix = create_matrix()
        elif option == "2":
            if matrix is not None:
                perform_operation(matrix, "determinant")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "3":
            if matrix is not None:
                perform_operation(matrix, "minor")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "4":
            if matrix is not None:
                perform_operation(matrix, "cofactor")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "5":
            if matrix is not None:
                perform_operation(matrix, "transpose")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "6":
            if matrix is not None:
                perform_operation(matrix, "eigenvalues")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "7":
            if matrix is not None:
                perform_operation(matrix, "rank")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "8":
            if matrix is not None:
                perform_operation(matrix, "inverse")
            else:
                console.print(Panel("Please create a matrix first.", style="red"))
        elif option == "9":
            console.print(Panel("Exiting the program. Goodbye!", style="bold white on black"))
            break

# Run the application
if __name__ == "__main__":
    main()