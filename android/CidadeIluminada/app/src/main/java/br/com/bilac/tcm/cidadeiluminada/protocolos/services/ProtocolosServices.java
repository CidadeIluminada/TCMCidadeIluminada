package br.com.bilac.tcm.cidadeiluminada.protocolos.services;

import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;

import java.io.File;

import br.com.bilac.tcm.cidadeiluminada.Constants;

/**
 * Created by arthur on 28/03/15.
 */
public class ProtocolosServices {
    private static final String BASE_URL = Constants.CIDADEILUMINADA_HOST + "/protocolos";

    public static void EnviarNovoProtocolo(File foto, String cep, String numero, String descricao) {
        try {
            Unirest.post(BASE_URL + "/novo/").field("cep", cep).field("numero", numero).asJson();
        } catch (UnirestException e) {
            e.printStackTrace();
        }
    }
}
