package com.example.thais.inicial;

import android.content.Intent;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;


public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void IrDenuncia(View view){
        Intent it = new Intent(MainActivity.this, MainActivity2Activity.class);
        startActivity(it);
    }

    public void IrProtocolo(View view){
        Intent it = new Intent(MainActivity.this, Protocolos.class);
        startActivity(it);
    }

    public void IrConfiguracoes(View view){
        Intent it = new Intent(MainActivity.this, Configuracoes.class);
        startActivity(it);
    }

    //Resources res = getResources();
    //Drawable dr = res.getDrawable(R.drawable.man282.png);

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
