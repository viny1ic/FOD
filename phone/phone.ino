#include <Servo.h>

// DEFINE INITIAL VARIABLES
Servo servo_y;
Servo servo_x; 
int pos_x = 0;
int pos_y = 90;

// MOVE THE X SERVO TO THE SPECIFIED POSITION
void move(int pos_x,int Pos_x){
  for (pos_x; pos_x < Pos_x; pos_x += 1) {
      servo_x.write(pos_x);
      delay(15);
    }
    delay(1000);
  Serial.println(pos_x);

  // WAIT FOR INPUT FROM COMPUTER
  while(!Serial.available()){
    ;
  }
  // READ INPUT FROM COMPUTER
  Serial.read();
  delay(1000);
}

void setup() {
  // INITIALISE PINS ATTACHED TO SERVOS
  servo_y.attach(9);
  servo_x.attach(6);

  // SET POSITION OF SERVO X TO 0 DEGREE
  servo_x.write(0);
  
  // INITIALISE SERIAL COMMUNICATION AT BAUD RATE 9600
  Serial.begin(9600);
  delay(3000);  
  
  // WAIT FOR INPUT FROM COMPUTER
  while(!Serial.available()){
    ;
  }
  // READ INPUT FROM COMPUTER
  Serial.read();
}

void loop() {
  // AMOUNT OF ANGLE TO INCREASE IN ONE ITERATION
  int inc = 30;
  while(true){
    if(pos_x>=90){
      for (pos_x; pos_x > 0; pos_x -= 1) { 
        servo_x.write(pos_x);
        delay(15);
      }
    delay(1000);
    }
    
    // MOVE SERVO BY SPECIFIED DEGREES
    move(pos_x,pos_x+inc);
    pos_x+=inc;
      
  }
}
