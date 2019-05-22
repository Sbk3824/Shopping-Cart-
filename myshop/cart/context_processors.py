from .cart import Cart
"""
A context processor is a function that receives the request object as a parameter and 
returns a dictionary of objects 
that will be available to all the templates rendered using RequestContext
"""

def cart(request):
    return {'cart': Cart(request)}