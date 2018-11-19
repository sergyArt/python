import sys
import sqlite3
import csv

def csv_writer(data,path):
    with open(path,'w',newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def json_writer(path, data):
    with open(path, 'w') as json_file:
        for line in data:
            json_file.write(str(line))

def work_with_bd(query,params=None):
    try:
        conn = sqlite3.connect('weather.db')
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




if len(sys.argv) >=3 and (sys.argv[1] in ('--csv', '--json', '--html') and len(sys.argv[2]) > 0):
    data_list = []
    data_list.append(('id_city', 'city', 'date_create', 'temperature', 'id_weather'))
    for line in work_with_bd('''select * from weather_data'''):
        if len(sys.argv) > 3:
            if line[1] == sys.argv[3]:
                data_list.append(line)
        else:
            data_list.append(line)
    if len(data_list) == 1:
        print('Такой город не найден')
        raise SystemExit(0)
    if sys.argv[1] == '--csv':
        csv_writer(data_list, sys.argv[2])
    elif sys.argv[1] == '--json':
        my_list =[]
        fieldsnames = data_list[0]
        for values in data_list[1:]:
            inner_dict = dict(zip(fieldsnames, values))
            my_list.append(inner_dict)
        json_writer(sys.argv[2], my_list)
    elif sys.argv[1] == '--html':
        template_start = '''
            <html>
            <head>
            <title> Weather data </title>
            </head>
            <body>
            <table border="1">
            <tr>
            <td> City Id </td>
            <td> City Name </td>
            <td> Date </td>
            <td> Temperature </td>
            <td> Weather Id </td>
                    '''
        template_finish = '''
            </table>
            </body>
            </html>
        '''
        template_data = '''
            <tr>
            <td> {id} </td>
            <td> {name} </td>
            <td> {date} </td>
            <td> {temp} </td>
            <td> {weather} </td>
            </tr>
        '''
        with open(sys.argv[2], 'w') as html_file:
            html_file.write(template_start)
            for i in data_list[1:]:
                html_file.write(template_data.format(id=i[0], name=i[1], date=i[2], temp=i[3], weather=i[4]))
            html_file.write(template_finish)
else:
    print('Введены неверные параметры. Задайте строку с аргументами вида: export_openweathermap.py --csv | --json | --html filename [city]')

