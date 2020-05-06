import os
import subprocess
basedir = os.path.dirname(__file__)

class Config(object):
    SECRET_KEY = 'NOT_SO_SECRET'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if 'DYNO' in os.environ:
        print('loading wkhtmltopdf path on heroku')
        WKHTMLTOPDF_CMD = subprocess.Popen(
            ['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')],
            stdout=subprocess.PIPE).communicate()[0].strip()
    else:
        print('loading wkhtmltopdf path on localhost')
        WKHTMLTOPDF_CMD = os.path.join(basedir + "\\app\\static\\executables\\bin\\", "wkhtmltopdf.exe")