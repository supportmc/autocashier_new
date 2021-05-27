function parseURLParams(variable) {
    var url_string = window.location;
    var url = new URL(url_string);
    var paramValue = url.searchParams.get(variable);
    return paramValue;
}

// Screen 1
if (!parseURLParams('nfc')) document.getElementById('nfc').style.display = 'none';
if (!parseURLParams('mercadoPago')) document.getElementById('mercado-pago').style.display = 'none';
if (!parseURLParams('insertCash')) document.getElementById('insert-cash').style.display = 'none';
if (!parseURLParams('swipeCard')) document.getElementById('swipe-card').style.display = 'none';
if (!parseURLParams('card')) document.getElementById('card-element').style.display = 'none';
if (!parseURLParams('scanApp')) document.getElementById('scan-app').style.display = 'none';
if (!parseURLParams('newCard')) document.getElementById('new-card').style.display = 'none';
if (!parseURLParams('saldo')) {
    document.getElementById('saldo').style.display = 'none';
} else {
    document.getElementById('saldo').innerHTML = parseURLParams('saldo');
};
if (!parseURLParams('simbolo')) {
    document.getElementById('simbolo').style.display = 'none';
} else {
    document.getElementById('simbolo').innerHTML = parseURLParams('simbolo');
};

if (
    !parseURLParams('nfc') &&
    !parseURLParams('mercadoPago') &&
    !parseURLParams('insertCash') &&
    !parseURLParams('swipeCard') &&
    !parseURLParams('card') &&
    !parseURLParams('scanApp') &&
    !parseURLParams('newCard') &&
    !parseURLParams('saldo'))
    {
        document.getElementById('left-container').style.display = 'none';
        document.getElementById('balance-container').style.display = 'none';
        document.getElementById('actions').style.display = 'none';
        document.getElementById('main-content').style.height = '100vh';
    }

// Buttons
var insertCashBtn = document.getElementById('insert-cash');
var mercadoPagoBtn = document.getElementById('mercado-pago');
var cardBtn = document.getElementById('card');
var newCardBtn = document.getElementById('new-card');

// INPUT con Focus

function accion() {
    var accionEjecutada = true;
}

// Screen 2 
if (!parseURLParams('value1Btn')) document.getElementById('value1Btn').style.display = 'none'
if (!parseURLParams('value2Btn')) document.getElementById('value2Btn').style.display = 'none'
if (!parseURLParams('value3Btn')) document.getElementById('value3Btn').style.display = 'none'
if (!parseURLParams('value4Btn')) document.getElementById('value4Btn').style.display = 'none'
if (!parseURLParams('valuePersonalizadoBtn')) document.getElementById('valuePersonalizadoBtn').style.display = 'none'

if (!parseURLParams('saldoScreen2')) {
    document.getElementById('saldoScreen2').style.display = 'none';
} else {
    document.getElementById('saldoScreen2').innerHTML = parseURLParams('saldoScreen2');
};

if (!parseURLParams('simboloScreen2')) {
    document.getElementById('simboloScreen2').style.display = 'none';
} else {
    document.getElementById('simboloScreen2').innerHTML = parseURLParams('simboloScreen2');
};

if (!parseURLParams('valueSimbolo1')) {
    document.getElementById('valueSimbolo1').style.display = 'none'
} else {
    document.getElementById('valueSimbolo1').innerHTML = parseURLParams('valueSimbolo1');
};

if (!parseURLParams('valueSimbolo2')) {
    document.getElementById('valueSimbolo2').style.display = 'none'
} else {
    document.getElementById('valueSimbolo2').innerHTML = parseURLParams('valueSimbolo2');
};

if (!parseURLParams('valueSimbolo3')) {
    document.getElementById('valueSimbolo3').style.display = 'none'
} else {
    document.getElementById('valueSimbolo3').innerHTML = parseURLParams('valueSimbolo3');
};

if (!parseURLParams('valueSimbolo4')) {
    document.getElementById('valueSimbolo4').style.display = 'none'
} else {
    document.getElementById('valueSimbolo4').innerHTML = parseURLParams('valueSimbolo4');
};

