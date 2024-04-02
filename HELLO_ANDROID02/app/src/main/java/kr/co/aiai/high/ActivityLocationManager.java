package kr.co.aiai.high;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.FileOutputStream;

public class ActivityLocationManager extends AppCompatActivity implements LocationListener {
    LocationManager lm;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location_manager);
        Button btn = findViewById(R.id.btn);
        tv = findViewById(R.id.tv);
        lm = (LocationManager) getSystemService(LOCATION_SERVICE);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String txt= (String) tv.getText();
                try {
                    FileOutputStream fileoutputstream = openFileOutput("babo.txt", MODE_PRIVATE);
                    fileoutputstream.write(txt.getBytes());
                    fileoutputstream.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return;
        }
        lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000, 5, this);
    }

    @Override
    protected void onPause() {
        lm.removeUpdates(this);
        super.onPause();
    }

    @Override
    public void onLocationChanged(@NonNull Location location) {
        String text = "lat:" + location.getLatitude() + "\t" + "lng:" + location.getLongitude() + "\n";
        tv.setText(text + tv.getText().toString());
    }
}