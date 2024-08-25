from __future__ import print_function

import logging

import grpc
import generated.weatherservice_pb2
import generated.weatherservice_pb2_grpc


def run():
    cityname="Mountain View, CA, USA"
    print("Making call to weather-server over grpc...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = generated.weatherservice_pb2_grpc.weatherserviceStub(channel)
        response = stub.GetWeather(generated.weatherservice_pb2.RequestWeather(cityname=cityname))
    print("Weather data for {0} received: {1}".format(cityname,response.message))


if __name__ == "__main__":
    logging.basicConfig()
    run()