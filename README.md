# Smart_farming

## Problem Statement:

 <p style = "color :#16DE2A;">Propose an IOT system to sense VOCs for accurately predicting onset of pathogen attack on the plant. A network on VOC sensor, temperature, humidity (soil), light, O2/CO2 can be deployed on the farm. In the project, these above mentioned sensor will be interfaced and deployed on an experimental farm (plants). Response to any stress introduced will be recorded via change in temperature, humidity & VOC levels of the plants.</p>
	
## Motivation
<p style = "color :#16DE2A;">Our IoT system addresses the critical challenge of timely pathogen detection in crops, aiming to revolutionize agriculture. Traditional methods often fail to provide early indicators, leading to significant economic losses. By integrating VOC sensors with temperature, humidity, light, and gas sensors, we offer a holistic approach for comprehensive plant health monitoring. The deployment on an experimental farm enables real-time data collection, refining our understanding of environmental parameters and stress responses. This innovative solution empowers farmers with timely information, enhancing crop resilience, reducing losses, and contributing to the sustainability of global food production.</p>

## Sensors 
`DHT(11)` :   
Temperature & Humidity (Range: Temp -> 0 - 50 C ; Humidity -> 20% to 90%)

Working Principle : The DHT11 is a temperature and humidity sensor that operates by measuring changes in resistance of a humidity-sensitive element(polymer) and built in thermistor in response to temperature and humidity variations. It converts these changes into digital signals for microcontrollers to read.​

Humidity-Sensitive Resistor (Polymer): The resistance of a humidity-sensitive resistor, often made of polymers, decreases with increasing humidity. As humidity increases, the polymer absorbs moisture, causing its conductivity to increase and, consequently, lowering its resistance.

Thermistor (Temperature-Sensitive Resistor): The resistance of a thermistor decreases with increasing temperature. Thermistors are designed to have a negative temperature coefficient (NTC), meaning their resistance decreases as the temperature rises. This characteristic makes them suitable for temperature sensing applications.

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

`LDR Sensor`:<br>
<p>It works on the principle of photoconductivity.Whenever the light falls on its photoconductive material, it absorbs its energy and the electrons of that photoconductive material in the valence band get excited and go to the conduction band,thus conductivity increases,resistivity decreases.Hence increase in light intensity results to decrease in resistance.We get the resistance value as the output.the range for ldr sensor is (0-1000)ohm.
we are displaying the reading in light_intensity(0-100) calculated by</p>
<p>light_intensity=(1000-sensor.output)/10</p>
<p>light_intensity=0 means dark and light_intensity=100 means maximum light intensity</p>

## Implementation

## How To Use ?

## Web Pages

## Data Collection

## Analysis


## Credits
