from app.extensions import DB


class User(DB.Model):
    user_id = DB.Column(DB.String(40), primary_key=True)
    first_name = DB.Column(DB.String(100))
    last_name = DB.Column(DB.String(100))
