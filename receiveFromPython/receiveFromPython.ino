#include <Servo.h>
Servo tiltServo;
Servo panServo; // create servo object to control a servo
int panServoPin = 10;
int panDegree = 90;
int tiltServoPin = 9;
int tiltDegree = 90;
String readString;

// create array
int incoming[2];

void setup()
{
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  tiltServo.attach(tiltServoPin);
  panServo.attach(panServoPin);
  
}
// the loop routine runs over and over again forever:
void loop()
{
  int x;
  int y; 
  //moveServo(150, 12);
  while(Serial.available() >=2){
    for (int i = 0; i < 2; i++){
      incoming[i] = Serial.read();
    }

    moveServo(incoming[0], incoming[1]);
    Serial.flush();
  }
  
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

