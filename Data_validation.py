from sqlalchemy.orm import sessionmaker, scoped_session # SQL API
from sqlalchemy import create_engine # SQL API
from DB import *
import datetime


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
con = DBSession()

def validate_event_input(phone,y,m,d,name):
    error = None
    year  = int(y)
    month = int(m)
    day = int(d)
    try:
        datetime.date(year,month,day)
    except ValueError or NameError:
        error = 'Wring dates'
    if phone.isdigit() != True or len(str(phone)) != 10 :
                error = 'Invalid phone number'
    try:
        if datetime.date(year,month,day) < datetime.date.today():
            error = "Can't create events in the past"
    except ValueError or NameError:
        error = "Incorrect dates"
    it_exists = con.query(Events).filter_by(name=name).first()
    if it_exists:
        error = 'Event name already exists'
    if error:
        return error

w = validate_event_input(phone='9442599858',y=2016,m=112,d=6,name='R9')
if w == None:
    print 'kkkkkkkkkkk'
else:
    print w