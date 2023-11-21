# Smart_farming

## Problem Statement:

 <p style = "color :#16DE2A;">Propose an IOT system to sense VOCs for accurately predicting onset of pathogen attack on the plant. A network on VOC sensor, temperature, humidity (soil), light, O2/CO2 can be deployed on the farm. In the project, these above mentioned sensor will be interfaced and deployed on an experimental farm (plants). Response to any stress introduced will be recorded via change in temperature, humidity & VOC levels of the plants.</p>

## Motivation

## Sensors 
`DHT(11)` :  Temperature & Humidity (Range: Temp -> 0 - 50 C ; Humidity -> )
Working Principle :
- 


## Implementation
The implementation of the project had various phases including sensor integration, data collection and web design and statistical analysis.

- The sensors are integrated to a Mango plant using a breadboard and were connected to the ESP32  
- The ESP32 (microcontroller) was connected to the Thingspeak as well as to OM2M for send data to store and retrieve for the usage  
- ESP32 is using the MQTT protocol to connect and transfer the data to the thingspeak and HTTP protocol is used to send data to OM2M and to send alerts to the website.
- Threasholds are declared for some plants and stored in the database to monitor the following plants according to their threashold values.
- Alert Mechanism is implemented by the ESP32 sending the alerts to the database of the website. The recent alert is verified before adding the same alert inorder to reduce the load to teh website.
- The data is monitored from the thingspeak and OM2M sent from the sensors and was displayed in the dashboard.
- Finally the project implements the required functionalities like statistical analysis, circuits and history, settings etc


## How To Use ?
- The setup of the circuit should as following:


## OM2M
The OM2M is provided as folder such that the setup should be run from the ecllipse/in-cse/
./start.bat or ./start.sh

### Website Usage:
To use the website, the user should register an account giving the required info, or can use by default provided login details in the login page to test the web

The user can change the preference of their plant monitoring. He can edit the number of readings that should be plotted for the statistics plots for every sensor.

The website is responsive and user friendly such that it can be explored at [greenplant](greenplant.pythonanywhere.com) website.

## Web Pages

## Analysis


## Credits
Dileepkumar Adari
Revanth Reddy
Karthikeya Chaganti
Gajawada Bharath

