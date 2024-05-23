import requests

def weather(city, API_KEY):
    try:
        we_result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
        if we_result['cod'] != 200:
            return {"error": we_result.get("message", "Error fetching data")}
        
        we_data = {
            "temp": f"{we_result['main']['temp'] - 273.15:.2f} ℃",
            "pressure": str(we_result['main']['pressure']),
            "humidity": str(we_result['main']['humidity']),
            "main":str( we_result['weather'][0]['main']).lower(),
            "description": str(we_result['weather'][0]['description']).capitalize(),
            "wind_speed":str(we_result['wind']['speed']),
        }
        return we_data
    except Exception as e:
        return {"error": str(e)}