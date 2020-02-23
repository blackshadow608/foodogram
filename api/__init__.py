from api.user import user


class ApiService:
    app = None

    @classmethod
    def setup_blueprints(cls, app):
        cls.app = app
        cls.app.register_blueprint(user)
