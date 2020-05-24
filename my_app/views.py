from my_app import app, db
from my_app.settings import app_cfg
from flask import render_template, url_for, request, jsonify
from my_app.models import Bookings, BookingSchema
from flask_marshmallow import Marshmallow

#
# # Create ma for Marshmallow
ma = Marshmallow(app)


# Init schema
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)


# Say Hello as a test of the basic functionality
@app.route('/', methods=['GET'])
def hello():
    result = "Hello !"
    return result


# Get Single Booking using GET
@app.route('/booking/<id>', methods=['GET'])
def get_booking(id):
    booking = Bookings.query.get(id)
    if booking is None:
        print('ID',  id, 'NOT found')
    return booking_schema.jsonify(booking)


# Get Multiple Bookings using GET
@app.route('/booking/customer/<customer>', methods=['GET'])
def get_bookings(customer):
    print('lookup customer', customer)
    customer_bookings = Bookings.query.filter_by(erp_end_customer_name=customer).all()
    print('found', len(customer_bookings), 'bookings')
    result = bookings_schema.dump(customer_bookings)
    return jsonify(result)


# Create a Booking using POST
@app.route('/booking', methods=['POST'])
def add_booking():
    fiscal_year = request.json['fiscal_year']
    erp_end_customer_name = request.json['customer_name']
    product_id = request.json['product_id']
    tms_sales_allocated_product_bookings_net = request.json['revenue']

    print(fiscal_year,tms_sales_allocated_product_bookings_net)
    new_booking = Bookings(fiscal_year, erp_end_customer_name,
                           product_id, tms_sales_allocated_product_bookings_net)

    db.session.add(new_booking)
    db.session.commit()

    return booking_schema.jsonify(new_booking)


# Update a Booking using PUT
@app.route('/booking/<id>', methods=['PUT'])
def update_booking(id):
  booking = Bookings.query.get(id)

  fiscal_year = request.json['fiscal_year']
  customer_name = request.json['customer_name']
  product_id = request.json['product_id']
  revenue = request.json['revenue']


  booking.fiscal_year = fiscal_year
  booking.erp_end_customer_name = customer_name
  booking.product_id = product_id
  booking.tms_sales_allocated_product_bookings_net = revenue

  db.session.commit()

  return booking_schema.jsonify(booking)


# Delete booking using DELETE
@app.route('/booking/<id>', methods=['DELETE'])
def delete_booking(id):
  booking = Bookings.query.get(id)
  db.session.delete(booking)
  db.session.commit()

  return booking_schema.jsonify(booking)


