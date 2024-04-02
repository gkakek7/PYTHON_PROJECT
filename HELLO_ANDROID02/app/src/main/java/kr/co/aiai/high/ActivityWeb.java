package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;

public class ActivityWeb extends AppCompatActivity {
    private WebView wv;
    EditText et_text;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        et_text = findViewById(R.id.et_text);
        wv = findViewById(R.id.wv);
        wv.getSettings().setJavaScriptEnabled(true);

        Button btn = findViewById(R.id.btn);
        Button btn2 = findViewById(R.id.btn2);
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick2();
            }
        });
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });

    }
    void myclick2(){
        String webUrlLocal = "file:///android_asset/index.html";
        wv.loadUrl(webUrlLocal);
    }
    void myclick(){
        String url = String.valueOf(et_text.getText());
        WebSettings settings = wv.getSettings();
        wv.setWebViewClient(new WebViewClient());
        wv.loadUrl(url);
    }
}
