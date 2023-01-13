


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get('cart')

        if not self.cart:
            self.cart = self.session['cart'] = {}

    def add(self, product, quantity, replace_current_quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        elif not replace_current_quantity:
            self.cart[product_id]['quantity']+=quantity
        self.save()
        print(self.cart)

    def save(self):
        self.session.modified = True