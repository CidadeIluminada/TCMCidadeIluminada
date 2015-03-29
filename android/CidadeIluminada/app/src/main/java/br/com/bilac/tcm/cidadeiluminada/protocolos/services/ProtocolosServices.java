package br.com.bilac.tcm.cidadeiluminada.protocolos.services;

import com.google.gson.Gson;
import com.mashape.unirest.http.JsonNode;

import java.io.File;
import java.util.concurrent.ExecutionException;

import br.com.bilac.tcm.cidadeiluminada.Constants;
import br.com.bilac.tcm.cidadeiluminada.protocolos.services.utils.APIResponse;
import br.com.bilac.tcm.cidadeiluminada.protocolos.services.utils.QueryBundle;
import br.com.bilac.tcm.cidadeiluminada.protocolos.services.utils.UnirestTask;

/**
 * Created by arthur on 28/03/15.
 */
public class ProtocolosServices {
    private static final String BASE_URL = Constants.CIDADEILUMINADA_HOST + "/protocolos";

    public static APIResponse EnviarNovoProtocolo(File foto, String cep, String numero, String descricao) {
        UnirestTask task = new UnirestTask();
        task.execute(new QueryBundle(BASE_URL + "/novo/", foto));
        try {
            JsonNode result = task.get();
            return new Gson().fromJson(result.toString(), APIResponse.class);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        return null;
    }
}
