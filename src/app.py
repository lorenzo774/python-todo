from todo import Todo
import keyboard
from utils import clear, message

class App:
    def __init__(self):
        self.__todos = [Todo("Hello, world!")]
        self.__key_check_uncheck = 't'
        self.__key_add = 'a'
        self.__key_edit = 'e'
        self.__key_remove = 'r'
        self.__key_quit = 'q'
        self.__tutorial = f'''{self.__key_quit} = Exit
{self.__key_edit} = Edit an item message
{self.__key_add} = Add a new item
{self.__key_remove} = Remove an item
{self.__key_check_uncheck} = Toggle todo item\n\n'''
    
    def run(self):
        """
        Run the application    
        """
        running = True
        while running:
            self.__render_todos()
            key = keyboard.read_key()
            match key:
                case self.__key_quit:
                    running = False
                case self.__key_add:
                    self.__add_todo_action()
                case self.__key_remove:
                    self.__remove_todo_action()
                case self.__key_edit:
                    self.__edit_todo_action()
                case self.__key_check_uncheck:
                    self.__toggle_check_todo_action()

            
    def __render_todos(self):
        clear()
        rendered = "\n".join(map(lambda td: f'\t - [{"✅" if td.is_done() else " "}] {td.get_msg()}', self.__todos))
        print(self.__tutorial, rendered, "\n")

    def __select_index(self) -> int:
        """
        Ask an index to use for the todo list
        """
        ask_input = True
        while ask_input:
            try:
                ind = int(input("Index: "))
                ask_input = True if ind >= len(self.__todos) else False
                if ask_input:
                    continue
                return ind
            except Exception:
                print("Not a valid number, try again")
                continue

    def __add_todo_action(self):
        """
        Action to create a new todo item
        """
        clear()
        msg = message()
        todo = Todo(msg)
        self.__todos.append(todo)

    def __remove_todo_action(self):
        """
        Action to remove a todo based on the index
        """
        ind = self.__select_index()
        self.__todos.pop(ind)

        
    def __edit_todo_action(self):
        """
        Action to edit a todo based on the index
        """
        ind = self.__select_index()
        msg = message()
        self.__todos[ind].set_msg(msg)

    def __toggle_check_todo_action(self):
        """
        Action to toggle the check state of a todo element
        """
        ind = self.__select_index()
        self.__todos[ind].toggle_check()