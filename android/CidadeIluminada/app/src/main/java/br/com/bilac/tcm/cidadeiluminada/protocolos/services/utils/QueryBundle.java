package br.com.bilac.tcm.cidadeiluminada.protocolos.services.utils;


import java.io.File;
import java.util.Map;

public class QueryBundle {

    private String method;
    private String url;
    private String body;
    private File file;
    private Map<String, String> args;

    public String getMethod() {
        return method;
    }

    public String getUrl() {
        String queryString = "";
        return url + queryString;
    }

    public String getBody() {
        return body;
    }

    public File getFile() {
        return file;
    }

    public QueryBundle(String url, String body, Map<String, String> args) {
        this.method = "POST";
        this.url = url;
        this.body = body;
        this.args = args;
    }

    public QueryBundle(String url, String body) {
        this.method = "POST";
        this.url = url;
        this.body = body;
    }

    public QueryBundle(String url, File file, Map<String, String> args) {
        this.method = "POST";
        this.url = url;
        this.args = args;
        this.file = file;
    }

    public QueryBundle(String url, File file) {
        this.method = "POST";
        this.url = url;
        this.file = file;
    }

    public QueryBundle(String url, Map<String, String> args) {
        this.method = "GET";
        this.url = url;
        this.args = args;
    }

    public QueryBundle(String url) {
        this.method = "GET";
        this.url = url;
    }
}
