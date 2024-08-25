# python-grpc-weather-microservice
This is a simple client-server microservice that demonstrates GRPC using python  
## Introduction
This code demonstrates GRPC in python in its simplest form, while making sense of how it can be used. Here, we use it in a microservice architecure. 

## How it works
1. The server listens on port 50051 on GRPC protocol.
2. The client makes a call to the server over 50051 on either localhost or on a remote host.
3. Variables to be exchanged are statically defined in the weatherservice.proto  file.  Both client and server need this same file.
4. GetWeather (RequestWeather) returns (ResponseWeather). Both are strings.
5. The server receives the request from the client, in this case the RequestWeather string is "Mountain View, CA", and the server does its job, making a external REST API call to get the real time weather info.
6. Server sends the ResponseWeather, also a string, back to the client.

Run the Server
```
python weather-server.py 
Server started, listening on 50051
```
Run the client
```
$ python weather-client.py 
Making call to weather-server over grpc...
Weather data for Mountain View, CA, USA received: The weather is 77.0!
```
   

## How to setup
1. Install required modules from requirements.txt
2. Run the compile-proto.sh which will read the .proto file and generate codes under generated directory.
3. Run server and the client. 
