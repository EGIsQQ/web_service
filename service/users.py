from dao.users import UserDAO
from constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT, JWT_SECRET, JWT_ALGORITHM
import hashlib
import base64
import hmac
import jwt 


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user_info(self, token):
        try: 
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return self.dao.get_one(payload)
        except Exception as e: 
            return e, 401

    def create(self, user_d):
        if None in [user_d.get("email"), user_d.get("password"), user_d.get("name"), user_d.get("surname")]: 
            return '', 400
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_update_data, token):
        user = self.get_user_info(token)
        return self.dao.update_user(user, user_update_data)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password): 
        hash_digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_digest)
    
    def get_by_email(self, email): 
        return self.dao.get_by_email(email)

    def compare_password(self, password_hash, other_password): 
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS)

        return hmac.compare_digest(decoded_digest, hash_digest)
    
    def update_password(self, token, password_old, password_new): 
        user = self.get_user_info(token)
        real_password = user.password
        if self.compare_password(real_password, password_old): 
            new_password = self.get_hash(password_new)
            update_data = {"password": new_password}
            self.update(update_data, token)
        else:
            return 'Введен неверный пароль', 401
            
