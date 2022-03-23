from . import db

class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Properties'

    id = db.Column(db.Integer, primary_key=True)
    property_title= db.Column(db.String(100))
    description = db.Column(db.String(300))
    bedrooms = db.Column(db.String(100))
    bathrooms = db.Column(db.String(300))
    price = db.Column(db.String(300))
    property_type = db.Column(db.String(300))
    location = db.Column(db.String(300), unique=True)
    photo = db.Column(db.String(300))

    def __init__(self, property_title, description, bedrooms, bathrooms, price, property_type, location, photo):
        self.property_title = property_title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.property_title)
