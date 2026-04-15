#define PINO 4

String comando = ""; // str
void setup() {
  Serial.begin(115200);
  pinMode(PINO, OUTPUT);
  digitalWrite(PINO, LOW);
}

void loop() {
  while(Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      comando.trim();

      if (comando == "LIGAR") {
        digitalWrite(PINO, HIGH);
        Serial.println("Pino 4 LIGADO");
      } else if (comando == "DESLIGAR"){
        digitalWrite(PINO, LOW);
        Serial.println("Pino 4 DESLIGADO");
      } else {
        Serial.println("Comando inválido");
      }
      comando = "";
    } else {
      comando += c;
    }
  }
}
