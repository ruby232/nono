from commands.command import Command


class RunChrome(Command):

    def get_phrase(self):
        return "ejecuta navegador"

    def execute(self):
        print("Ejecutando crome !!!!!!!")