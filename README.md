# IOT ILKKM Sg Buloh (ThermoHygroSense) - Indoor Air Temperature & Humidity Smart ML Product [IBES](https://ibes.ilkkmsb.edu.my)

This repository is dedicated to another tutorial of our project in IOT Development for Healthcare Facilities Monitoring System (Smart HFMS). This equipment use MCU and industrial sensor to be used as monitoring devices for indoor air quality parameters namely as Temperature and Humidity. This project can be visualize using multiple Real-Time Dashboard:
1) [IBES](https://ths.ilkkmsb.edu.my/)
2) [Web Apps](https://ilkkmsb.streamlit.app)

You can find below the pipeline to develop a Similar project :

![Pipeline](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/logo.png?raw=true)


## [Python part](https://github.com/ismailsakdo/iot_ilkkmsb/tree/main/python)

This has been designed using SciKit-learn library for machine learning algorithm, testing, evaluation and development. This network has been trained on [dataset](https://drive.google.com/file/d/1RVnZ8bWAOIb6zj-c8u4W_f6DXKH8gKId/view?usp=sharing) collected via PhD research journey by Dr. Syazwan Aizat Ismail [UTM](https://github.com/ismailsakdo/iaqkkm)
Then this model has been exported into c code .h file. To convert the model we had used [tensorflow & keras](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb) python library.

## [Arduino part](https://github.com/ismailsakdo/iot_ilkkmsb/tree/main/arduino_logistic)

In this part I have used VS code and Arduino IDE to deploy the model onto the [ESP8266 WEMOS D1 mini lite](https://shopee.com.my/product/110910897/6506668056?gclid=Cj0KCQjwoeemBhCfARIsADR2QCvAm6SHw3rSFEKv2D6YZI35avUBvZwwjMw4xG5S5XS1iTIA9RsA2TQaAiijEALw_wcB). To do it we had to import our model, and the libraries to use I2C protocol and HDC1080 temperature and humidity sensor on the ESP8266. For the application that runs for the visualization and others, the link can be access below:

1) Link for [ILKKMSB](https://github.com/ismailsakdo/iot_ilkkmsb)
2) Link for [Web Apps ILKKMSB](https://github.com/ismailsakdo/ths_app)

Here is the schema of the wiring : 

![Wiring schema](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/circuit.png?raw=true)

To conclude by running the code with get an accuracy about 90% which is quite satisfiying.

## [Inforgraphic Development](https://ths.ilkkmsb.edu.my)

Let us learn the basic of the development using this steps. Interested to join us, [REGISTER HERE](https://spsshelper.wasap.my). There are 13 important steps (without) electronics discussion when to learn implementing this project. Before dive into this technical details, let us answer this [SURVEY](https://docs.google.com/forms/d/e/1FAIpQLSd_-rdpB3TI9kPT1e3keSa4b7VBOHB9cFocjUfOxjCgfh7MDw/viewform) to get the idea of the Sick Building Syndrome (SBS) that you possibly impacted due to poor indoor air quality/ indoor environmental quality. 

### Step 1 - Exploratory Data Analysis and Machine Learning Algorithm Testing
This chapter, the data from previous PhD research had been analyzed and use for identifying the suitable ML algorithm. Python module and Scikit-Learn library had been used.
![EDA and ML](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step1.png?raw=true)

### Step 2 - Machine Learning Model Evaluation, Hyperparameter Testing
This step, the data best algorithm set/ selected will be tested using hyperparameter approach. The best model will be further used in the ML convertion.
![ML Evaluation](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step2.png?raw=true)

### Step 3 - Visualization of The Tested Algorithm
This step, the data had been visualize using python based on selected algorithm and the producton of the windows applications/ computer applications for testing and validating purposes.
![Visualize and Window Apps](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step3.png?raw=true)

### Step 4 - Visualization of The Tested Algorithm & Algorithm Deployment
This is special steps where the ML algorithm had been deployed to ensure the use of the algorithm can be done across different platform around the world (WebApps Module). 
![Visualize and Cloud Deploy](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step4.png?raw=true)

### Step 5 - Convertion of the Model into C Language
In this ste, the model that had been produce, was converted into the C language for embedded technology applications. Arduino IDE and C++
![ML Convertion](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step5.png?raw=true)

### Step 6 - Programming the MCU with the ML
In this ste, we then prepare the electronics circuit and start programming the micro-controller (MCU) using ESP8266 and industrial sensors for measuring the IEQ parameters
![Arduino ML](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step6.png?raw=true)

### Step 7 - Adaptation of the ML Model in MCU
In this step, we include the machine learning model as C language in the sketch together with the model equation. This was done to ensure the output of the IEQ parameters (Temperature and Humidity) can successfuly predict the outcome based on ML model.
![Arduino ML Library](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step7.png?raw=true)

### Step 8 - Testing the Output from MCU
In this step, we test the output from the MCU by using the library and arduino sketch. Testing was also perform to calibrate/ verify the condition of the sensor and the predicted output.
![MCU Testing ML](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step8.png?raw=true)

### Step 9 - Cloud Computing and Records
In this step, we capture the data that had been read by the sensor (from ESP8266) and sent the data straight into the Google Clouds (using Google Apps Script). We use Google Sheets to store data in order to easily manipulate the Dashboard/ related applications.
![GS and Arduino](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step9.png?raw=true)

### Step 10 - Summarizing Record & Building Smart Applications
In this step, we convert the granular data into more manageable data sources to be utilized in Appsheet for analysis and creation of mobile apps. The mobile Apps was important to enable the engineers to record any problem related to mechanical ventilation system and their related components. 
![GS and Appsheet](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step10.png?raw=true)

### Step 11 - Appsheet and Report Generation
In this interesting step, the data from Google Sheet had been converted into representative condition by hours and date. Then the Mobile Applications was build using AppSheet to integrate with the investigation report development and inspection protocol. This help the engineers/ maintainance personnel to record any problem observed during operation of mechanical ventilation system. Automatic bot from Appsheet was used to generate report to be used as official document for record keeping and ML applications. Mobile Applications can be access [HERE](https://www.appsheet.com/start/ae4f326e-96f9-47cf-97a5-2cb82fe976d8?platform=desktop#viewStack[0][identifier][Type]=Control&viewStack[0][identifier][Name]=Temperature&appName=ThermoHygroSenseV2-744365623).
![Appsheet and Pdf](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step11.png?raw=true)

### Step 12 - LookerStudio and Dashboard Development
In this last steps, Google Data Studio or LookerStudio was integrate with the Google Sheet data. This enable the report generation mechanism much more efficient and robust.
![Looker and Appsheet](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step12.png?raw=true)

### Step 13 - Additional Web Apps For Analyst and Engineers
Additional approach was used to enable the data scientist and engineers to visualize and predict the outcome of the health events based on IEQ parameters namely as temperature and humidity. The application to visualize the real-time data is shown [HERE](https://ilkkmsb.streamlit.app/), and the application to predict the health events based on temperature and humidity setting can be found [HERE](https://ilkkmsbths.streamlit.app/).
![Streamlit](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/step13.png?raw=true)
