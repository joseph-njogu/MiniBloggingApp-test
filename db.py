from pymongo import MongoClient
from bson.objectid import ObjectId


class Database:
    def __init__(self):
        # self.client = MongoClient(current_app.config['MONGODB_URI'])
        self.client = MongoClient('mongodb://127.0.0.1:27017/blog_collections')
        # self.db = self.client[current_app.config['MONGODB_DB']]
        self.db = self.client['blog_collections']
        self.users_collection = self.db['users']
        self.posts_collection = self.db['posts']

    def find_posts_by_author(self, author_id=None):
        try:
            if author_id:
                return list(self.posts_collection.find({"author_id": author_id}))
            else:
                return list(self.posts_collection.find())
        except Exception as e:
            print(f"Error inserting user: {e}")
            return []  # Return an empty list as a default in case of an error

    def insert_user(self, user_data):
        try:
            return self.users_collection.insert_one(user_data)
        except Exception as e:
            print(f"Error inserting user: {e}")
            return []

    def find_user_by_username(self, username):
        try:
            return self.users_collection.find_one({"username": username})
        except Exception as e:
            print(f"Error finding user: {e}")
            return []

    def insert_post(self, post_data):
        try:
            return self.posts_collection.insert_one(post_data)
        except Exception as e:
            print(f"Error inserting post: {e}")
            return []

    def find_post_by_id(self, post_id):
        try:
            return self.posts_collection.find_one({"_id": ObjectId(post_id)})
        except Exception as e:
            print(f"Error finding post: {e}")
            return []

    def update_post(self, post_id, updated_data):
        try:
            return self.posts_collection.update_one({"_id": ObjectId(post_id)},
                                                    {"$set": updated_data})
        except Exception as e:
            print(f"Error updating post: {e}")
            return None

    def delete_post(self, post_id):
        try:
            return self.posts_collection.delete_one({"_id": ObjectId(post_id)})
        except Exception as e:
            print(f"Error deleting post: {e}")
            return None