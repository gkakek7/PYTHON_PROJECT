package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import kotlin.random.Random

class MainActivity04 : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main04)
        var btn = findViewById<Button>(R.id.btn)

        btn.setOnClickListener{
            myclick()
        }


    }
    fun myclick(){
        var arr=IntArray(45)
        for (i in 0 until arr.size) {
            arr[i] = i + 1
        }
        for(i in 0 until 10000){
            val rnd = Random.nextInt(0, arr.size)
            var temp = arr[0]
            arr[0]=arr[rnd]
            arr[rnd]=temp
        }

        var tvarr= arrayOf(
            findViewById<TextView>(R.id.tv1)
            ,findViewById<TextView>(R.id.tv2)
            ,findViewById<TextView>(R.id.tv3)
            ,findViewById<TextView>(R.id.tv4)
            ,findViewById<TextView>(R.id.tv5)
            ,findViewById<TextView>(R.id.tv6)
        )

        for(i in 0 until tvarr.size){
            for(j in 0 until tvarr.size){
                var a=arr[i]
                var b=arr[j]
                if(a<b){
                    arr[i]=b
                    arr[j]=a;
                }
            }
        }

        for(i in 0 until tvarr.size){
            tvarr[i].setText(arr[i].toString())
        }
    }

}