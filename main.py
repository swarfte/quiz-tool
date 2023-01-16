import json
from importlib import import_module

class Main(object):
    def __init__(self) -> None:
        with open("./config/setting.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        database_package = import_module(f"tool.database.{config['database']}")
        model_package = import_module(f"tool.model.{config['model']}")
        controller_package = import_module(f"tool.controller.{config['controller']}")
        view_package = import_module(f"tool.view.{config['view']}")

        self.database = eval(f"database_package.{config['database']}")(config["path"])
        self.model = eval(f"model_package.{config['model']}(self.database)")
        self.controller = eval(f"controller_package.{config['controller']}(self.model)")
        self.view = eval(f"view_package.{config['view']}(self.controller)")
        self.view.run()


if __name__ == "__main__":
    Main()
