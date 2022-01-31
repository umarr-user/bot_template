from dataclasses import dataclass
from yaml import safe_load


@dataclass
class BotConfig:
    token: str
    admin_ids: list[str]


@dataclass
class DBConfig:
    host: str
    user: str
    password: str
    database: str


@dataclass
class LoggingConfig:
    level: str
    format: str
    log_file: str
    rotation: str
    compression: str


@dataclass
class Config:
    bot: BotConfig
    db: DBConfig
    logging: LoggingConfig


def load_config(config_file: str) -> Config:
    with open(config_file, 'r', encoding='utf-8') as file:
        config = safe_load(file)

    return Config(
        bot=BotConfig(
            token=config['bot']['token'],
            admin_ids=config['bot']['admin_ids']
        ),
        db=DBConfig(
            host=config['db']['host'],
            user=config['db']['user'],
            password=config['db']['password'],
            database=config['db']['database']
        ),
        logging=LoggingConfig(
            level=config['logging']['level'],
            format=config['logging']['format'],
            log_file=config['logging']['log_file'],
            rotation=config['logging']['rotation'],
            compression=config['logging']['compression']
        )
    )
