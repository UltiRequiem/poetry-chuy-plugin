import sys

try:
    from poetry.console import application as app
    from poetry.plugins.application_plugin import ApplicationPlugin
except ModuleNotFoundError:
    app = type("application", (), {"Application": None})
    ApplicationPlugin = type(
        "ApplicationPlugin",
        (),
        {"PLUGIN_API_VERION": "1.0.0", "type": "application.plugin"},
    )


class PoePlugin(ApplicationPlugin):
    def activate(self, application: app.Application) -> None:

        if app.Application is None:
            print(
                "Poetry not found. Did you install this plugin via `poetry plugin add poetry-chuy-plugin`?"
            )
            sys.exit(1)

        # I'm going to wait until the plugin API of poetry is more stable

        print("Is Working!")
        print(application)
