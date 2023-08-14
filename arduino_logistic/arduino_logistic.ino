#include "model_c.h" // Include the generated model header file
#include<Wire.h>
#include "ClosedCube_HDC1080.h"
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1

Adafruit_SSD1306 display(128, 64, & Wire, -1);
ClosedCube_HDC1080 hdc1080;

//------------- WiFi -----
const char* ssid = "iot_kdo@unifi"; //--> Your wifi name or SSID.
const char* password = "ismailsa2022"; //--> Your wifi password.
const char* host = "script.google.com";
const int httpsPort = 443;

WiFiClientSecure client; //--> Create a WiFiClientSecure object.
String GAS_ID = "AKfycbwe99Z1JAyDYnKa3dy0WypQdGTeEK9C7tEcFy1-DbyVAgH6DHWKLyj1C6Gkr_2lKVR-"; //--> spreadsheet script ID

//------ end of WiFi

// Define the minimum and maximum values for normalization
// Replace these placeholders with the actual values
const float MIN_LINEAR = -10.179950480801295 /* Your minimum value */;
const float MAX_LINEAR = 6.27804738856662 /* Your maximum value */;

float thi; float t; float h; String latlong = "1.5459771077916329,103.79077517258013"; String  statusthi;
float linear_combination_f; float probability_f; 

void setup() {
  Wire.begin();
  hdc1080.begin(0x40);
  Serial.begin(115200);

  //OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }
  delay(2000);
  display.clearDisplay();
  display.setTextColor(WHITE);
  Serial.println("PM25 found!");
  delay(1000);

  //WiFi
  WiFi.begin(ssid, password); //--> Connect to your WiFi router
  Serial.println("");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    //----------------------------------------Make the On Board Flashing LED on the process of connecting to the wifi router.
    digitalWrite(LED_BUILTIN, LOW);
    delay(250);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(250);
    //----------------------------------------
  }
  //----------------------------------------
  digitalWrite(LED_BUILTIN, HIGH); //--> Turn off the On Board LED when it is connected to the wifi router.
  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  //----------------------------------------
  Serial.println("I'm awake, but I'm going into deep sleep mode for 30 seconds");

  client.setInsecure();
}

float sigmoid(float x) {
  return 1.0 / (1.0 + exp(-x));
}

void loop() {
  float temperature = hdc1080.readTemperature();
  float humidity = hdc1080.readHumidity();

  // Perform prediction using the model weights and biases
  float linear_combination = layer_0_biases[0] +
                             layer_0_weights[0] * temperature +
                             layer_0_weights[1] * humidity;

  // Apply normalization to the linear combination
  linear_combination = (linear_combination - MIN_LINEAR) / (MAX_LINEAR - MIN_LINEAR);

  float probability = sigmoid(linear_combination);

  //THI
  float tf = ((temperature*1.8)+32); //convertion of the temperature into Farenhiet
  thi = (tf - (0.55-(0.55*humidity/100))*(tf-58));

  //final calibration based on algorithm ***THI****
  t = temperature; //Rsquare = 0.9999999125
  h = humidity; // Rqsuare = 0.9996

  //additional metrics
  linear_combination_f = abs(linear_combination);
  probability_f = probability*1000;

  Serial.print("Temperature: ");
  Serial.print(temperature, 2);
  Serial.print(" °C, Humidity: ");
  Serial.print(humidity, 2);
  Serial.print("%, Linear Combination: ");
  Serial.print(linear_combination, 4);
  Serial.print(" THI:");
  Serial.print(thi,0);  
  Serial.print(", Probability: ");
  Serial.println(probability, 4);

  Serial.print("Health Event: ");
  Serial.println(probability >= 0.5 ? "Yes" : "No");

  if(thi>80)
  {
    sendData1(); //--> Calls the sendData Subroutine
    }
  else
  {
    sendData2();    
  }
}


