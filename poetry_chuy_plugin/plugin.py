from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin


class CustomCommand(Command):

    name = "my-command"

    def handle(self) -> int:
        self.line("My command")

        return 0


def factory():
    return CustomCommand()


class MyApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("my-command", factory)
