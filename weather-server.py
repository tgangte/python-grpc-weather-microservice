from concurrent import futures
import logging
import requests

import grpc
import generated.weatherservice_pb2
import generated.weatherservice_pb2_grpc

from geopy.geocoders import Nominatim

weatherurl = "https://api.open-meteo.com/v1/forecast?current=temperature_2m&temperature_unit=fahrenheit&"

class Weather(generated.weatherservice_pb2_grpc.weatherserviceServicer):
    def GetWeather(self, request, context):
        return generated.weatherservice_pb2.ResponseWeather (message="The weather is %s!" % WeatherAPIcall(request.cityname))
    
def WeatherAPIcall(cityname): #This function makes a REST api call to a free weather service, it takes lat and long values
    #make a call to weather api
    latlong=cityToLatLong(cityname)
    r=requests.get(weatherurl+"latitude="+str(latlong[0])+"&longitude="+str(latlong[1])).json()
    temperature = r["current"]["temperature_2m"]
    return(temperature)

def cityToLatLong(cityname): #This function converts the city name into lat and long values
    geolocator = Nominatim(user_agent="Geopy Library")
    location = geolocator.geocode(cityname)
    return(location.latitude, location.longitude)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generated.weatherservice_pb2_grpc.add_weatherserviceServicer_to_server(Weather(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
