# def get_todos(filepath):
Filepath = "todos.txt"
def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_args,filepath=Filepath):
    """
    It just take the two arguments and one is the name of the file and other is what to write in the fiel
    """
    file = open(filepath, 'w')
    file.writelines(todos_args)
    file.close()


if __name__ == "__main__":
    print("Hi")
#If we want to print someting if we call a module but dont want to print that if we import that then we use the __name__.
#The __name__ is equal to __main__ if we run the file directly.