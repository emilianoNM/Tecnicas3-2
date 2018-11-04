const byte led = 11;
char cadena[30];
float valor=0;
byte posicion=0;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT); 
}


void loop() {
  
  while(valor==0){ 
    Serial.flush();
     if(Serial.available()){
      memset(cadena, 0,sizeof(cadena));
      while(Serial.available()>0){
        delay(5);
        cadena[posicion]=Serial.read();
        posicion++;
      }
      valor=atoi(cadena);//Convertimos la cadena de caracteres en enteros
      posicion=0;//Ponemos la posicion a 0
      }
  }
  if(valor>=0 && valor<=255){
    analogWrite(led, valor);
  }
  valor=0;
}

