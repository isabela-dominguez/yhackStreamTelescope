#include <Servo.h>
Servo myservo;  // create servo object to control a servo

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  myservo.attach(9);
}
// the loop routine runs over and over again forever:
void loop() {
  //read from serial
  String command=Serial.readString();
  myservo.write(175);
  //if a command is found in the serial buffer 
  if (command.length()>0){
    myservo.write(90);
  }
  //output to serial monitor 
  
  delay(500);        // delay in between reads for stability
}

//void serialEvent() {
//}
