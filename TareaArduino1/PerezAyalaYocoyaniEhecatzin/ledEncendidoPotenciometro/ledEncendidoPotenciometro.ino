const byte led = 11, potenciometro = A0;
int lectura = 0;
byte intensidad = 0;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(potenciometro, INPUT);
}

void loop() {
  lectura = analogRead(potenciometro);
  intensidad = map(lectura, 0, 1023, 0, 255);
  analogWrite(led, lectura);  
}
