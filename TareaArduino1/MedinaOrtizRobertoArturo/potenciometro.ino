const int led =3;  
const int pot =0; 

int brillo; 

void setup ()  {
  Serial.begin(9600);
  pinMode (led, OUTPUT);  
}

void loop (){
  
  brillo = analogRead (pot) / 4; 
  Serial.println(brillo);
  analogWrite(led, brillo);
  delay(100);
}
