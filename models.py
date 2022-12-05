from run import db
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    #def hash_password(self, password):
    #    self.password_hash = generate_password_hash(password)
    #def verify_password(self, password):
    #    return check_password_hash(self.password_hash, password)
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password_hash
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
    def __repr__(self):
        return '<User %r>' % self.username
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


