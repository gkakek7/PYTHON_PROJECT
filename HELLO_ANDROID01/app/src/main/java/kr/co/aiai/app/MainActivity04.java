package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity04 extends AppCompatActivity {
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main04);

        btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }
    void myclick(){
        int[] arr=new int[45];

        for(int i=0;i<arr.length;i++){
            arr[i]=i;
        }
        for(int i=0;i<100000;i++){
            int rnd=(int)((Math.random()*arr.length-1)+1);
            int temp=arr[0];
            arr[0]=arr[rnd];
            arr[rnd]=temp;
        }

        TextView[] tvarr={findViewById(R.id.tv1),findViewById(R.id.tv2),findViewById(R.id.tv3),findViewById(R.id.tv4),
                findViewById(R.id.tv5),findViewById(R.id.tv6)
        };
        for(int i=0;i<tvarr.length;i++) {
            for(int j=0;j<tvarr.length;j++) {
                int a=arr[i];
                int b= arr[j];
                if(a<b) {
                    arr[i]=b;
                    arr[j]=a;
                }
            }
        }


        for(int i=0;i<tvarr.length;i++){
            tvarr[i].setText(""+arr[i]);
        }

    }
}