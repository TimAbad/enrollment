import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x1d\x1f@mC\xd5\x04@\xdb\xcd\xdf\xc0\x96\x98\x90\xdb'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    
