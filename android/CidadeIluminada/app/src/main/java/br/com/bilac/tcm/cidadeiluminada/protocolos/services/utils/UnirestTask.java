package br.com.bilac.tcm.cidadeiluminada.protocolos.services.utils;

import android.os.AsyncTask;
import android.util.Log;

import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.mashape.unirest.request.HttpRequestWithBody;

import java.util.UUID;

public class UnirestTask extends AsyncTask<QueryBundle, Void, JsonNode> {
    @Override
    protected JsonNode doInBackground(QueryBundle... queryBundles) {
        QueryBundle query = queryBundles[0];
        try {
            if (query.getMethod().equals("GET")) {
                return Unirest.get(query.getUrl()).asJson().getBody();
            } else {
                HttpRequestWithBody postRequest = Unirest.post(query.getUrl());
                postRequest.field("arquivo_protocolo", query.getFile());
                postRequest.field("cod_protocolo", "dasdasdasdasdasd");
                postRequest.field("cep", "12240-310");
                return postRequest.asJson().getBody();
            }
        } catch (UnirestException e) {
            Log.e(this.getClass().getName(), e.getClass().getName(), e);
            return null;
        }
    }
}
