#include <Servo.h>

Servo servo_y;
Servo servo_x; 
int pos_x = 0;
int pos_y = 90;

void move(int pos_x,int Pos_x){
  for (pos_x; pos_x < Pos_x; pos_x += 1) {
      servo_x.write(pos_x);
      delay(15);
    }
    delay(1000);
  Serial.println(pos_x);
  while(!Serial.available()){
    ;
  }
  Serial.read();
  delay(1000);
}

void setup() {
  servo_y.attach(9);
  servo_x.attach(6);
  servo_x.write(0);
  Serial.begin(9600);
  delay(3000);  
  while(!Serial.available()){
    ;
  }
  Serial.read();
}

void loop() {
  int inc = 30;
  while(true){
    if(pos_x>=180){
      for (pos_x; pos_x > 0; pos_x -= 1) { 
        servo_x.write(pos_x);
        delay(15);
      }
    delay(1000);
    }
    move(pos_x,pos_x+inc);
    pos_x+=inc;
      
  }
}
