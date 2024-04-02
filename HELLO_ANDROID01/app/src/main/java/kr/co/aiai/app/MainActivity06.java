package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity06 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main06);

        Button btn=findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }
    void myclick(){
        EditText first=findViewById(R.id.et_first);
        EditText last=findViewById(R.id.et_last);

        String firstt= String.valueOf(first.getText());
        String lastt= String.valueOf(last.getText());

        int ifirst=Integer.parseInt(firstt);
        int ilast=Integer.parseInt(lastt);
        String txt="";
        for(int i=ifirst;i<=ilast;i++){
            for(int j=ifirst;j<ifirst+i;j++){
                txt+="*";
            }
            txt+="\n";
        }
        EditText et_disp=findViewById(R.id.et_disp);

        et_disp.setText(txt);

    }
}