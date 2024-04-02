package kr.co.aiai.high;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.widget.Toast;

public class ServiceMe extends Service {
    @Override
    public void onCreate() {
        Toast toast = Toast.makeText(this, "onCreate", Toast.LENGTH_LONG);
        toast.show();
        super.onCreate();
    }

    @Override
    public void onStart(Intent intent, int startId) {
        String param = intent.getStringExtra("param");
        Toast toast = Toast.makeText(this, "onStart:" + param, Toast.LENGTH_LONG);
        toast.show();
        super.onStart(intent, startId);
    }

    @Override
    public void onDestroy() {
        Toast toast = Toast.makeText(this, "onDestroy", Toast.LENGTH_LONG);
        toast.show();
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent arg0) {
        // TODO Auto-generated method stub
        return null;
    }

}