
String inputString = "";      
bool stringComplete = false;  

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(200);
}

void loop() {
  if (stringComplete) {
    if(inputString=="a\n"){
      digitalWrite(13, HIGH);
    }
    if(inputString=="b\n"){
      digitalWrite(13, LOW);
    }
    inputString="";
    stringComplete = false;
  }
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
