FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    try:
        with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(filepath, "w") as file_local:
            pass
        todos_local = []
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list to the text file."""
    #print(f"Writing to file: {filepath}")  # Debugging
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("YNWA")

