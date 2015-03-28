package br.com.bilac.tcm.cidadeiluminada.protocolos.validators;

import android.widget.TextView;

/**
 * Created by arthur on 28/03/15.
 */
public class EmptyValidator extends TextValidatorBase {
    private static final String message = "Campo não pode ser vazio";

    public EmptyValidator(TextView textView) {
        super(textView, message);
    }

    @Override
    public boolean validate(String text) {
        return !text.trim().isEmpty();
    }
}
