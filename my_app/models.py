from my_app import db
from my_app import ma


# Bookings Class/Model
class Bookings(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    fiscal_year = db.Column(db.String(100))
    erp_end_customer_name = db.Column(db.String(200))
    product_id = db.Column(db.String(200))
    tms_sales_allocated_product_bookings_net = db.Column(db.Float)

    def __init__(self,
                 fiscal_year,
                 erp_end_customer_name,
                 product_id,
                 tms_sales_allocated_product_bookings_net):

        self.fiscal_year = fiscal_year
        self.erp_end_customer_name = erp_end_customer_name
        self.product_id = product_id
        self.tms_sales_allocated_product_bookings_net = tms_sales_allocated_product_bookings_net


# Product Schema
class BookingSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'fiscal_year',
                  'erp_end_customer_name',
                  'product_id',
                  'tms_sales_allocated_product_bookings_net')
