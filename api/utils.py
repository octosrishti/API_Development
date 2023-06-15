import hashids

from django.conf import settings
import pandas as pd
import os
from datetime import datetime 

def slugify(id: int) -> str:
    hash = hashids.Hashids(
        salt=settings.HASHIDS_SALT,
        min_length=settings.HASHIDS_MIN_LENGTH,
        alphabet=settings.HASHIDS_ALPHABET,
    )
    return hash.encrypt(id)


def update_database():
    
    from .models import Market
    try:
        market_data_csv = pd.read_csv(os.path.join(os.getcwd(), "data.csv"))
        
        for indx, item in market_data_csv.iterrows():
            market_id = item["id"]
            date = item["date"]
            seats = item["seats"]
            amount = item["amount"]
            user = item["user"]
            software = item["software"]
            department = item["department"]
            
            dateList = date.split(" ")
            dateList = [dateList[0], dateList[1]]
            date = dateList.join(" ")
            
            date = datetime.strptime(date, "%y-%m-%d %H:%M:%S")
            
            Market.objects.create(market_id=market_id, date=date,seats=seats, amount=amount, user=user, software=software, department=department)
            
    except Exception as e:
        print(e)
        