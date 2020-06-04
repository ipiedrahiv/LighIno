int data;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 8 as an output.
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  digitalWrite (8, 0);
  // initial message for python/arduino coordination
  Serial.println("Hello! How are you Python?");
}

// the loop function runs over and over again forever
void loop() {
  // Reads the information written by python
  while(Serial.available()){
    data = Serial.read();
  }

  Serial.println(data);

  if (data == '1'){
    digitalWrite (8, 1);		//Turns ON the led
  }else if (data == '0'){
    digitalWrite (8, 0);                //Turn OFF the Led
  }

}
