from flask import Flask
from config import BaseConfig, VkConfig, LoggerConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from vk_api import VkApi
import logging

from core.controler import EventControler
from handlers_settings import HANDLERS_LIST

app = Flask(__name__)
app.config.from_object(BaseConfig)

api = VkApi(token=VkConfig.TOKEN)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

logger_handler = logging.FileHandler(LoggerConfig.FILE_NAME)
logger_formatter = logging.Formatter(LoggerConfig.FORMAT)

logger_handler.setLevel(LoggerConfig.LEVEL)
logger_handler.setFormatter(logger_formatter)

app.logger.addHandler(logger_handler)

controler = EventControler(HANDLERS_LIST, api, db, app.logger)