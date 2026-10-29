
const int LED_PIN = LED_BUILTIN;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ON") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED ON");
    } else if (command == "OFF") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED OFF");
    }
  }
}
