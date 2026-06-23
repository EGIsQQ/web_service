from dao.model.users import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, payload):
        email = payload.get('email')
        user = self.session.query(User).filter_by(email=email).first()
        return user
    
    
    def update_user(self, user, user_d):
        for key, value in user_d.items():
            setattr(user, key, value)

        self.session.commit()
        self.session.refresh(user)
    
    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user, user_d):
        if user_d.get('name') is not None: 
            user['name'] = user_d.get('name')
        if user_d.get('surname') is not None: 
            user['surname'] = user_d.get('surname')
        if user_d.get('favorite_genre') is not None: 
            user['favorite_genre'] = user_d.get('favorite_genre')
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()

    def get_by_email(self, email): 
        return self.session.query(User).filter_by(email=email).first()
    
