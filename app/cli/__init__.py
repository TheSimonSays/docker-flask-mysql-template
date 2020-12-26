from flask import Blueprint


bp = Blueprint('cli', __name__)


from app.cli import commands
