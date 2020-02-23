import os

from flask import Flask

from api import ApiService

app = Flask(__name__)


class Envs:
    TEST = 'test'
    PROD = 'prod'
    DEV = 'dev'
    __configs = {
        TEST: 'settings.dev_settings',
        PROD: 'settings.dev_settings',
        DEV: 'settings.dev_settings',
    }

    def get_config(self, name):
        return self.__configs.get(name)


envs = Envs()
config_object = envs.get_config(os.environ.get("ENVIRON", default=Envs.TEST))
app.config.from_object(config_object)

ApiService.setup_blueprints(app)


if __name__ == '__main__':
    app.run()
