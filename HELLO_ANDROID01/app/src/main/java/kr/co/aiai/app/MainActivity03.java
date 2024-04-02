package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity03 extends AppCompatActivity {
    Button btn;
    EditText et_dan;
    EditText et_disp;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main03);
        btn=findViewById(R.id.btn);
        et_dan=findViewById(R.id.et_dan);
        et_disp=findViewById(R.id.et_disp);
        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
               myclick();
            }
        });
    }
    void myclick(){
        int dan = Integer.parseInt(""+et_dan.getText());
        String txt="";
        for(int i=1;i<=9;i++){
            txt+=dan+"*"+i+"="+(dan*i)+"\n";
        }

        et_disp.setText(txt);
    }
}