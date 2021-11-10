from enum import unique
from myapp import db

class TopCities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64),nullable = False)
    city_rank = db.Column(db.Integer,nullable = False)
    is_visited = db.Column(db.Boolean)

    def __repr__(self):
        return f'<city_name  {self.city_name} city_rank {self.city_rank}>'
