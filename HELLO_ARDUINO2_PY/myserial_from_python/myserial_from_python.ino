String s;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    char c;
    c = Serial.read();
    if(c == '\n'){
      if(s == "on"){
        digitalWrite(13,HIGH);
        s="";
      }else if(s == "off"){
        digitalWrite(13,LOW);
        s="";
      }else{
        s="";
      }
    }else{
      s += c;
    }
  }
}
