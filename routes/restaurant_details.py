from flask import Blueprint, render_template
from models import Restaurant, Review

# Blueprintの作成
details_bp = Blueprint('res_details', __name__, url_prefix='/restaurants')