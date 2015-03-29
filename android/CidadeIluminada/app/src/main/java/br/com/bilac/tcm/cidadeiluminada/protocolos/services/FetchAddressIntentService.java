package br.com.bilac.tcm.cidadeiluminada.protocolos.services;

import android.app.IntentService;
import android.content.Intent;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.os.Bundle;
import android.os.ResultReceiver;
import android.text.TextUtils;
import android.util.Log;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

import br.com.bilac.tcm.cidadeiluminada.Constants;

/**
 * Created by arthur on 29/03/15.
 */
public class FetchAddressIntentService extends IntentService {

    public FetchAddressIntentService() {
        super("FetchAddressIntentService");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        Geocoder geocoder = new Geocoder(this, Locale.getDefault());
        Location location = intent.getParcelableExtra(Constants.LOCATION_DATA_EXTRA);
        ResultReceiver receiver = intent.getParcelableExtra(Constants.RECEIVER);

        List<Address> addresses = null;

        try {
            addresses = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
        } catch (IOException e) {
            e.printStackTrace();
            Log.e("addresIntentService", "Localização indisponivel");
        }

        Bundle bundle = new Bundle();
        if (addresses == null || addresses.size() == 0) {
            bundle.putBoolean(Constants.RESULT_DATA_KEY, false);
            receiver.send(Constants.FAILURE_RESULT, bundle);
        } else {
            Address address = addresses.get(0);
            bundle.putParcelable(Constants.RESULT_DATA_KEY, address);
            receiver.send(Constants.SUCESS_RESULT, bundle);
        }
    }
}
