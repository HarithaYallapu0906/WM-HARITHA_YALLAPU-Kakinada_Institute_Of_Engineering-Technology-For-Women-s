 SMART CITY BIN NETWORK  
[Virtual IoT Design Challenge]

---

## Abstract
This project proposes a **low-cost Smart Bin Network** using Internet of Things (IoT) technology to monitor waste levels in different regions. The system uses sensors to measure bin fill levels and transmits real-time data to a central server for monitoring and analysis.  

Key features include:  
- Area-wise bin identification  
- Reliable communication mechanisms and redundancy techniques  
- Separate monitoring for wet and dry waste  
- Efficient waste collection and optimized routing  

The proposed solution reduces operational costs, improves overall waste management efficiency, and is suitable for global deployment, even under extreme environmental conditions such as cyclones.

## Problem Statement
Traditional waste management systems operate on **fixed schedules** without considering actual bin fill levels. This leads to:  
- Overflowing bins in some areas  
- Unnecessary collection in others  
- Inefficient use of manpower, fuel, and time  

Challenges in existing smart waste systems include:  
- Sensor inaccuracies under adverse weather (rain, strong winds, etc.)  
- Communication failures  
- Lack of area-wise monitoring and separate handling of wet/dry waste  

**Need:** A low-cost, reliable, and scalable smart bin monitoring system providing accurate real-time information and ensuring efficient waste collection across different regions.





## Components Used

### Hardware
- Arduino Mega 2500 – Microcontroller to read sensor data and process it  
- Ultrasonic Sensor HC-SR04 – Measures the distance to garbage for fill-level detection  
- ESP8266 (ESP-01) Wi-Fi Module – Sends real-time data from bins to the server  
- Dustbins – Separate for wet and dry waste  
- Breadboard – For prototyping and connections  
- Jumper Wires – To connect sensors and modules  

### Software
- Arduino IDE – For writing and uploading code to Arduino  
- Python – For data processing and filtering (optional backend)  
- React JS – Web dashboard for real-time monitoring and visualization  
- Server / Cloud Platform – To store, process, and visualize data

## System Architecture

### 1. Smart Bins
- Each bin is equipped with IoT sensors and a microcontroller.  
- Sensors measure bin fill levels and classify them as **Empty, Partially Filled, or Fully Filled**.  
- Wet and dry waste bins are monitored separately to ensure accurate readings.  

### 2. Communication Module
- Data from bins is transmitted via **Wi-Fi, LoRa, or GSM** depending on area coverage.  
- **Local data buffering** ensures no data loss during network failures.  

### 3. Central Server / Cloud
- Receives and stores data from all bins.  
- Processes data to filter out false readings and generate alerts.  
- Maintains **area-wise bin identification** and historical data.  

### 4. Dashboard / Authority Interface
- Visualizes real-time bin status.  
- Sends alerts to authorities when bins reach threshold levels.  

### 5. Garbage Collection Trucks
- Receive notifications and **optimized collection routes**.  
- Update bin status on the server after collection.  

![Smart-City-Bin-Network-Architecture](SMARTBIN/readme/docs/architecture.png)
---


Working:

The Smart Bin uses ultrasonic sensors to monitor the height of garbage in any dustbin. Ultrasonic sensors are placed on the interior side of the lid of each dustbin. The HC-SR04 ultrasonic sensor is a 4-pin module, whose pin names are Vcc, Trigger, Echo and Ground respectively. The module has two eyes like projects in the front which forms the Ultrasonic transmitter and Receiver. The Ultrasonic transmitter transmits an ultrasonic wave which travels in air and when it strikes any material, it gets reflected back towards the sensor. This reflected wave is observed by the Ultrasonic receiver module as shown in the picture below.

![ultrasonic-sensor-working](https://user-images.githubusercontent.com/17234130/40727592-d07c9e80-6445-11e8-82fb-a636e6c5967a.png)

The circuitry inbuilt on the module calculates the time taken for the ultrasonic wave to come back. Now, the speed of sound in air is known. Using the simple formula Distance = Speed * Time, the amount of garbage in the dustbin is calculated.

As trash increases, the distance between the sensor and the dustbin decreases. This live data is sent to the microcontroller. The microcontroller then processes the data and using the ESP8266 WiFi module, it sends the data to the server. Once the amount of garbage in each dustbin is available to the server, the dustbin that requires attention is determined by considering the level of garbage. If the level of garbage in any dustbin exceeds a particular threshold (considered 75% here), it is alerted so that the dustbin can be cleaned.

Instructions for Use:

1. Download and install the Arduino IDE  
2. Make all necessary hardware connections as per the circuit diagram  
3. Compile and upload the Arduino code to the microcontroller  
4. Power the system and monitor bin status on the dashboard  


![img_20180318_173939](https://user-images.githubusercontent.com/17234130/40727614-dce7b506-6445-11e8-941e-d92ca7f9ccd3.jpg)

![img_20180318_181521_hdr](https://user-images.githubusercontent.com/17234130/40727661-fcbbe064-6445-11e8-9cec-24b56c02d584.jpg)


**Power Management Plan**

Since bins may be battery-powered, the following energy-saving techniques are used:

1.Periodic sensing: Sensor readings are taken at fixed intervals (e.g., every 10–15 minutes)

2.Deep sleep mode: Microcontroller enters sleep mode when inactive

3.Low-power communication: Data is transmitted only when significant level change occurs

4.Event-based alerts: Continuous transmission is avoided unless threshold is crossed

These methods significantly extend battery life and ensure long-term operation.


**Reliability & Fault Handling**
Handling False Readings

False readings may occur due to plastic blockage, uneven waste, rain, or vibrations.
To handle this:

Multiple readings averaging is used instead of a single reading

Outlier filtering ignores sudden abnormal values

Time-based confirmation: Bin must remain full for consecutive readings before alert

Wet & dry bins monitored separately to avoid mixed sensor interference

**Redundancy / Calibration Mechanisms**

Redundant sensing logic using historical data comparison
Initial calibration during installation to set empty-bin baseline
Periodic recalibration after garbage collection
Local data buffering during network failures
This improves accuracy and system reliability.


**Scalability & Network Considerations**
Handling 100+ Bins Across Zones

Each bin has a unique bin ID and zone ID
Data is stored area-wise on the server
Cloud-based backend supports large-scale data handling
Dashboard filters bins by zone, status, and priority

Network Topology
**Star topology is preferred:**

Bins communicate directly with a gateway/cloud
Easier to manage, scalable, and low maintenance
Mesh topology can be used in remote areas for redundancy
The system is designed to scale easily from small areas to city-wide deployment.
![Best-Tpopolgy-Example](SMARTBIN/readme/BestTopolgy.jpeg)

