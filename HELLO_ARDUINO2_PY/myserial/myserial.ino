int a = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("babo"+String(a));
  a++;
}
