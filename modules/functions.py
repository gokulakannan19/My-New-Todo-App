FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """" Read the text file and return the items"""
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the items list to the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
