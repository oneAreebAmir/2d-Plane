#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

void setup() {
  // Initialize Serial communication
  Serial.begin(115200);

  // Initialize I2C communication
  Wire.begin();

  // Initialize ADXL345 accelerometer
  if(!accel.begin())
  {
    Serial.println("ADXL345 not found!");
    while(1);
  }
}

void loop() {
  // Read the X, Y, and Z axis values from the accelerometer
  sensors_event_t event;
  accel.getEvent(&event);
  float x = event.acceleration.y;
  float y = event.acceleration.x;
  float z = event.acceleration.z;

  // Print the X, Y, and Z axis values
  Serial.print("X:");
  Serial.print(x);
  Serial.print(",Y:");
  Serial.print(y);
  Serial.print(",Z:");
  Serial.println(z);

  delay(10); // Wait for 500 milliseconds
}
