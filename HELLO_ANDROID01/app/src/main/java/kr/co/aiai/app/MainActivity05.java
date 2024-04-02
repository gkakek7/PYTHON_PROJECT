package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity05 extends AppCompatActivity {
    TextView tv;
    String text="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main05);
        tv=findViewById(R.id.tv);
        Button[] btn={
                findViewById(R.id.btn1),findViewById(R.id.btn2),findViewById(R.id.btn3),
                findViewById(R.id.btn4),findViewById(R.id.btn5),findViewById(R.id.btn6),
                findViewById(R.id.btn7),findViewById(R.id.btn8),findViewById(R.id.btn9),
                findViewById(R.id.btn0)
        };
        Button btn_call=findViewById(R.id.btn_call);
        btn_call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mycall();
            }
        });
        for(Button b:btn){
            b.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    myclick(view);
                }
            });
        }
    }
    void myclick(View view){
        Button btn=(Button) view;
        String txt = (String)btn.getText();
        text+=txt;
        tv.setText(text);
    }
    void mycall(){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        Toast.makeText(this.getApplicationContext(),"calling\n"+text,Toast.LENGTH_SHORT).show();
//        builder.setTitle("알림").setMessage(text+"\n calling...").show();
    }
}