import cmd


class MyInterpreter(cmd.Cmd):
    prompt = '>>> '

    def do_hello(self, arg):
        print('Hello, Camilo', arg)

    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    interpreter = MyInterpreter()
    interpreter.cmdloop('Starting prompt...')
