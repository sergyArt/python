import json
import os
import sqlite3
from grab import Grab
import datetime
import time

file_bd = 'weather.db'
file_appid = 'app.id'
weather_data = None
file_cyties = 'city.list.json'

def get_appid():
    if os.path.isfile(file_appid):
        with open(file_appid,'r') as f:
            return f.read().replace('\n','')

def get_query(city_id=None, country=None, url=None):
    try:
        g = Grab(log_file='grab.log')
        g.setup(timeout=30, connect_timeout=30)
        g.go(url)
        return g.response.body
    except Exception as e:
        pass
        #print('Some error in grab [', str(e), ']')


def work_with_bd(query,params=None):
    try:
        conn = sqlite3.connect(file_bd)
        c = conn.cursor()
        if not params:
            c.execute(query)
        else:
            c.execute(query,params)
        conn.commit()
        row = c.fetchall()
        return row
    except Exception as e:
        print('Error in database level [', str(e), ']')
        raise SystemExit(1)
    finally:
        c.close()
        conn.close()

def update_bd():
    alredy_exists = []
    for row in work_with_bd('''select id_city from weather_data'''):
        alredy_exists.append(row[0])
    loads_bd(alredy_exists)

def loads_bd(mass_id = None):
    city_list = []
    with open(file_cyties,'r') as f:
        line = f.read()

    try:
        data = json.loads(line)
        for l in data:
            city_id = l['id']
            if (not mass_id) or (len(mass_id) >= 0 and city_id not in mass_id):
                city_name = l['name']
                weather_data = json.loads(get_query(city_id=city_id,url='http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'.format(city_id,get_appid())))
                temperature_data = json.loads(get_query(city_id=city_id,url='http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(city_id,get_appid())))
                if weather_data['cod'] == 200 and temperature_data['cod'] == 200:
                    date_weather = str(time.ctime(weather_data['dt']))
                    city_temp = temperature_data['main']['temp']
                    weather_id = weather_data['weather'][0]['id']
                    work_with_bd('insert into weather_data values(?,?,?,?,?);', [city_id, city_name, date_weather, city_temp, weather_id])
    except Exception as e:
        pass
        #print("Some error when load data [", str(e), ' ]')



print('Program weather in towns')
if not os.path.isfile(file_cyties):
    print('Not found file with cyties')
    raise SystemExit(1)
if os.path.isfile(file_bd):
    print('File bd is found. DB is update now.....')
    update_bd()
    print('Update finished')
else:
    print('File db is not found. DB is create now.....')
    work_with_bd('''create table weather_data (id_city integer primary key, city varchar(255), date_create date, temperature integer, id_weather integer);''')
    loads_bd()
    print('Create finished')


answer = input('Enter city name: ')
for row in work_with_bd('''select city from weather_data'''):
   if row[0] == answer:
       print("This city found!")
       answer1 = input('Do you want download weather new data? y/n ')
       if answer1 == 'y':
           city_id = work_with_bd('''select id_city from weather_data where city=?''', [answer])
           weather_data = json.loads(get_query(city_id=city_id, url='http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(city_id[0][0], get_appid())))
           temperature_city = weather_data['main']['temp']
           work_with_bd('update weather_data set temperature={} where id_city={}'.format(temperature_city, city_id[0][0]))














