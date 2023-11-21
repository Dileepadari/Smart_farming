# Smart_farming

## Problem Statement:

 <p style = "color :#16DE2A;">Propose an IOT system to sense VOCs for accurately predicting onset of pathogen attack on the plant. A network on VOC sensor, temperature, humidity (soil), light, O2/CO2 can be deployed on the farm. In the project, these above mentioned sensor will be interfaced and deployed on an experimental farm (plants). Response to any stress introduced will be recorded via change in temperature, humidity & VOC levels of the plants.</p>
	
## Motivation
<p style>Our IoT system addresses the critical challenge of timely pathogen detection in crops, aiming to revolutionize agriculture. Traditional methods often fail to provide early indicators, leading to significant economic losses. By integrating VOC sensors with temperature, humidity, light, and gas sensors, we offer a holistic approach for comprehensive plant health monitoring. The deployment on an experimental farm enables real-time data collection, refining our understanding of environmental parameters and stress responses. This innovative solution empowers farmers with timely information, enhancing crop resilience, reducing losses, and contributing to the sustainability of global food production.</p>

## Sensors 
`DHT(11)` :   
Temperature & Humidity (Range: Temp -> 0 - 50 C ; Humidity -> 20% to 90%)

Working Principle :   
- The DHT11 is a temperature and humidity sensor that operates by measuring changes in resistance of a humidity-sensitive element(polymer) and built in thermistor in response to temperature and humidity variations. It converts these changes into digital signals for microcontrollers to read.​
- Humidity-Sensitive Resistor (Polymer): The resistance of a humidity-sensitive resistor, often made of polymers, decreases with increasing humidity. As humidity increases, the polymer absorbs moisture, causing its conductivity to increase and, consequently, lowering its resistance.
- Thermistor (Temperature-Sensitive Resistor): The resistance of a thermistor decreases with increasing temperature. Thermistors are designed to have a negative temperature coefficient (NTC), meaning their resistance decreases as the temperature rises. This characteristic makes them suitable for temperature sensing applications.

`Soil Moisture`: 

Working Principle : 
- The Soil Moisture sensor uses capacitance to measure dielectric permittivity of the surrounding medium to measure the soil moisture.
- In soil the dielectric permittivity is function of water content.When water content increases the dielectric permittivity also increase.So when dielectric permittivity is high then the Voltage measured across the `Soil Moisture` pins decreases.

`SGP30` :    
CO<sub>2</sub> and VOC  

Working Principle : 
- SGP30 uses Metal-oxide semiconductor to detect various gases.The sensor has MOX(Metal Oxide) and ASIC(Application Specific Integrated Circuit).
- `SGP30` mainly measures the concentrations of CO<sub>2</sub> and TVOCs.The MOX sensor reacts to the presence of these gases ,causing changes in it's electric conductivity.
- The ASIC then converts these changes into digital signals , which are used to calculate the gas concentrations.

`LDR Sensor`:   

- The LDR sensor operates on the principle of photoconductivity. When exposed to light, its photoconductive material absorbs energy, causing electrons to move from the valence band to the conduction band. This transition increases conductivity and decreases resistivity, resulting in a measurable decrease in resistance within the range of 0 to 1000 ohms.
- For clarity, we convert the sensor's resistance output to a light intensity value using the formula:
            Light Intensity = 10(1000 - Sensor Output)
            
- This formula produces a light intensity reading between 0 and 100. A light intensity of 0 indicates darkness, while 100 signifies maximum light intensity. This conversion allows for a precise interpretation of the sensor's output in relation to the prevailing light conditions.

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
- The setup of the circuit circuit should as following:
<div style="display: flex;justify-content: space-around;">
<img src="https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/circ.jpeg" width="40%" alt="circuit 1"><br>
<img src="https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/circuit.jpeg" width="50%"alt="circuit 2">
</div>  

## OM2M
The OM2M is provided as folder such that the setup should be run from the eclipse-om2m-v1-4-1/in-cse/start.sh


### Website Usage:
To use the website, the user should register an account giving the required info, or can use by default provided login details in the login page to test the web

The user can change the preference of their plant monitoring. He can edit the number of readings that should be plotted for the statistics plots for every sensor.

The website is responsive and user friendly such that it can be explored at [greenplant](greenplant.pythonanywhere.com) website.

## Web Pages
- Home Page : Consists of the current values of sensors and Plot of VOC values​  

![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/home.jpeg)   
    

- Statistics Page : Consists of Graphs of sensor data retrieved from Thingspeak.​  

![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/stat.jpeg)    
     

- Analysis Page : Consists threshold values of each sensor for the Plant selected by the user and the current values of each sensor. ​   
     
![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/analysis.jpeg)    
       
     
- Circuit Page : Consists of the entire circuit diagram of the system.​     
       
![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/circuit.jpeg)     
       
      
- History Page : Here the user can select Dates in which they want to see the sensor data generated between the timeline.     ​
      
![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/history.jpeg)     
      
      
- Alerts Page : When the current values of the sensors are not in the range of threshold values an alert is generated and is shown in Alerts Page.     
    
     
![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/alerts.jpeg)     
     

- About Page : Consists of the information of the project and team members.​   
    
![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/about.jpeg)    
     

- Settings Page : Here the user can make certain changes:​   
    - The user can choose the number of values for observation in the Statistics Page.​
    - The user can change Plant and if the Plant is present in the Database then the corresponding Threshold values are shown in the Analysis Page.   

![Graph image](https://github.com/Dileepadari/Smart_farming/tree/main/project_photos/settings.jpeg)  
     

## Analysis
- Graphs for shown in the Statistics page of the website of each sensor.The data obtained is Analysed and compared with the Threshold value of the selected plant.The Status shown in Analysis page is based on the values of Threshold values and Current values.     

## Important links
- [Website link](http://greenplant.pythonanywhere.com/)   
- [file_to_start_OM2M](https://github.com/Dileepadari/Smart_farming/blob/main/eclipse-om2m-v1-4-1/in-cse/start.sh)    
- [Arduino_code](https://github.com/Dileepadari/Smart_farming/blob/main/Arduino/ESW_Project.ino)                                                                                            

## Credits
Dileepkumar Adari    
Revanth Reddy    
Karthikeya Chaganti    
Gajawada Bharath    

@ Copyright Aakashavani

