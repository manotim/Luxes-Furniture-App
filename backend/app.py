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
    
#post route for furniture

@app.route('/furniture', methods=["POST"])
def create_furniture():
    data = request.json
    furniture = Furniture(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        image=data.get('image'),
        category=data.get('category')
    )
    db.session.add(furniture)
    db.session.commit()
    return jsonify({"message": "Furniture created successfully"}), 201

#put method for updating furniture

@app.route('/furniture/<int:id>', methods=["PUT"])
def update_furniture(id):
    furniture = Furniture.query.get(id)
    if furniture:
        data = request.json
        furniture.name = data.get('name')
        furniture.description = data.get('description')
        furniture.price = data.get('price')
        furniture.image = data.get('image')
        furniture.category = data.get('category')
        db.session.commit()
        return jsonify({"message": "Furniture updated successfully"})
    else:
        return jsonify({"error": "Furniture not found"}), 404
    
#patch method for furniture

@app.route('/furniture/<int:id>', methods=["PATCH"])
def patch_furniture(id):
    furniture = Furniture.query.get(id)
    if furniture:
        data = request.json
        if 'name' in data:
            furniture.name = data.get('name')
        if 'description' in data:
            furniture.description = data.get('description')
        if 'price' in data:
            furniture.price = data.get('price')
        if 'image' in data:
            furniture.image = data.get('image')
        if 'category' in data:
            furniture.category = data.get('category')
        db.session.commit()
        return jsonify({"message": "Furniture patched successfully"})
    else:
        return jsonify({"error": "Furniture not found"}), 404

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
    
#post route for customers

@app.route('/customers', methods=["POST"])
def create_customer():
    data = request.json
    customer = Customer(
        name=data.get('name'),
        contact=data.get('contact'),
        address=data.get('address')
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify({"message": "Customer created successfully"}), 201

#put method for customers

@app.route('/customers/<int:id>', methods=["PUT"])
def update_customer(id):
    customer = Customer.query.get(id)
    if customer:
        data = request.json
        customer.name = data.get('name')
        customer.contact = data.get('contact')
        customer.address = data.get('address')
        db.session.commit()
        return jsonify({"message": "Customer updated successfully"})
    else:
        return jsonify({"error": "Customer not found"}), 404

#patch method for customers

@app.route('/customers/<int:id>', methods=["PATCH"])
def patch_customer(id):
    customer = Customer.query.get(id)
    if customer:
        data = request.json
        if 'name' in data:
            customer.name = data.get('name')
        if 'contact' in data:
            customer.contact = data.get('contact')
        if 'address' in data:
            customer.address = data.get('address')
        db.session.commit()
        return jsonify({"message": "Customer patched successfully"})
    else:
        return jsonify({"error": "Customer not found"}), 404

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

# getting owners

@app.route('/owners', methods=["GET"])
def get_all_owners():
    owners = Owner.query.order_by(Owner.id).all()
    data = [
        {
            "id": owners.id,
            "name": owners.name,
            "location": owners.location,
            "address": owners.address,
        }
        for owners in owners
    ]
    return jsonify(data)

# getting owners by id

@app.route('/owners/<int:id>', methods=["GET"])
def get_owner(id):
    owner = Owner.query.filter_by(id=id).first()
    if owner:
        data = {
            "id": owner.id,
            "name": owner.name,
            "location": owner.location,
            "address": owner.address,
        }
        return jsonify(data)
    else:
        return jsonify({"error": "owner not found"}), 404

# post route for owners

@app.route('/owners', methods=["POST"])
def create_owner():
    data = request.json
    owner = Owner(
        name=data.get('name'),
        location=data.get('location'),
        address=data.get('address')
    )
    db.session.add(owner)
    db.session.commit()
    return jsonify({"message": "Owner created successfully"}), 201

# put route for owners
    
@app.route('/owners/<int:id>', methods=["PUT"])
def update_owner(id):
    owner = Owner.query.get(id)
    if owner:
        data = request.json
        owner.name = data.get('name')
        owner.location = data.get('location')
        owner.address = data.get('address')
        db.session.commit()
        return jsonify({"message": "Owner updated successfully"})
    else:
        return jsonify({"error": "Owner not found"}), 404

# patch route for owners
    
@app.route('/owners/<int:id>', methods=["PATCH"])
def patch_owner(id):
    owner = Owner.query.get(id)
    if owner:
        data = request.json
        if 'name' in data:
            owner.name = data.get('name')
        if 'location' in data:
            owner.location = data.get('location')
        if 'address' in data:
            owner.address = data.get('address')
        db.session.commit()
        return jsonify({"message": "Owner patched successfully"})
    else:
        return jsonify({"error": "Owner not found"}), 404

# deleting an owner
    
@app.route('/owners/<int:id>', methods=['DELETE'])
def delete_owner(id):
    owner = Owner.query.get(id)
    if owner:
        Purchase.query.filter_by(owner_id=id).delete()
        db.session.delete(owner)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'owner not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)