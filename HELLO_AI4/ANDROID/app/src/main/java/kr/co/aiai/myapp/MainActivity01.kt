package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView

class MainActivity01 : AppCompatActivity() {
    lateinit var tv:TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main01)
        tv = findViewById<TextView>(R.id.tv)
        var btn = findViewById<Button>(R.id.btn)
        btn.setOnClickListener{
            Log.d("gilsang","myclick")
            tv.text="Good Evening"
        }
    }

}