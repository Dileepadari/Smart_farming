# Smart_farming

## Problem Statement:

 <p style = "color :#16DE2A;">Propose an IOT system to sense VOCs for accurately predicting onset of pathogen attack on the plant. A network on VOC sensor, temperature, humidity (soil), light, O2/CO2 can be deployed on the farm. In the project, these above mentioned sensor will be interfaced and deployed on an experimental farm (plants). Response to any stress introduced will be recorded via change in temperature, humidity & VOC levels of the plants.</p>
	
## Motivation
<p style = "color :#16DE2A;">Our IoT system addresses the critical challenge of timely pathogen detection in crops, aiming to revolutionize agriculture. Traditional methods often fail to provide early indicators, leading to significant economic losses. By integrating VOC sensors with temperature, humidity, light, and gas sensors, we offer a holistic approach for comprehensive plant health monitoring. The deployment on an experimental farm enables real-time data collection, refining our understanding of environmental parameters and stress responses. This innovative solution empowers farmers with timely information, enhancing crop resilience, reducing losses, and contributing to the sustainability of global food production.</p>

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
	Light Intensity=(1000−Sensor Output)10Light Intensity=10(1000−Sensor Output)​
- This formula produces a light intensity reading between 0 and 100. A light intensity of 0 indicates darkness, while 100 signifies maximum light intensity. This conversion allows for a precise interpretation of the sensor's output in relation to the prevailing light conditions.

## Implementation

## How To Use ?

## Web Pages

## Data Collection

## Analysis


## Credits
