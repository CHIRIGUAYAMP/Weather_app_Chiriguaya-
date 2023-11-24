from flask import Flask, render_template
import requests 
from dotenv import load_dotenv, dotenv_values

config=dotenv_values('.env')


app = Flask (__name__)

def get_weather_data(city):   #funcion parametro ciudad - abre y copie
    API_KEY= config['API_KEY']
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    r= requests.get(url).json()
    print(r)
    return r    #retorna un json


@app.route('/prueba')
def prueba():
    #return get_weather_data('QUITO') cambio abajo por lo mismo 
    clima=get_weather_data('SANTA LUCIA') #el json esta en clima 
    #print(clima) imprime toddo el json  
    #print(clima.get('coord')) solo lo que pongo dentro de los parenteis 
    #return clima ['main'] veo todo lo del main o return clima.get('main')
    temperatura=str(clima['main']['temp'])
    descripcion=str (clima['weather'][0]['description'])
    icono=str (clima['weather'][0]['icon'])

    r_json={ #creacion del json 
            'ciudad':'SANTA LUCIA',
            'temperatura': temperatura,
            'descripcion': descripcion,
            'icono': icono
        }
    return render_template('weather.html',clima=r_json)
    #return str (clima['weather'][0]['description'])#tengo un diccionario por eso la ubicacion del diccionario 0



@app.route('/CHIRI')
def CHIRI():
    return get_weather_data('QUITO')


@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/about')
def CHIRICV():
    return render_template ("CHIRICV.html")

@app.route('/clima')
def clima():
    return 'Obten la informacion del clima'

if __name__== '__main__':
    app.run(debug=True)