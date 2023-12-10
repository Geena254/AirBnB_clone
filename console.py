#!/usr/bin/python3
"""This is the script for the entry point of the command line interpreter."""

import re
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class for the command line intepreter."""

    prompt = "(hbnb)"

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        twin = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not twin:
            return line
        classname = twin.group(1)
        method = twin.group(2)
        args = twin.group(3)
        twin_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if twin_uid_and_args:
            uid = twin_uid_and_args.group(1)
            att_or_dict = twin_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        att_and_value = ""
        if method == "update" and att_or_dict:
            twin_dict = re.search('^({.*})$', att_or_dict)
            if twin_dict:
                self.update_dict(classname, uid, twin_dict.group(1))
                return ""
            twin_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', att_or_dict)
            if twin_attr_and_value:
                att_and_value = (twin_attr_and_value.group(
                    1) or "") + " " + (twin_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + att_and_value
        self.onecmd(command)
        return command

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
