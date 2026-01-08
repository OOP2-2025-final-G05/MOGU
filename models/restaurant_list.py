# 今はDB未使用なので「データの形」だけ用意

class Restaurant:
    def __init__(self, id, name, address, min_price, max_price, avg_rating):
        self.id = id
        self.name = name
        self.address = address
        self.min_price = min_price
        self.max_price = max_price
        self.avg_rating = avg_rating
