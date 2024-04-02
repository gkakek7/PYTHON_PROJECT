package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView

class MainActivity02 : AppCompatActivity() {
    lateinit var tv:TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main02)
        var btn = findViewById<Button>(R.id.btn)
        tv = findViewById<TextView>(R.id.tv)
        btn.setOnClickListener{
            myclick()
        }


    }
    fun myclick(){
        var cnt = Integer.parseInt(tv.getText().toString());
        cnt--
        tv.text= cnt.toString();
    }

}