package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity03 : AppCompatActivity() {
    lateinit var tv:TextView
    lateinit var et_dan:EditText
    lateinit var et_disp:EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main03)
        var btn = findViewById<Button>(R.id.btn)
        tv = findViewById<EditText>(R.id.et_dan)
        et_dan = findViewById<EditText>(R.id.et_dan)
        et_disp = findViewById<EditText>(R.id.et_disp)

        btn.setOnClickListener{
            myclick()
        }


    }
    fun myclick(){
        var dan =Integer.parseInt(tv.getText().toString());
        var txt=""
        var tdan=dan.toString();
        for (i in 1..9) {
            var result = dan*i;
            txt+=tdan+"*"+i.toString()+"="+result.toString()+"\n";
        }
        et_disp.setText(txt);
    }

}