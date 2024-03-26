from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    BOT_TOKEN: str
    
    @property
    def DATABASE_URL_mysql(self):
        return f'mysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}'
    
    def BOT_TOKEN(self):
        return self.BOT_TOKEN
    
    model_config = SettingsConfigDict(env_file='.env')
    
settings = Settings()