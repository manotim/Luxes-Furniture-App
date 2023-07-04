from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Furniture(db.Model, SerializerMixin):
    __tablename__ = 'furnitures'

    serialize_rules = ('-purchases.furniture',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    purchases = db.relationship('Purchase', backref='furniture')


class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    serialize_rules = ('-purchases.customer',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    contact = db.Column(db.Integer)
    address = db.Column(db.String)
    purchases = db.relationship('Purchase', backref='customer')
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza')

    

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    # serialize_rules = ('-restaurantpizzas.game',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    address = db.Column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza')

  

class Purchase(db.Model, SerializerMixin):
    __tablename__ = 'purchases'

    serialize_rules = ('-furniture.purchases', '-customer.purchases',)

    id = db.Column(db.Integer, primary_key=True)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furnitures.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    # name = db.Column(db.String, unique=True)
    # location = db.Column(db.String)
    # address = db.Column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza')

 


# class RestaurantPizza(db.Model, SerializerMixin):
#     __tablename__ = 'restaurantpizzas'

#     serialize_rules = ('-pizza.restaurantpizzas', '-restaurant.restaurantpizzas',)

#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    # restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    # def __repr__(self):
    #     return f'<RestaurantPizza ({self.id}) of {self.pizza}: {self.price}>'
