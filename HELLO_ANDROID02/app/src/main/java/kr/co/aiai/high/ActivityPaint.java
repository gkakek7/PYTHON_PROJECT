package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.View;

public class ActivityPaint extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView( new ViewMe(this));
    }

    private class ViewMe extends View {
        public ViewMe(Context context) {
            super(context);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            Paint paint = new Paint();
            paint.setColor(Color.RED);
            // paint.setAlpha(125);
//            Matrix matrix = new Matrix();
//            matrix.postRotate(45, 100, 100);
//            canvas.setMatrix(matrix);
            paint.setStrokeWidth(20);
            canvas.drawLine(0,50,300,50,paint);
            paint.setColor(Color.rgb(255,165,0));
            canvas.drawLine(0,150,300,150,paint);
            paint.setColor(Color.YELLOW);
            canvas.drawLine(0,250,300,250,paint);
            paint.setColor(Color.GREEN);
            canvas.drawLine(0,350,300,350,paint);
            paint.setColor(Color.BLUE);
            canvas.drawLine(0,450,300,450,paint);
            paint.setColor(Color.rgb(0, 0, 128));
            canvas.drawLine(0,550,300,550,paint);
            paint.setColor(Color.rgb(128,0,128));
            canvas.drawLine(0,650,300,650,paint);
            super.onDraw(canvas);
        }
    }
}
