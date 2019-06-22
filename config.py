import os

from typing import Optional, Dict, Union, Type


class Config:
    SECRET_KEY: Optional[str] = os.environ.get('SECRET_KEY')
    SSL_REDIRECT: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_RECORD_QUERIES: bool = True

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: Optional[str] = \
        f'postgresql://{os.environ.get("DEV_DB_AUTH")}@{os.environ.get("DEV_DB_HOST")}:5432/{os.environ.get("DB_NAME")}'


    @staticmethod
    def init_app(app):
        Config.init_app(app)

        import logging
        from logging.handlers import SysLogHandler

        sys_logger: SysLogHandler = SysLogHandler()
        sys_logger.setLevel(logging.WARNING)
        app.logger.addHandler(sys_logger)


class Staging(Config):
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: Optional[str] = \
        f'postgresql://{os.environ.get("STAG_DB_AUTH")}@{os.environ.get("STAG_DB_HOST")}:5432/{os.environ.get("DB_NAME")}'


class Production(Config):
    SQLALCHEMY_DATABASE_URI: Optional[str] = \
        f'postgresql://{os.environ.get("PROD_DB_AUTH")}@{os.environ.get("PROD_DB_HOST")}:5432/{os.environ.get("DB_NAME")}'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config: Dict[str, Union[Type[Development], Type[Staging], Type[Production]]] = {
    'development': Development,
    'staging': Staging,
    'production': Production,
    'default': Development
}
