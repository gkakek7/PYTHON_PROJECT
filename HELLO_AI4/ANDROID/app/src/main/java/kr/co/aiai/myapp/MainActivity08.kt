package kr.co.aiai.myapp

import android.app.AlertDialog
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import kotlin.random.Random

class MainActivity08 : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main07)
        Log.d("gilsang","[MainActivity08]onCreate")
        var btn = findViewById<Button>(R.id.btn)
        btn.setOnClickListener() {
        }

    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("gilsang","[MainActivity08]onDestroy");
    }

    override fun onStart() {
        super.onStart()
        Log.d("gilsang","[MainActivity08]onStart");
    }

    override fun onStop() {
        super.onStop()
        Log.d("gilsang","[MainActivity08]onStop");
    }

    override fun onResume() {
        super.onResume()
        Log.d("gilsang","[MainActivity08]onResume");
    }

    override fun onPause() {
        super.onPause()
        Log.d("gilsang","[MainActivity08]onPause");
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("gilsang","[MainActivity08]onRestart");
    }

}