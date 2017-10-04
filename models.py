from app import db
from passlib.apps import custom_app_context as pwd_context
import os

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column(db.String(15), unique=True , index=True)
    password = db.Column(db.String(15))
    tenancy_ocid = db.Column(db.String(128))
    user_ocid = db.Column(db.String(128))
    fingerprint = db.Column(db.String(128))
    private_key_path = db.Column(db.String(128))
    region = db.Column(db.String(50))

    def __init__(self, username, password, tenancy_ocid, user_ocid, fingerprint, private_key, region):
        self.username = username
        self.password = hash_password(password)
        self.tenancy_ocid = tenancy_ocid
        self.user_ocid = user_ocid
        self.fingerprint = fingerprint
        self.private_key_path =
        self.region = region

    def hash_password(self, pword):
        self.password = pwd_context.encrypt(pword)

    def verify_password(self, pword):
        return pwd_context.verify(pword, self.password)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException as e:
            print('exception occurred, rolling back db')
            print(str(e))
            db.session.rollback()


    def create_key_file(self, private_key):
        path = '/home/opc/.oci'
        filename = self.username + '.pem'

        if not os.path.exists(path):
            os.makedirs(path)

        try:
            if os.path.join(path,filename).exists():
                return
            with open(os.path.join(path, filename), 'wb') as key_file:
                key_file.write(buff)
        except BaseException e:
            print('Error: ' + str(e))
            return
        self.private_key_path = path + '/' + filename



#tenancy_ocid, user_ocid, fingerprint, private_key_path, region
