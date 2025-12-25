void setup() {
  Serial.begin(9600);
}

void loop() {
  int binLevel = 80;  // example value (sensor reading)

  if (binLevel >= 75) {
    Serial.println("ALERT: Bin is Full");
  } else if (binLevel >= 30) {
    Serial.println("Bin is Partially Filled");
  } else {
    Serial.println("Bin is Empty");
  }

  delay(2000); // wait 2 seconds
}
