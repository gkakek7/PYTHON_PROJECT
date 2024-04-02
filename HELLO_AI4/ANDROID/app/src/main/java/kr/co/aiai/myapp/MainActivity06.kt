package kr.co.aiai.myapp

import android.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import kotlin.random.Random

class MainActivity06 : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main06)
        var btn = findViewById<Button>(R.id.btn)
        btn.setOnClickListener() {
            myclick()
        }

    }

    fun myclick() {
        var first = findViewById<EditText>(R.id.et_first)
        var last = findViewById<EditText>(R.id.et_last)
        var firstt=first.getText().toString()
        var lastt=last.getText().toString()

        var ifirst=Integer.parseInt(firstt)
        var ilast=Integer.parseInt(lastt)
        var txt=""
        for(i in ifirst until ilast){
            for(j in ifirst until ifirst+i){
                txt+="*"
            }
            txt+="\n"
        }

        var et_disp=findViewById<EditText>(R.id.et_disp)

        et_disp.setText(txt)
    }



}