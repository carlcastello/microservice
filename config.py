import os

from typing import Optional, Dict, Union, Type


class Config:
    SECRET_KEY: Optional[str] = os.environ.get('SECRET_KEY')
    SSL_REDIRECT: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_RECORD_QUERIES: bool = True

    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATAPASE_USERNAME: Optional[str] = os.environ.get(
        'DATABASE_USERNAME')
    SQLALCHEMY_DATAPASE_PASS: Optional[str] = os.environ.get(
        'DATABASE_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG: bool = True
    TESTING: bool = True

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


class Production(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config: Dict[str, Union[Type[Development], Type[Staging], Type[Production]]] = {
    'development': Development,
    'staging': Staging,
    'production': Production,
    'default': Development
}
