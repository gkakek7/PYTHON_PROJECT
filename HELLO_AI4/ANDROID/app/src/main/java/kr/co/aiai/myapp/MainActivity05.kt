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

class MainActivity05 : AppCompatActivity() {
    var text=""
    lateinit var tv:TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main05)
        tv=findViewById<TextView>(R.id.tv)
        var btn_call=findViewById<Button>(R.id.btn_call)
        var btns= arrayOf(
            findViewById<Button>(R.id.btn1)
            ,findViewById<Button>(R.id.btn2)
            ,findViewById<Button>(R.id.btn3)
            ,findViewById<Button>(R.id.btn4)
            ,findViewById<Button>(R.id.btn5)
            ,findViewById<Button>(R.id.btn6)
            ,findViewById<Button>(R.id.btn7)
            ,findViewById<Button>(R.id.btn8)
            ,findViewById<Button>(R.id.btn9)
            ,findViewById<Button>(R.id.btn0)
        )
        for (btn in btns){
            btn.setOnClickListener(){
                myclick(btn)
            }
        }
        btn_call.setOnClickListener(){
            mycall(btn_call)
        }

    }
    fun myclick(btn:Button){
        var txt=btn.getText().toString()
        text+=txt
        tv.text=text

    }
    fun mycall(btn:Button){
        var builder = AlertDialog.Builder(this)
        Toast.makeText(this.applicationContext,"calling\n"+text,Toast.LENGTH_SHORT).show();
    }

}