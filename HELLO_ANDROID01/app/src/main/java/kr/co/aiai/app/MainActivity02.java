package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity02 extends AppCompatActivity {
    TextView tv = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main02);
        Log.d("aiai","안녕");
        Button btn = findViewById(R.id.btn);
        tv=findViewById(R.id.tv);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }
    void myclick(){
        Log.d("tookeon","myclcik");
        int cnt=Integer.parseInt((String)tv.getText());
        cnt--;
        tv.setText(String.valueOf(cnt));
    }
}