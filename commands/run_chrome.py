from commands.command import Command


class RunChrome(Command):

    def get_phrases(self):
        return ["ejecuta navegador", "abre chrome", "abre crome"]

    def execute(self):
        print("Ejecutando crome !!!!!!!")