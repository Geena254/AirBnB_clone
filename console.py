#!/usr/bin/python3
"""This is the script for the entry point of the command line interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class for the command line intepreter."""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ = '__main__':
    HBNB() = cmdloop()
