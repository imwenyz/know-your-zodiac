import datetime
from models import EastZodiac, WestZodiac
import sys

west_zodiacs = [(120, 'capricorn'), (218, 'aquarius'), (320, 'pisces'), (420, 'aries'), (521, 'taurus'),
           (621, 'gemini'), (722, 'cancer'), (823, 'leo'), (923, 'virgo'), (1023, 'libra'),
           (1122, 'scorpio'), (1222, 'sagitarius'), (1231, 'capricorn')]

east_zodiacs = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'goat', 'monkey', 'rooster', 'dog', 'pig']

def get_zodiac_api(year, month, day, url_root):

    try:
        date = datetime.date(year, month, day)
    except:
        errInfo = str(sys.exc_info()[1])
        print "Error, datatime issue" + errInfo
        return {"error": errInfo}

    eastZodiac = get_east_zodiac(date.year)
    westZodiac = get_west_zodiac(date.month, date.day)
    ez = EastZodiac.query.filter_by(name=eastZodiac['name']).first()
    wz = WestZodiac.query.filter_by(name=westZodiac['name']).first()
    eastZodiac['imageurl'] = url_root + ez.image
    westZodiac['imageurl'] = url_root + wz.image

    return {"birthday" : {"year": date.year, "month": date.month, "day": date.day}, "eastZodiac" : eastZodiac, "westZodiac" : westZodiac}

def get_east_zodiac(year):
    num = (int(year)+8) % 12
    return {"number" : num+1, "name" : east_zodiacs[num]}

def get_west_zodiac(month, day):
    date_number = int("".join((str(month), '%02d' % day)))
    for z in west_zodiacs:
        if date_number <= z[0]:
            return {"number" : z[0]/100, "name" : z[1]}
