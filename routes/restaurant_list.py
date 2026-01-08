from flask import Blueprint, render_template, request
from models import Restaurant

# Blueprintの作成
list_bp = Blueprint('res_list', __name__, url_prefix='/restaurants')