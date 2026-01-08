from flask import Blueprint, request, redirect, url_for
from models import Review

# Blueprintの作成
review_bp = Blueprint('review', __name__, url_prefix='/reviews')