#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.last_transaction = 0
        self.discount = discount
        self.items = []  # Initialize items as an empty list

    def add_item(self, title, price, quantity=1):  # Accept title, price, and optional quantity
        total_cost = price * quantity
        self.total += total_cost
        self.last_transaction = total_cost
        self.items.append((title, price, quantity))  # Add tuple of (title, price, quantity) to the list of items

    def apply_discount(self):
        if self.discount > 0:
            discount_decimal = self.discount / 100
            self.total -= self.total * discount_decimal
            print(f"After the discount, the total comes to ${self.total:.2f}.")  # Print success message
            return self.total
        else:
            return "No discount applied"

    def void_last_transaction(self):
        if self.items:  # Check if there are items to void
            voided_item = self.items.pop()  # Remove the last item from the list
            self.total -= voided_item[1] * voided_item[2]  # Subtract the total cost of the voided item from the total
            self.last_transaction = 0
        else:
            return "No items to void"





