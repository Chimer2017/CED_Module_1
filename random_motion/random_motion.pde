int num = 2000;
int rangeA = 10;
int rangeB = 18;

float[] ax = new float[num];
float[] ay = new float[num];
float[] bx = new float[num];
float[] by = new float[num];

void setup()
{
  size(1000, 1000);
  for(int i = 0; i < num; i++) {
    ax[i] = width/2;
    ay[i] = height/2;
    bx[i] = width/2;
    by[i] = height/2;
   
  }
  frameRate(30);
}

void draw()
{
  background(random(0,255),random(0,255),random(0,255));

  for(int i = 1; i < num; i++) {
    ax[i-1] = ax[i];
    ay[i-1] = ay[i];
    bx[i-1] = bx[i];
    by[i-1] = by[i];
  }

  ax[num-1] += random(-rangeA, rangeA);
  ay[num-1] += random(-rangeA, rangeA);
  bx[num-1] += random(-rangeB, rangeB);
  by[num-1] += random(-rangeB, rangeB);


  // Constrain all points to the screen
  ax[num-1] = constrain(ax[num-1], 0, width);
  ay[num-1] = constrain(ay[num-1], 0, height);
  bx[num-1] = constrain(bx[num-1], 0, width);
  by[num-1] = constrain(by[num-1], 0, height);
 
  // Draw a line connecting the points
  for(int i=1; i<num; i++) {    
    float val = float(i)/num * 204.0 + 51;
    stroke(val);
    strokeWeight(5);
    line(ax[i-1], ay[i-1], ax[i], ay[i]);
    line(bx[i-1], by[i-1], bx[i], by[i]);
  }
}
