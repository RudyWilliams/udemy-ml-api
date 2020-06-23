from api.app import create_app
from api.config import DevelopmentConfig

application = create_app(config_obj=DevelopmentConfig)

if __name__ == "__main__":
    application.run()
