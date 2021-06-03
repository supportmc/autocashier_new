function parseURLParams(variable) {
    var url_string = window.location;
    var url = new URL(url_string);
    var paramValue = url.searchParams.get(variable);
    return paramValue;
}

// Pantalla 1:

if (!parseURLParams('mercadoPago')) document.getElementById('mercado-pago').style.display = 'none';
if (!parseURLParams('insertCash')) document.getElementById('insert-cash').style.display = 'none';
if (!parseURLParams('card')) document.getElementById('card').style.display = 'none';

if (!parseURLParams('nfc')) document.getElementById('nfc').style.display = 'none';
if (!parseURLParams('swipeCard')) document.getElementById('swipe-card').style.display = 'none';
if (!parseURLParams('scanApp')) document.getElementById('scan-app').style.display = 'none';

if (!parseURLParams('newCard')) document.getElementById('new-card').style.display = 'none';

if ( (!parseURLParams('saldo')) || (!parseURLParams('simbolo')) ) {
    document.getElementById('balance').style.display = 'none';
} else {
    document.getElementById('saldo').innerHTML = parseURLParams('saldo');
    document.getElementById('simbolo').innerHTML = parseURLParams('simbolo');
};

if (!parseURLParams('finTransaccion')) {
    document.getElementById('finTransaccion').style.display = 'none';
    document.getElementById('finTransaccionLogo').style.display = 'none';
}

window.onload = function() {
    if ( (parseURLParams('finTransaccion'))  ) {
        document.getElementById('finTransaccion').className += ' finTransaccionFinal';
        document.getElementById('finTransaccionLogo').className += ' finTransaccionLogoFinal';
        setTimeout(() => {
            var searchParams = window.location.search;
            var URL = window.location.pathname;
            console.log(window.location)
            console.log(URL) 
            var newStr = searchParams.split('&fin')
            var newsearchParams = newStr[0];
            window.location.href = URL + '?' + newsearchParams;  
        }, 2500);
    }
}

// Pantalla 2 

if ( (!parseURLParams('saldo2')) || (!parseURLParams('simbolo2')) ) {
    document.getElementById('balance2').style.display = 'none';
} else {
    document.getElementById('saldo2').innerHTML = parseURLParams('saldo2');
    document.getElementById('simbolo2').innerHTML = parseURLParams('simbolo2');
};

if (!parseURLParams('screen2')) {
    document.getElementById('backToScreen1').style.display = 'none' 
    document.getElementById('card2').style.display = 'none' 
}

if (!parseURLParams('valueMonto1') ) {
    document.getElementById('value1').style.display = 'none'
} else {
    document.getElementById('valueMonto1').innerHTML = parseURLParams('valueMonto1');
    document.getElementById('valueSimbolo1').innerHTML = parseURLParams('simbolo2');
}

if (!parseURLParams('valueMonto2') ) {
    document.getElementById('value2').style.display = 'none'
} else {
    document.getElementById('valueMonto2').innerHTML = parseURLParams('valueMonto2');
    document.getElementById('valueSimbolo2').innerHTML = parseURLParams('simbolo2');
}

if (!parseURLParams('valueMonto3') ) {
    document.getElementById('value3').style.display = 'none'
} else {
    document.getElementById('valueMonto3').innerHTML = parseURLParams('valueMonto3');
    document.getElementById('valueSimbolo3').innerHTML = parseURLParams('simbolo2');
}

if (!parseURLParams('valueMonto4') ) {
    document.getElementById('value4').style.display = 'none'
} else {
    document.getElementById('valueMonto4').innerHTML = parseURLParams('valueMonto4');
    document.getElementById('valueSimbolo4').innerHTML = parseURLParams('simbolo2');
}

if (!parseURLParams('valuePersonalizado')) document.getElementById('valuePersonalizado').style.display = 'none'


// Screen 3  Monto Seleccionado 

if ( (!parseURLParams('saldo3')) || (!parseURLParams('simbolo3')) ) {
    document.getElementById('balance3').style.display = 'none';
} else {
    document.getElementById('saldo3').innerHTML = parseURLParams('saldo3');
    document.getElementById('simbolo3').innerHTML = parseURLParams('simbolo3');
};

if (!parseURLParams('screen3')) {
    document.getElementById('backToScreen2').style.display = 'none'; 
    document.getElementById('card3').style.display = 'none';
    document.getElementById('posnetIcon').style.display = 'none';
    document.getElementById('señalador').style.display = 'none'   
}

if ( (!parseURLParams('valueSimboloSelected')) || (!parseURLParams('valueMontoSelected')) ) {
    document.getElementById('ItemSelected').style.display = 'none';
} else {
    document.getElementById('valueSimboloSelected').innerHTML = parseURLParams('valueSimboloSelected');
    document.getElementById('valueMontoSelected').innerHTML = parseURLParams('valueMontoSelected');
};

if (parseURLParams('saldoUpdated')) {
    document.getElementById('valueMontoSelected').innerHTML = parseURLParams('saldoUpdated');
};

if (!parseURLParams('processing')) document.getElementById('processing').style.display = 'none';
if (!parseURLParams('successProcess')) document.getElementById('successProcess').style.display = 'none';
if (!parseURLParams('errorProcess')) document.getElementById('errorProcess').style.display = 'none';


// Screen 3 Monto Personalizado

if ( (!parseURLParams('saldo3Personalizado')) || (!parseURLParams('simbolo3Personalizado')) ) {
    document.getElementById('balance3Personalizado').style.display = 'none';
} else {
    document.getElementById('saldo3Personalizado').innerHTML = parseURLParams('saldo3Personalizado');
    document.getElementById('simbolo3Personalizado').innerHTML = parseURLParams('simbolo3Personalizado');
};

if (!parseURLParams('screen3Personalizado')) {
    document.getElementById('backToScreen2Personalizado').style.display = 'none';
    document.getElementById('card3Personalizado').style.display = 'none';  
    document.getElementById('posnetPersonalizado').style.display = 'none';  
    document.getElementById('posnetIconPersonalizado').style.display = 'none';
    document.getElementById('confirmBtn').style.display = 'none';
    document.getElementById('señaladorPersonalizado').style.display = 'none';
}

if (!parseURLParams('processingPersonalizado')) document.getElementById('processingPersonalizado').style.display = 'none';
if (!parseURLParams('successProcessPersonalizado')) document.getElementById('successProcessPersonalizado').style.display = 'none'; 
if (!parseURLParams('errorProcessPersonalizado')) document.getElementById('errorProcessPersonalizado').style.display = 'none'; 

if (!parseURLParams('successMsg')) {
    document.getElementById('successMsg').style.display = 'none';
} else {
    document.getElementById('successMsg').innerHTML = parseURLParams('successMsg');
}

if (!parseURLParams('errorMsg')) {
    document.getElementById('errorMsg').style.display = 'none';
} else {
    document.getElementById('errorMsg').innerHTML = parseURLParams('errorMsg');
}

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

if (!parseURLParams('errorMsg')) {
    document.getElementById('errorMsg').style.display = 'none';
} else {
    document.getElementById('errorMsg').innerHTML = parseURLParams('errorMsg');
}

// CHARGE INFORMATION SCREEN

 if (!parseURLParams('cardNumber')) document.getElementById('card-number').style.display = 'none'; 
 if (!parseURLParams('chargeInfo')) {
    document.getElementById('chargeInfo').style.display = 'none';
 } else {
     document.getElementById('chargeInfo').innerHTML = parseURLParams('chargeInfo');
 }
