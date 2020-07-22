from flask import Flask
from config import BaseConfig, VkConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from vk_api import VkApi

from core.controler import EventControler
from handlers_settings import HANDLERS_LIST


app = Flask(__name__)
app.config.from_object(BaseConfig)

api = VkApi(token=VkConfig.TOKEN)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

controler = EventControler(HANDLERS_LIST, api, db)