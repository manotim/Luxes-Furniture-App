from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Furniture, Customer, Owner, Purchase

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Furniture API"

#getting all furniture

@app.route('/furniture', methods=["GET"])
def get_all_furniture():
    furniture = Furniture.query.order_by(Furniture.id).all()
    data = [
        {
            "id": furniture.id,
            "name": furniture.name,
            "description": furniture.description,
            "price": furniture.price,
            "image": furniture.image,
            "category": furniture.category,
        }
        for furniture in furniture
    ]
    return jsonify(data)


#getting furniture by id

@app.route('/furniture/<int:id>', methods=["GET"])
def get_furniture(id):
    furniture = Furniture.query.filter_by(id=id).first()
    if furniture:
        data = {
            "id": furniture.id,
            "name": furniture.name,
            "description": furniture.description,
            "price": furniture.price,
            "image": furniture.image,
            "category": furniture.category,
        }
        return jsonify(data)
    else:
        return jsonify({"error": "furniture not found"}), 404

#deleting a furniture

@app.route('/furniture/<int:id>', methods=['DELETE'])
def delete_furniture(id):
    furniture = Furniture.query.get(id)
    if furniture:
        Purchase.query.filter_by(furniture_id=id).delete()
        db.session.delete(furniture)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Furniture not found'}),404
    
# getting all customers

@app.route('/customers', methods=["GET"])
def get_all_customers():
    customers = Customer.query.order_by(Customer.id).all()
    data = [
        {
            "id": customers.id,
            "name": customers.name,
            "contact": customers.contact,
            "address": customers.address,
        }
        for customers in customers
    ]
    return jsonify(data)

#getting customer by id

@app.route('/customers/<int:id>', methods=["GET"])
def get_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        data = {
            "id": customer.id,
            "name": customer.name,
            "contact": customer.contact,
            "address": customer.address,
        }
        return jsonify(data)
    else:
        return jsonify({"error": "customer not found"}), 404

#deleting a customer
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer:
        Purchase.query.filter_by(customer_id=id).delete()
        db.session.delete(customer)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'customer not found'}),404
    
if __name__ == '__main__':
    app.run(port=5555)