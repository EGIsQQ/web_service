import base64
import hashlib
from flask_restx import abort
from datetime import UTC, datetime, timedelta
import calendar
import jwt
from constants import JWT_ALGORITHM, JWT_SECRET

class AuthService: 
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False): 
        print(f'Looking up {email}')
        user = self.user_service.get_by_email(email)

        if user is None: 
            abort(404)
        
        if not is_refresh:  
            if not self.user_service.compare_password(user.password, password): 
                abort(400)

        
        data = {
            'email': user.email,
            'name': user.name,
            'surname': user.surname,
            'favorite_genre': user.favorite_genre
        }
        
        min30 = datetime.now(UTC) + timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.now(UTC) + timedelta(minutes=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    
    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token.encode('utf-8'), key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get('email')

        return self.generate_tokens(email, None, is_refresh=True)
    
    
    