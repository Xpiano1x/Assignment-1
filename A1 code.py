# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qjp6LAo_uUaSI9a529UUwltWtTm7qpeJ
"""

from enum import Enum

# Enums
class OrderStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    PAYPAL = "PayPal"
    CASH_ON_DELIVERY = "Cash on Delivery"

class YesNo(Enum):
    YES = "Yes"
    NO = "No"

# Customer Class
class Customer:
    def __init__(self, customer_id, name, email, phone_number, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def get_customer_details(self):
        return f"""
Customer ID: {self.customer_id}
Name: {self.name}
Email: {self.email}
Phone: {self.phone_number}
Address: {self.address}
"""

    def set_address(self, new_address):
        self.address = new_address

    def set_phone_number(self, new_phone):
        self.phone_number = new_phone

# Order Class
class Order:
    def __init__(self, order_id, customer, items, total_amount, status):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def get_order_details(self):
        items_details = "\n".join([f"{item.name} - ${item.price} x {item.quantity}" for item in self.items])
        return f"""
Order ID: {self.order_id}
Status: {self.status.value}
Items:
{items_details}
Total Amount: ${self.total_amount}
"""

    def generate_delivery_note(self):
        return DeliveryNote(1, self, "Delivery scheduled.")

    def set_status(self, new_status):
        self.status = new_status

    def process_order(self):
        pass  # Logic to process the order

# DeliveryPerson Class
class DeliveryPerson:
    def __init__(self, person_id, name, phone_number):
        self.person_id = person_id
        self.name = name
        self.phone_number = phone_number

    def get_delivery_person_details(self):
        return f"""
Delivery Person: {self.name}
Phone: {self.phone_number}
"""

    def update_availability(self):
        pass  # Logic to update availability status

# Delivery Class
class Delivery:
    def __init__(self, delivery_id, order, delivery_person, status, estimated_arrival):
        self.delivery_id = delivery_id
        self.order = order
        self.delivery_person = delivery_person
        self.status = status
        self.estimated_arrival = estimated_arrival

    def get_delivery_details(self):
        return f"""
Delivery ID: {self.delivery_id}
Status: {self.status.value}
Estimated Arrival: {self.estimated_arrival}
"""

    def set_status(self, new_status):
        self.status = new_status

    def track_delivery(self):
        pass  # Logic to track the delivery status

# Item Class
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self):
        pass  # Logic to update item quantity

# Payment Class
class Payment:
    def __init__(self, payment_id, order, payment_method, amount_paid):
        self.payment_id = payment_id
        self.order = order
        self.payment_method = payment_method
        self.amount_paid = amount_paid

    def get_payment_details(self):
        return f"""
Payment ID: {self.payment_id}
Payment Method: {self.payment_method.value}
Amount Paid: ${self.amount_paid}
"""

    def set_amount_paid(self, new_amount):
        self.amount_paid = new_amount

    def process_payment(self):
        pass  # Logic to process payment

# DeliveryNote Class
class DeliveryNote:
    def __init__(self, note_id, order, delivery_details):
        self.note_id = note_id
        self.order = order
        self.delivery_details = delivery_details

    def get_delivery_note_details(self):
        return f"""
========== DELIVERY NOTE ==========
Delivery Note ID: {self.note_id}
Order ID: {self.order.order_id}
Customer: {self.order.customer.name}
Total Amount: ${self.order.total_amount}
Status: {self.order.status.value}
{self.delivery_details}
====================================
"""

# Object Creation & Delivery Note Generation
customer = Customer(1, "reem", "ReemAlhamami@gmail.com", "1234567890", "123 Main St")
items = [Item(101, "Laptop", 1000.0, 1), Item(102, "Mouse", 50.0, 2)]
order = Order(1, customer, items, 1100.0, OrderStatus.PENDING)
delivery_person = DeliveryPerson(1, "Saleh", "0987654321")
delivery = Delivery(1, order, delivery_person, OrderStatus.PENDING, "Tomorrow")
delivery_note = order.generate_delivery_note()
payment = Payment(1, order, PaymentMethod.CREDIT_CARD, 1100.0)

# Displaying Data
print("===== CUSTOMER DETAILS =====")
print(customer.get_customer_details())
print("===== ORDER DETAILS =====")
print(order.get_order_details())
print("===== DELIVERY PERSON DETAILS =====")
print(delivery_person.get_delivery_person_details())
print("===== DELIVERY DETAILS =====")
print(delivery.get_delivery_details())
print("===== PAYMENT DETAILS =====")
print(payment.get_payment_details())
print(delivery_note.get_delivery_note_details())