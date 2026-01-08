from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant

# Blueprintの作成
reg_bp = Blueprint('res_reg', __name__, url_prefix='/restaurants')