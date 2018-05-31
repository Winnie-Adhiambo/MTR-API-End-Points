import os

class Config(object):
    """Parent Configuration Class"""
    DEBUG = False
    CSFR_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True


class TestingConfig(Config):
    """Configuration for testing separate database"""
    TESTING = True
    DEBUG=True

class StagingConfig(Config):
    """Configuration for staging"""
    DEBUG = True

class ProductionConfig(Config):
    """ Configuration for production"""
    DEBUG = False
    TESTING = False

app_config = {

'development':DevelopmentConfig,
'testing': TestingConfig,
'staging': StagingConfig,
'production': ProductionConfig

}