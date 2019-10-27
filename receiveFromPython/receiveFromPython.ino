#include <Servo.h>
Servo tiltServo;
Servo panServo; // create servo object to control a servo
int panServoPin = 10;
int panDegree = 90;
int tiltServoPin = 9;
int tiltDegree = 90;
void setup()
{
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  tiltServo.attach(tiltServoPin);
  panServo.attach(panServoPin);
}
// the loop routine runs over and over again forever:
void loop()
{
  int x;
  int y;
  //read from serial
  //if a command is found in the serial buffer
  if (Serial.available() > 0)
  {
    //read value
    String command = Serial.readStringUntil(';');
    //tiltServo.write(175);
    delay(500);
    //is it a move command?
  if (command == "move"){
      //get coordinates
      //tiltServo.write(135);
      delay(500);
      x =Serial.readStringUntil(';').toInt();
      y =Serial.readStringUntil(';').toInt();
      moveServo(x,y);
  }
  //output to servo motors
  }
  delay(100); // delay in between reads for stability
}

void moveServoRelative(int x, int y)
{
  panDegree += x;
  tiltDegree += y;
  panServo.write(panDegree);
  tiltServo.write(tiltDegree);
}
void moveServo(int x, int y)
{
  panDegree = x;
  tiltDegree = y;
  panServo.write(panDegree);
  tiltServo.write(tiltDegree);
}
//void serialEvent() {
//}
