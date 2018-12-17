#include <Arduino.h>
#include <ArduinoOTA.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

/************
 Well, then you have a choice - you can either fully disable interrupts while writing out led data by putting the line:

#define FASTLED_ALLOW_INTERRUPTS 0
before you #include <FastLED.h>. Sometimes, especially on the esp8266, you might have better luck by just tweaking the re-try attempt code with:

#define FASTLED_INTERRUPT_RETRY_COUNT 1
*************/
#define FASTLED_ESP8266_DMA // better control for ESP8266 will output or RX pin requires fork https://github.com/coryking/FastLED
#define FASTLED_ALLOW_INTERRUPTS 0  // Reduce flickering
#include "FastLED.h"

/************ Network Information (CHANGE THESE FOR YOUR SETUP) ************************/
const char* ssid = "HalcyonWifi"; //"Gegenueber vom Kuenstlereingang";
const char* password = "HalcyonPassword";//"OrangeViolin056";

const char* sensor_name = "HalcyonTower02";
const char* ota_password = "HalcyonPassword";

const bool static_ip = true;
IPAddress ip(192, 168, 100, 105);
IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 0);

const int udp_port = 7778;

/*********************************** FastLED Defintions ********************************/
#define NUM_LEDS      120
#define DATA_PIN      5
//#define CLOCK_PIN   2
#define CHIPSET       WS2812B
#define COLOR_ORDER   GRB

/*********************************** Globals *******************************************/
WiFiUDP port;
CRGB leds[NUM_LEDS];

/********************************** Start Setup ****************************************/
void setup() {
  Serial.begin(115200);

  // Setup FastLED
  #ifdef CLOCK_PIN
    FastLED.addLeds<CHIPSET, DATA_PIN, CLOCK_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  #else
    FastLED.addLeds<CHIPSET, DATA_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  #endif

  // Setup the wifi connection
  setup_wifi();

  // Setup OTA firmware updates
  setup_ota();

  // Initialize the UDP port
  port.begin(udp_port);
}

void setup_wifi() {
  delay(10);

  Serial.println();
  Serial.print("Connecting to ");
  Serial.print(ssid);

  if (static_ip) {
    WiFi.config(ip, gateway, subnet);
  }
  
  WiFi.hostname(sensor_name);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup_ota() {
  ArduinoOTA.setHostname(sensor_name);
  ArduinoOTA.setPassword(ota_password);

  ArduinoOTA.onStart([]() {
    Serial.println("Starting");
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
    else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
    else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
    else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
    else if (error == OTA_END_ERROR) Serial.println("End Failed");
  });
  ArduinoOTA.begin();
}

void loop() {

  if (WiFi.status() != WL_CONNECTED) {
    delay(1);
    Serial.print("WIFI Disconnected. Attempting reconnection.");
    setup_wifi();
    return;
  }
  
  ArduinoOTA.handle();

  // TODO: Hookup either a more elaborate protocol, or a secondary
  // communication channel (i.e. mqtt) for functional control. This
  // will also give the ability to have some non-reative effects to
  // be driven completely locally making them less glitchy.

  // Handle UDP data
  int packetSize = port.parsePacket();
  if (packetSize == sizeof(leds)) {
    port.read((char*)leds, sizeof(leds));
    Serial.printf(".");
    FastLED.show();
    // flush the serial buffer
    while(Serial.available()) { Serial.read(); } 
  } else if (packetSize) {
    Serial.printf("Invalid packet size: %u (expected %u)\n", packetSize, sizeof(leds));
    port.flush();
    return;
  } else {
    Serial.printf("~");
  }
}
