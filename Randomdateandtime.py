import random 
from datetime import datetime, timedelta
def get_random_date(start_date, end_date):
    start = datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.strptime(end_date, "%m/%d/%Y")
    delta = (end-start).days
    random_days = random.randint(0, delta)
    random_date = start + timedelta(days=random_days)
    return random_date.strftime("%m/%d/%Y")
print("Random Date=", get_random_date("01/01/2016","12/12/2018"))