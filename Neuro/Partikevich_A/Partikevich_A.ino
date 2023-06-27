#define EMG A0
#define ARRSIZE 10
int val = 0;
int noise = 0;
int max_v = 0;
int min_v = 255;
int ampl = 0;
int arr[ARRSIZE];
int smooth_ampl = 0;

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < ARRSIZE; i++) {
    arr[i] = 0;
  }

}

void loop() {
  for (int i=0; i<32; i++) {
    val = analogRead(EMG);
    val = map(val, 0, 1023, 0, 255);
    if (val > max_v) {
      max_v = val;
    }
    if (val < min_v) {
      min_v = val;
    }
  }
  ampl = (max_v - min_v)* 0.7 + ampl*0.3;
  max_v = 0;
  min_v = 255;
  for (int i = 0; i <= ARRSIZE-1; i++){
    arr[i] = arr[i+1];
  }
  arr[ARRSIZE-1] = ampl;

  for (int i=0; i<ARRSIZE; i++) {
    smooth_ampl += arr[i];
  }

  smooth_ampl = smooth_ampl/ARRSIZE;

// для битроника
//  Serial.write("A0");
//  Serial.write(val);
//  Serial.write("A2");
//  Serial.write(smooth_ampl);
  Serial.print("s");
  Serial.print(val);
  Serial.print(",");
  Serial.println(smooth_ampl);
  delay(3);

}
