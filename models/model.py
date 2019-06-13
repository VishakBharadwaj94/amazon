from pymongo import MongoClient
from flask import session
from bson.objectid import ObjectId

client = MongoClient()
db = client['amazon']


def user_exists(username):
	query = {'username':username}
	result = db['users'].find_one(query)
	if bool(result):
		return result
	return False

def save_user(user_info):
	db['users'].insert_one(user_info)

def product_exists(name):
	query = {'product_name':name}
	result = db['products'].find_one(query)
	if bool(result):
		return result
	return False

def add_product(product_info):
	db['products'].insert_one(product_info)

def remove_product(product):
	query = {"product_name":product}	
	db['products'].remove(query)

def products_list():
	if session['type']=='buyer':

		products = db['products'].find({})
		return products
	query = {"seller":session['username']}	
	products = db['products'].find(query)
	return products


def add_to_cart(product_id):
	query = {"username":session['username']}
	action= {"$addToSet":{"cart":{"$each":[product_id]}}}
	db['users'].update(query,action)
	return True
	
def cart_items(username):
	query = {"username":session['username']}
	result = db['users'].find_one(query)
	cart = result['cart']

	cart_list = []
	total = 0
	for product_id in cart:
		query = {"_id":ObjectId(product_id)}
		result = db['products'].find_one(query)
		total+=result['price']
		cart_list.append(result)

	return cart_list,total	

def remove_from_cart(name):

	db['users'].update({"username":session['username']},{"$pull":{"cart":name}})


