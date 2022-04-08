import requests
import psycopg2
import json
import time
while(True):
#this program will call the free weather APIs to receive the temperature data in the degree centigrade
	weather_data=requests.get('https://api.openweathermap.org/data/2.5/weather?lat=20.3880&lon=78.1292&appid=6967a112420d4a7027cddcba2a87189f&units=metric')
#print(weather_data.text)
	a_list=weather_data.json()
#print(a_list)
#print(type(a_list))
#print(a_list['main'])
	new_dict=dict(a_list['main'])
#print(new_dict)
	print(new_dict['temp'])
	a=(float)(new_dict['temp'])
	b=(float)(a_list['dt'])
	print(a_list['dt'])
	conn=psycopg2.connect(database="weather_data",user="postgres",password="missionbegins@",host="127.0.0.1",port="5432")
#python3 -m venv weather_data
#source weather_data/bin/activate
	conn.autocommit = True
	cursor = conn.cursor()
#cursor.execute('''INSERT INTO TEMPERATURE(VALUE,TIMESTAMP)VALUES (%d,%f)'''[a,b])
	cursor.execute("INSERT INTO TEMPERATURE VALUES (%s, %s)", (a,b))
	conn.commit()
	print("records inserted")
	time.sleep(100)
	conn.close()
