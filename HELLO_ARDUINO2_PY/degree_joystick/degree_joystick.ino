#include <Servo.h>

Servo sv_btm;
Servo sv_ar1;
Servo sv_ar2;
Servo sv_grp;

int SENSE = 1;

int val_btm = 90;
int val_ar1 = 90;
int val_ar2 = 90;
int val_grp = 90;

String inputString = "";      
bool stringComplete = false;  

void setup() {
	Serial.begin(9600);
	sv_btm.attach(8);
	sv_ar1.attach(9);
	sv_ar2.attach(10);
	sv_grp.attach(11);

	sv_btm.write(val_btm);
	sv_ar1.write(val_ar1);
	sv_ar2.write(val_ar2);
	sv_grp.write(val_grp);

  pinMode(13, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(200);
}

void loop(){
	int int_a0 = analogRead(A0);
	int int_a1 = analogRead(A1);
	int int_a3 = analogRead(A3);
	int int_a2 = analogRead(A2);
	
	//Serial.println("int_a0:"+String(int_a0));
	//Serial.println("int_a1:"+String(int_a1));
	//Serial.println("int_a3:"+String(int_a3));
	Serial.println("int_a2:"+String(int_a2));
  if (stringComplete) {
    if(inputString=="a\n"){
      val_ar2+=90;
    }
    if(inputString=="b\n"){
      val_ar2-=90;
    }
    inputString="";
    stringComplete = false;
  }
	if (int_a0 > 800) { 
		val_btm += SENSE;
	}
	if (int_a0 < 200) {
		val_btm -= SENSE;
	}
	val_btm = constrain(val_btm, 90-80, 90+80);

	if (int_a1 > 800) { 
		val_ar1 -= SENSE;
	}
	if (int_a1 < 200) {
		val_ar1 += SENSE;
	}
	val_ar1 = constrain(val_ar1, 90-60, 90+60);

	if (int_a3 > 800) { 
		val_ar2 += SENSE;
	}
	if (int_a3 < 200) {
		val_ar2 -= SENSE;
	}
	val_ar2 = constrain(val_ar2, 90-60, 90+60);

	if (int_a2 > 800) { 
		val_grp += SENSE;
	}
	if (int_a2 < 200) {
		val_grp -= SENSE;
	}
	val_grp = constrain(val_grp, 90, 90+50);

	sv_btm.write(val_btm);
	sv_ar1.write(val_ar1);
	sv_ar2.write(val_ar2);
	sv_grp.write(val_grp);

	delay(10);
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString+=inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

