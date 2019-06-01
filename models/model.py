from pymongo import MongoClient

client = MongoClient()
db = client['amazon']


def user_exists(username):
	query = {'username':username}
	result = db['users'].find(query)

	if result.count()>0:
		return True
	return False

def save_user(user_info):
	db['users'].insert_one(user_info)