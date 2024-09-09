class Invoice:
    """
    This class is only responsible for managing invoice details,
    such as items and calculating the total price.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item: str, price: float):
        """
        Adds an item to the invoice.
        """
        self.items.append((item, price))

    def total_price(self):
        """
        Calculates the total price of all items in the invoice.
        """
        return sum([item[1] for item in self.items])


class InvoicePrinter:
    """
    This class is only responsible for printing the invoice details.
    It does not manage the invoice data itself.
    """

    def print_invoice(self, invoice: Invoice):
        """
        Prints the invoice items and the total price.
        """
        for item in invoice.items:
            print(f"Item: {item[0]}, Price: {item[1]}")
        print(f"Total: {invoice.total_price()}")


class InvoiceSaver:
    """
    This class is only responsible for saving the invoice to the database.
    It does not handle invoice creation or printing.
    """

    def save_to_db(self, invoice: Invoice):
        """
        Saves the invoice to the database.
        """
        print(f"Invoice with total {invoice.total_price()} saved to the database.")


# Example usage of the classes
invoice = Invoice()
invoice.add_item("Laptop", 1200.0)
invoice.add_item("Mouse", 25.0)

# Printing the invoice
printer = InvoicePrinter()
printer.print_invoice(invoice)

# Saving the invoice to the database
saver = InvoiceSaver()
saver.save_to_db(invoice)

# output:
# Item: Laptop, Price: 1200
# Item: Mouse, Price: 25
# Total: 1225
# Invoice with total 1225.0 saved to the database.
