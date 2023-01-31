#include <AFMotor.h>
#include <Servo.h>

AF_DCMotor motor(1);
AF_DCMotor motor2(2);

Servo my_servo;


void setup() {
  //mstop();
  Serial.begin(9600);
  my_servo.attach (10);
  my_servo.write(90);

}

void loop() {
   if (Serial.available()) {  // check for incoming serial data
      char command = Serial.read();
      if (command == '1'){
        forward();
      }else if(command=='2'){
       back();
      }else if(command=='0'){
        mstop();
      }else if(command=='3'){
        stanga();
      }else if(command=='4'){
        dreapta();
      }else if(command=='5'){
        centru();
      }}

}

void stanga(){
  my_servo.write(0);
}

void dreapta(){
  my_servo.write(180);
}

void centru(){
  my_servo.write(90);
}

void forward(){
  motor.setSpeed(100);
  motor.run(FORWARD);
  motor2.setSpeed(100);
  motor2.run(FORWARD);
  
}

void back(){
  motor.setSpeed(100);
  motor.run(BACKWARD);
  motor2.setSpeed(100);
  motor2.run(BACKWARD);
}

void mstop(){
  motor.run(RELEASE);
  motor2.run(RELEASE);

}