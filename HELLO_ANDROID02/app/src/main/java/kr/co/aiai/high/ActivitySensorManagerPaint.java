package kr.co.aiai.high;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.SensorListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class ActivitySensorManagerPaint extends AppCompatActivity implements SensorListener {
    TextView tv;
    SensorManager sensormanager;
    ViewMe viewme;
    float[] values = new float[6];
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        viewme = new ViewMe(this);
        setContentView(viewme);
        sensormanager = (SensorManager) getSystemService(SENSOR_SERVICE);
    }
    @Override
    protected void onResume() {
        sensormanager.registerListener(this, SensorManager.SENSOR_ALL);
        super.onResume();
    }
    @Override
    protected void onPause() {
        sensormanager.unregisterListener(this);
        super.onPause();
    }
    @Override
    public void onSensorChanged(int sensor, float[] values) {
        if (sensor == SensorManager.SENSOR_ORIENTATION) {
            String text = "";
            this.values[0] = values[0];
            this.values[1] = values[1];
            this.values[2] = values[2];
            this.values[3] = values[3];
            this.values[4] = values[4];
            this.values[5] = values[5];
            viewme.invalidate();
        }
    }

    @Override
    public void onAccuracyChanged(int i, int i1) {

    }

    private class ViewMe extends View {

        public ViewMe(Context context) {
            super(context);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setTextSize(40);
            paint.setStrokeWidth(10);
            paint.setColor(Color.RED);
            canvas.drawLine(100 + 20 * 0, 100 + values[0] * 3, 100 + 20 * 0, 200, paint);
            canvas.drawLine(100 + 20 * 1, 100 + values[1] * 3, 100 + 20 * 1, 200, paint);
            canvas.drawLine(100 + 20 * 2, 100 + values[2] * 3, 100 + 20 * 2, 200, paint);
            canvas.drawLine(100 + 20 * 3, 100 + values[3] * 3, 100 + 20 * 3, 200, paint);
            canvas.drawLine(100 + 20 * 4, 100 + values[4] * 3, 100 + 20 * 4, 200, paint);
            canvas.drawLine(100 + 20 * 5, 100 + values[5] * 3, 100 + 20 * 5, 200, paint);

            paint.setColor(Color.BLUE);
            canvas.drawText(values[0] + "", 50, 300, paint);
            canvas.drawText(values[1] + "", 50, 300 + 40, paint);
            canvas.drawText(values[2] + "", 50, 300 + 80, paint);
            canvas.drawText(values[3] + "", 50, 300 + 120, paint);
            canvas.drawText(values[4] + "", 50, 300 + 160, paint);
            canvas.drawText(values[5] + "", 50, 300 + 200, paint);

            super.onDraw(canvas);
        }

    }
}