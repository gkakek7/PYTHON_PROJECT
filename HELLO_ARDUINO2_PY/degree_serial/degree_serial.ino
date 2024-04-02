#include <Servo.h>

Servo sv_btm;
Servo sv_ar1;
Servo sv_ar2;
Servo sv_grp;

String s;

int SENSE = 1;

int val_btm = 90;
int val_ar1 = 90;
int val_ar2 = 90;
int val_grp = 90;


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


}

void loop(){
	
  if(Serial.available()>0){
    char c;
    c = Serial.read();
    if(c == '\n'){
      if(s == "on"){
    		sv_btm.write(120);
    		delay(10);
        s="";
      }else if(s == "off"){
    		sv_btm.write(60);
    		delay(10);
        s="";
      }else{
        s="";
      }
    }else{
      s += c;
    }
  }
	
}