if (!parseURLParams('valueMonto1')) {
    document.getElementById('valueMonto1').style.display = 'none'
} else {
    document.getElementById('valueMonto1').innerHTML = parseURLParams('valueMonto1');
};

if (!parseURLParams('valueMonto2')) {
    document.getElementById('valueMonto2').style.display = 'none';
} else {
    document.getElementById('valueMonto2').innerHTML = parseURLParams('valueMonto2');
};

if (!parseURLParams('valueMonto3')) {
    document.getElementById('valueMonto3').style.display = 'none';
} else {
    document.getElementById('valueMonto3').innerHTML = parseURLParams('valueMonto3');
};

if (!parseURLParams('valueMonto4')) {
    document.getElementById('valueMonto4').style.display = 'none';
} else {
    document.getElementById('valueMonto4').innerHTML = parseURLParams('valueMonto4');
};

if (!parseURLParams('valueSaldoPersonalizado')) {
    document.getElementById('valueSaldoPersonalizado').style.display = 'none';
} else {
    document.getElementById('valueSaldoPersonalizado').innerHTML = 'Personalised';
};

if (
    !parseURLParams('value1Btn') &&
    !parseURLParams('value2Btn') &&
    !parseURLParams('value3Btn') &&
    !parseURLParams('value4Btn') &&
    !parseURLParams('valuePersonalizadoBtn'))
    {
        document.getElementById('values').style.display = 'none';
    }

// Screen 3 ( Monto Seleccionado y Procesos Postnet )
if (!parseURLParams('valueSimboloSelected')) {
    document.getElementById('valueSimboloSelected').style.display = 'none';
} else {
    document.getElementById('valueSimboloSelected').innerHTML = parseURLParams('valueSimboloSelected');
};
if (!parseURLParams('valueMontoSelected')) {
    document.getElementById('valueMontoSelected').style.display = 'none';
} else {
    document.getElementById('valueMontoSelected').innerHTML = parseURLParams('valueMontoSelected');
};
if (!parseURLParams('saldoUpdated')) {
    document.getElementById('saldoUpdated').style.display = 'none';
} else {
    document.getElementById('saldoUpdated').innerHTML = parseURLParams('saldoUpdated');
};

if (!parseURLParams('processing')) document.getElementById('processing').style.display = 'none';

if (!parseURLParams('successProcess')) document.getElementById('successProcess').style.display = 'none';
if (!parseURLParams('errorProcess')) document.getElementById('errorProcess').style.display = 'none';
if (!parseURLParams('posnet')) document.getElementById('posnet').style.display = 'none';

// Screen 3 Monto Personalizado

if (!parseURLParams('posnetPersonalizado')) document.getElementById('posnetPersonalizado').style.display = 'none'; 


function mostrarValor( displayValue, valorBtn ) {
    document.getElementById(displayValue).innerHTML = document.getElementById(displayValue).innerHTML + valorBtn;
    var newDisplayValue = document.getElementById(displayValue).innerHTML;
    if ( newDisplayValue.length > 7 ) {
        eliminarValor()
    }
    if ( newDisplayValue.includes(',,') ) {
        eliminarValor()
    }
    var confirmBtn = document.getElementById('confirmBtn');
    confirmBtn.href = '?confirmedValue' + newDisplayValue;
    console.log(confirmBtn.href); 
}

function eliminarValor() {
    var displayValue = document.getElementById('displayValue').innerHTML;
    var newDisplayValue = displayValue.substr(0, displayValue.length - 1);
    console.log(newDisplayValue)
    document.getElementById('displayValue').innerHTML = newDisplayValue
}

if (!parseURLParams('processingPersonalizado')) document.getElementById('processingPersonalizado').style.display = 'none';
if (!parseURLParams('successProcessPersonalizado')) document.getElementById('successProcessPersonalizado').style.display = 'none'; 
if (!parseURLParams('errorProcessPersonalizado')) document.getElementById('errorProcessPersonalizado').style.display = 'none'; 

