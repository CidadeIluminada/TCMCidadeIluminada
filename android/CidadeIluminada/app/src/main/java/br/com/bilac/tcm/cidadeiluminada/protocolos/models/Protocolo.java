package br.com.bilac.tcm.cidadeiluminada.protocolos.models;

import com.orm.SugarRecord;

import java.util.UUID;

/**
 * Created by arthur on 29/03/15.
 */
public class Protocolo extends SugarRecord {

    private String cod_protocolo;
    private String cep;
    private String estado;
    private String cidade;
    private String bairro;
    private String logradouro;
    private String numero;

    public Protocolo() {
    }

    public Protocolo(String cep, String estado, String cidade, String bairro, String logradouro, String numero) {
        this.cod_protocolo = UUID.randomUUID().toString();

        this.cep = cep;
        this.estado = estado;
        this.cidade = cidade;
        this.bairro = bairro;
        this.logradouro = logradouro;
        this.numero = numero;
    }

    public static Protocolo novoProtocoloSJC(String cep, String bairro, String logradouro, String numero) {
        return new Protocolo(cep, "SP", "Sâo José dos Campos", bairro, logradouro, numero);
    }

    public String getCep() {
        return cep;
    }

    public String getNumero() {
        return numero;
    }
}
