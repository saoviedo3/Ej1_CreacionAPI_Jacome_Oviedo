from flask import jsonify, request
from .models import db, Product

def configure_routes(app):
    @app.route('/')
    def index():
        return jsonify({"message": "Bienvenido a la API de gestión de productos, en el siguiente enlace se puede ver los productos: http://127.0.0.1:5000/products"}), 200

    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])

    @app.route('/products/<int:id>', methods=['GET'])
    def get_product(id):
        product = Product.query.get(id)
        return jsonify(product.to_dict()) if product else ({"error": "Product not found"}, 404)

    @app.route('/products', methods=['POST'])
    def create_product():
        data = request.json
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

    @app.route('/products/<int:id>', methods=['PUT'])
    def update_product(id):
        product = Product.query.get(id)
        if not product:
            return {"error": "Product not found"}, 404
        for key, value in request.json.items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify(product.to_dict())

    @app.route('/products/<int:id>', methods=['DELETE'])
    def delete_product(id):
        product = Product.query.get(id)
        if not product:
            return {"error": "Product not found"}, 404
        db.session.delete(product)
        db.session.commit()
        return '', 204
