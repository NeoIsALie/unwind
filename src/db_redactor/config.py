from pydantic import BaseSettings


class Settings(BaseSettings):
    cb_request_url: str = "http://www.cbr.ru/scripts/XML_daily.asp"
    creds_filename: str = "creds_google.json"
    file_name: str = "today_rate.txt"
    spreadsheet_id: str = "1Swh1pi3m_kBXQQ_nnPjmDAhPgUHh1ElYO_sc9VKn5LQ"
    bot_token: str = "5522983032:AAHHks_5nzR6upv26HCa8BJvtHIZWuRX-cc"
    chat_id: str = "-1001798624557"
    api_time_interval: float = 1.5  # Seconds between two calls to google API. Min value is 1 second (60 requests / min)

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

DATABASE = {
    "drivername": "postgresql+psycopg2",
    "host": "db",
    "port": "5432",
    "username": "user_app",
    "password": "user_pwd_01",
    "database": "spreadsheet",
}
