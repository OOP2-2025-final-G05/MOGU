from .restaurant_list import list_bp
from .restaurant_registration import reg_bp
from .restaurant_details import details_bp
from .review import review_bp

blueprints = [
    list_bp, reg_bp, 
    details_bp, 
    review_bp
    ]