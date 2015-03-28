package br.com.bilac.tcm.cidadeiluminada.protocolos.validators;

import android.text.Editable;
import android.text.TextWatcher;
import android.widget.TextView;

/**
 * Created by arthur on 28/03/15.
 */
public abstract class TextValidatorBase implements TextWatcher {

    private TextView textView;
    private String errorMessage;

    private ValidationState validationState;

    public TextValidatorBase(TextView textView, String errorMessage, ValidationState validationState) {
        this.textView = textView;
        this.errorMessage = errorMessage;
        this.validationState = validationState;
    }

    @Override
    public void beforeTextChanged(CharSequence s, int start, int count, int after) {
    }

    @Override
    public void onTextChanged(CharSequence s, int start, int before, int count) {
    }

    @Override
    public void afterTextChanged(Editable s) {
        boolean result = validate(textView.getText().toString());
        if (!result) {
            textView.setError(errorMessage);
        } else {
            textView.setError(null);
        }
        validationState.setValid(result);
    }

    public abstract boolean validate(String text);
}
