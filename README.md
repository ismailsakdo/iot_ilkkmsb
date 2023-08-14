# IOT ILKKM Sg Buloh (ThermoHygroSense) - Indoor Air Temperature & Humidity Smart ML Product [IBES](https://ibes.ilkkmsb.edu.my)

This repository is dedicated to another tutorial of our project in IOT Development for Healthcare Facilities Monitoring System (Smart HFMS). This equipment use MCU and industrial sensor to be used as monitoring devices for indoor air quality parameters namely as Temperature and Humidity. This project can be visualize using multiple Real-Time Dashboard:
1) [IBES](https://ths.ilkkmsb.edu.my/)
2) [Web Apps](https://ilkkmsb.streamlit.app)

You can find below the pipeline to develop a Similar project :

![Pipeline](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/logo.png?raw=true)


## [Python part](https://github.com/BaptisteZloch/MakeIT-How-to-deploy-SK-learn-model-on-ESP8266/tree/master/Python%20notebook)

This has been designed using SciKit-learn library for machine learning algorithm, testing, evaluation and development. This network has been trained on [dataset](https://drive.google.com/file/d/1RVnZ8bWAOIb6zj-c8u4W_f6DXKH8gKId/view?usp=sharing) collected via PhD research journey by Dr. Syazwan Aizat Ismail [UTM](https://osf.io/b4xsw/)
Then this model has been exported into c code .h file. To convert the model we had used [tensorflow & keras](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb) python library.

## [Arduino part](https://github.com/BaptisteZloch/MakeIT-How-to-deploy-SK-learn-model-on-ESP8266/tree/master/Arduino%20code/MAKEIT_SKlearn_Orientation_spot)

In this part I have used VS code and Arduino IDE to deploy the model onto the [ESP8266 WEMOS D1 mini lite](https://shopee.com.my/product/110910897/6506668056?gclid=Cj0KCQjwoeemBhCfARIsADR2QCvAm6SHw3rSFEKv2D6YZI35avUBvZwwjMw4xG5S5XS1iTIA9RsA2TQaAiijEALw_wcB). To do it we had to import our model, and the libraries to use I2C protocol and HDC1080 temperature and humidity sensor on the ESP8266. For the application that runs for the visualization and others, the link can be access below:

1) Link for [ILKKMSB](https://github.com/ismailsakdo/iot_ilkkmsb)
2) Link for [Web Apps ILKKMSB](https://github.com/ismailsakdo/ths_app)

Here is the schema of the wiring : 

![Wiring schema](https://github.com/ismailsakdo/iot_ilkkmsb/blob/main/Assets/circuit.png?raw=true)

To conclude by running the code with get an accuracy about 90% which is quite satisfiying.