// Subroutine for sending data to Google Sheets SendData1
// float t, float h, float thi, int co2, int tvoc, int pm25, int pm10
void sendData1() {
  Serial.println("==========");
  Serial.print("connecting to ");
  Serial.println(host);

  //----------------------------------------Connect to Google host
  if (!client.connect(host, httpsPort)) {
    Serial.println("connection failed");
    return;
  }
  //----------------------------------------

  //----------------------------------------Processing data and sending data
  String string_t =  String(t);
  String string_h =  String(h);
  String string_thi =  String(thi);
  String statusthi = "Poor";
  String string_latlong = "1.5459771077916329,103.79077517258013";
  
  String url = "/macros/s/" + GAS_ID + "/exec?temperature=" + string_t + "&humidity=" + string_h + 
  "&thi=" + string_thi + "&status=" + statusthi + "&latlong=" + string_latlong;

  Serial.print("requesting URL: ");
  Serial.println(url);

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "User-Agent: BuildFailureDetectorESP8266\r\n" +
               "Connection: close\r\n\r\n");

  Serial.println("request sent");
  //----------------------------------------

  //----------------------------------------Checking whether the data was sent successfully or not
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    if (line == "\r") {
      Serial.println("headers received");
      break;
    }
  }
  String line = client.readStringUntil('\n');
  if (line.startsWith("{\"state\":\"success\"")) {
    Serial.println("esp8266/Arduino CI successfull!");
  } else {
    Serial.println("esp8266/Arduino CI has failed");
  }
  Serial.print("reply was : ");
  Serial.println(line);
  Serial.println("closing connection");
  Serial.println("==========");
  Serial.println();
  //---------------------------------------- 


     //display on OLED LCD
  delay(500);
  display.clearDisplay();

  // display temperature
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.print("ThermoHygroSense");
  display.setTextSize(1);
  display.setCursor(0, 10);
  display.print("====================");
  display.setTextSize(1);
  display.setCursor(0, 20);
  display.print("Temp [C] & Hum [%]");
  display.setTextSize(1.5);
  display.setCursor(0, 30);
  display.print(t);
  display.print(" ");
  display.setTextSize(1);
  display.cp437(true);
  display.write(167);
  display.setTextSize(1);
  display.print("C ");
  display.setTextSize(1.5);
  display.setCursor(60, 30);
  display.print(h);
  display.print(" %");

  //display THI and Status
  display.setTextSize(1.5);
  display.setCursor(0, 40);
  display.print("THI:");
  display.setTextSize(1.5);
  display.setCursor(20, 40);
  display.print(thi);
  display.print(" ");
  display.setTextSize(1.5);
  display.setCursor(60, 40);
  display.print("STAT:");
  display.setTextSize(1.5);
  display.setCursor(90, 40);
  display.print(statusthi);

  //display LR and Prob
  display.setTextSize(1.5);
  display.setCursor(0, 50);
  display.print("LC:");
  display.setTextSize(1.5);
  display.setCursor(20, 50);
  display.print(linear_combination_f);
  display.print(" ");
  display.setTextSize(1.5);
  display.setCursor(60, 50);
  display.print("PROB:");
  display.setTextSize(1.5);
  display.setCursor(90, 50);
  display.print(probability_f);
  display.print("");


  display.display();

  delay(1000);
}

//====== Send Data 2 for option No. 2
void sendData2() {
  Serial.println("==========");
  Serial.print("connecting to ");
  Serial.println(host);

  //----------------------------------------Connect to Google host
  if (!client.connect(host, httpsPort)) {
    Serial.println("connection failed");
    return;
  }
  //----------------------------------------

  //----------------------------------------Processing data and sending data
  String string_t =  String(t);
  String string_h =  String(h);
  String string_thi =  String(thi);
  String statusthi = "Good";
  String string_latlong = "1.5459771077916329,103.79077517258013";
  
  String url = "/macros/s/" + GAS_ID + "/exec?temperature=" + string_t + "&humidity=" + string_h + 
  "&thi=" + string_thi + "&status=" + statusthi + "&latlong=" + string_latlong;


  Serial.print("requesting URL: ");
  Serial.println(url);

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "User-Agent: BuildFailureDetectorESP8266\r\n" +
               "Connection: close\r\n\r\n");

  Serial.println("request sent");
  //----------------------------------------

  //----------------------------------------Checking whether the data was sent successfully or not
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    if (line == "\r") {
      Serial.println("headers received");
      break;
    }
  }
  String line = client.readStringUntil('\n');
  if (line.startsWith("{\"state\":\"success\"")) {
    Serial.println("esp8266/Arduino CI successfull!");
  } else {
    Serial.println("esp8266/Arduino CI has failed");
  }
  Serial.print("reply was : ");
  Serial.println(line);
  Serial.println("closing connection");
  Serial.println("==========");
  Serial.println();
  //---------------------------------------- 

     //display on OLED LCD
  delay(500);
  display.clearDisplay();

  // display temperature
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.print("ThermoHygroSense");
  display.setTextSize(1);
  display.setCursor(0, 10);
  display.print("====================");
  display.setTextSize(1);
  display.setCursor(0, 20);
  display.print("Temp [C] & Hum [%]");
  display.setTextSize(1.5);
  display.setCursor(0, 30);
  display.print(t);
  display.print(" ");
  display.setTextSize(1);
  display.cp437(true);
  display.write(167);
  display.setTextSize(1);
  display.print("C ");
  display.setTextSize(1.5);
  display.setCursor(60, 30);
  display.print(h);
  display.print(" %");

  //display THI and Status
  display.setTextSize(1.5);
  display.setCursor(0, 40);
  display.print("THI:");
  display.setTextSize(1.5);
  display.setCursor(20, 40);
  display.print(thi);
  display.print(" ");
  display.setTextSize(1.5);
  display.setCursor(60, 40);
  display.print("STAT:");
  display.setTextSize(1.5);
  display.setCursor(90, 40);
  display.print(statusthi);

  //display LR and Prob
  display.setTextSize(1.5);
  display.setCursor(0, 50);
  display.print("LC:");
  display.setTextSize(1.5);
  display.setCursor(20, 50);
  display.print(linear_combination_f);
  display.print(" ");
  display.setTextSize(1.5);
  display.setCursor(60, 50);
  display.print("PROB:");
  display.setTextSize(1.5);
  display.setCursor(90, 50);
  display.print(probability_f);
  display.print("");

  display.display();

  delay(1000);
}
