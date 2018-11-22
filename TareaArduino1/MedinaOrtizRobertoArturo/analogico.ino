int led=3;

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("Introduzca un numero de 0 a 255:\n");
};

void loop()
{
  char cad[4];
  int i;
  if( Serial.available() > 0)
  {
    delay(5);
    for( i=0 ; Serial.available() > 0 ; i++ )
      cad[i] = Serial.read(); 
    cad[i] = '\0';     
    analogWrite(led, (byte)atoi(cad));
  }
}
