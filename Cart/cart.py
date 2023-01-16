from Products.models import Product


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get('cart')

        if not self.cart:
            self.cart = self.session['cart'] = {}


    def __repr__(self):
        return str(self.cart)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].get_final_price() * item['quantity']
            yield item

    def add(self, product, quantity:int, replace_current_quantity):

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        elif not replace_current_quantity:
            self.cart[product_id]['quantity']+=quantity
        self.save()
        

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    
    def save(self):
        self.session.modified = True


    def clear(self):
        del self.session['cart']
        self.save()


    def get_total_price(self):
       
        return sum(item['total_price'] for item in self)


    def is_empty(self):
        if self.cart:
            return False
        return True