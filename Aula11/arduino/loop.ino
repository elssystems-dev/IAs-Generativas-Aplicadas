#define PINO 4

void setup() {
  Serial.begin(115200);
  pinMode(PINO, OUTPUT);
  digitalWrite(PINO, LOW);
}

void loop() {
  digitalWrite(PINO, HIGH);
  delay(1000);
  digitalWrite(PINO, LOW);
  delay(1000);
}