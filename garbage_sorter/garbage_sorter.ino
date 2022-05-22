//libraries
#include <Stepper.h>
#include <Servo.h>
#include <SR04.h>

int stepsPerRevolution = 2048;
int motSpeed = 10;
int numSteps = 683;

#define servoPin 6

#define trigPin2 4
#define echoPin2 5

#define trigPin1 2
#define echoPin1 3

Servo servo;

SR04 USSensor1 = SR04(echoPin1, trigPin1);
SR04 USSensor2 = SR04(echoPin2, trigPin2);

int USVal1 = 0, USVal2 = 0;
String usval1, usval2;


Stepper stepper(stepsPerRevolution, 8, 9, 10, 11);
String InBytes;


void setup() {
  Serial.begin(9600);
  stepper.setSpeed(motSpeed);
  servo.attach(servoPin);
  servo.write(90);
}

void loop(){
  if(Serial.available()>0){
//    Serial.write("recognizes");
    USVal1 = USSensor1.Distance();
    Serial.println(USVal1);
    InBytes = Serial.readStringUntil('\n');
    // if garbage is detected it will execute the code below
    Serial.println(InBytes);
    if(InBytes == "GARBAGE"){
      // moves the stepper motor shaft so the person can throw their garbage in
      stepper.step(stepsPerRevolution);
//      Serial.write("stepper");
      
      // moves the slide to aim at the garbage bin
      servo.write(57);
//      Serial.write("servo");
      
      // while nothing is put in the garabge it will keep checking 
      check_garbage();
      
      // once something has been detected it will move the stepper motor shaft to close the opening 
      delay(1000);
//      Serial.write("starting");
      stepper.step(-stepsPerRevolution);   
      servo.write(90);

      delay(500);
      USVal1 = USSensor1.Distance();
      if(USVal1 < 18){
        Serial.println("g full");
      }
      else{
        Serial.println("not full");
      }
  }

    // if recycling is detected it will execute the code below
    if(InBytes == "RECYCLING"){
      // moves the stepper motor shaft so the person can throw their recycling in
      stepper.step(stepsPerRevolution);
//      Serial.write("stepper");
      
      // moves the slide to aim at the recycling bin
      servo.write(123);
//      Serial.write("servo");
      
      // while nothing is put in the recycling bin it will keep checking 
      check_recycling();
      
      // once something has been detected it will the stepper motor shaft to close the opening 
      delay(1000);
      stepper.step(-stepsPerRevolution);   
      servo.write(90);

      delay(500);
      USVal2 = USSensor2.Distance();
      if(USVal2 < 18){
        Serial.println("r full");
      }

      else{
        Serial.println("not full");
      }
      
    }
    
  }

  if(InBytes == "done"){
    stepper.step(stepsPerRevolution - numSteps);
  }
}


void check_garbage(){
  USVal1 = USSensor1.Distance();
  while(USVal1 >= 18){
    USVal1 = USSensor1.Distance();
    usval1 = String(USVal1);
    Serial.println(usval1); 
  }
  if(USVal1 < 18){
    usval1 = String(USVal1);
    Serial.println(usval1); 
    delay(250);
  }
}

void check_recycling(){
  USVal2 = USSensor2.Distance();
  while(USVal2 >= 18){
    USVal2 = USSensor2.Distance();
    usval2 = String(USVal2);
    Serial.println(usval2); 
  }
  if(USVal2 < 18){
    usval2 = String(USVal2);
    Serial.println(usval2); 
    delay(250);
  }
 }
