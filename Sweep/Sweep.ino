#include <Servo.h>

Servo servo1;
Servo servo2;
int pos = 0; 


void setup() {
  servo1.attach(9);  // attaches the servo on pin 9 to the servo object
  servo2.attach(6);
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  while(!Serial.available()){
    ;
  }
  Serial.read();
  delay(3000);
}

void loop() {
  pos = 0;
  servo1.write(pos);
  servo2.write(pos);
  delay(100);
  Serial.println(pos);
  while(!Serial.available()){
    ;
  }
  Serial.read();
//  if(Serial.available()){
//    Serial.println(Serial.read());
//    while(!Serial.available()){
//    digitalWrite(13,HIGH);
//    delay(500);
//    digitalWrite(13,LOW);
//    delay(500);
//    }
//  }
  delay(100);
  
  pos += 90;
  servo1.write(pos);
  servo2.write(pos);
  delay(100);
  Serial.println(pos);
  while(!Serial.available()){
    ;
  }
  Serial.read();
//  if(Serial.available()){
//    if(Serial.read() == 49) 
//    while(!Serial.available()){
//    continue;
//    }
//  }
  delay(100);
  pos += 90;
  servo1.write(pos);
  servo2.write(pos);
  delay(100);
  Serial.println(pos);
  while(!Serial.available()){
    ;
  }
  Serial.read();
//  if(Serial.available()){
//    Serial.println(Serial.read());
//    while(!Serial.available()){
//    continue;
//    }
//  }
  delay(100);
 
}
