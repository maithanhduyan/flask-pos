from app import db

class Item(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Float)
    description = db.Column(db.String(256))
    image_url = db.Column(db.String(256))

    def __repr__(self):
        return '<Item {}>'.format(self.name)