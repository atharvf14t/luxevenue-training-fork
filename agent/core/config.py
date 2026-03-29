from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Azure OpenAI
    azure_openai_api_key: str
    azure_openai_endpoint: str
    azure_openai_deployment: str = "gpt-4o"
    azure_openai_api_version: str = "2024-08-01-preview"

    # PostgreSQL
    database_url: str

    # SMTP
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 465
    smtp_sender_email: str
    smtp_app_password: str

    # Security
    internal_api_key: str

    # Server
    host: str = "0.0.0.0"
    port: int = 8000


settings = Settings()
