from starlette.config import Config

#realization connect to db
config = Config(".env_dev")
DATABASE_URL = config("EE_DATABASE_URL", cast=str, default = "")
