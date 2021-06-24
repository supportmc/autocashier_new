function parseURLParams(variable) {
    var url_string = window.location;
    var url = new URL(url_string);
    var paramValue = url.searchParams.get(variable);
    return paramValue;
}

function backToPreviousPage() {
    history.go(-2);
}

// SPINNER
if ( (!parseURLParams('btnCardActivado')) || (!parseURLParams('btnCardActivado')) )  document.getElementById('spinner').style.display = 'none';

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

if ( (!parseURLParams('newCardPrice')) ) {
    document.getElementById('newCardPrice').style.display = 'none';
} else {
    document.getElementById('newCardPrice').innerHTML = '(' + parseURLParams('newCardPrice');
};

window.onload = function() {

    if ( (!parseURLParams('msj'))  ) {
        document.getElementById('msj').style.display = 'none';    
    }

    if ((parseURLParams('finTransaccion')) && (parseURLParams('msj'))) {
        console.log('hola')
        document.getElementById('msj').innerHTML = parseURLParams('msj');
        setTimeout(() => {
            var searchParams = window.location.search;
            var URL = window.location.pathname;
            var newStr = searchParams.split('&fin')
            var newsearchParams = newStr[0];
            window.location.href = URL  + newsearchParams; 
        }, 4500);
    }
}

if ( (!parseURLParams('redWarning'))) document.getElementById('redWarning').style.display = 'none';
if ( (!parseURLParams('yellowWarning'))) document.getElementById('yellowWarning').style.display = 'none';

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

if (!parseURLParams('montoPersonalizado')) document.getElementById('valuePersonalizado').style.display = 'none';

function value1Selected() {
    var URL = window.location.pathname;
    var valueMonto1 = document.getElementById('valueMonto1').innerHTML;
    window.location.href = URL + '?' + 'valueSelected=' + valueMonto1;  
}

function value2Selected() {
    var URL = window.location.pathname;
    var valueMonto2 = document.getElementById('valueMonto2').innerHTML;
    window.location.href = URL + '?' + 'valueSelected=' + valueMonto2;  
}

function value3Selected() {
    var URL = window.location.pathname;
    var valueMonto3 = document.getElementById('valueMonto3').innerHTML;
    window.location.href = URL + '?' + 'valueSelected=' + valueMonto3;  
}

function value4Selected() {
    var URL = window.location.pathname;
    var valueMonto4 = document.getElementById('valueMonto4').innerHTML;
    window.location.href = URL + '?' + 'valueSelected=' + valueMonto4;  
}


// Screen 3  Monto Seleccionado 
if ( (!parseURLParams('saldo3')) || (!parseURLParams('simbolo3')) ) {
    document.getElementById('balance3').style.display = 'none';
} else {
    document.getElementById('saldo3').innerHTML = parseURLParams('saldo3');
    document.getElementById('simbolo3').innerHTML = parseURLParams('simbolo3');
};

if (!parseURLParams('screen3')) {
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

if (!parseURLParams('successProcess')) document.getElementById('successProcess').style.display = 'none';
if (!parseURLParams('errorProcess')) document.getElementById('errorProcess').style.display = 'none';


// Screen 3 Monto Personalizado
if ( (!parseURLParams('saldo3Personalizado')) || (!parseURLParams('simbolo3Personalizado')) ) {
    document.getElementById('balance3Personalizado').style.display = 'none';
} else {
    document.getElementById('saldo3Personalizado').innerHTML = parseURLParams('saldo3Personalizado');
    document.getElementById('simbolo3Personalizado').innerHTML = parseURLParams('simbolo3Personalizado');
    document.getElementById('divisaDisplay').innerHTML = parseURLParams('simbolo3Personalizado');
};

if (!parseURLParams('screen3Personalizado')) {
    document.getElementById('backToScreen2Personalizado').style.display = 'none';
    document.getElementById('card3Personalizado').style.display = 'none';  
    document.getElementById('posnetPersonalizado').style.display = 'none';  
    document.getElementById('posnetIconPersonalizado').style.display = 'none';
    document.getElementById('confirmBtn').style.display = 'none';
}

if (!parseURLParams('successProcessPersonalizado')) document.getElementById('successProcessPersonalizado').style.display = 'none'; 
if (!parseURLParams('errorProcessPersonalizado')) document.getElementById('errorProcessPersonalizado').style.display = 'none'; 

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
    confirmBtn.href = '?confirmedValue=' + newDisplayValue;
    console.log(confirmBtn.href); 
}

function eliminarValor() {
    var displayValue = document.getElementById('displayValue').innerHTML;
    var newDisplayValue = displayValue.substr(0, displayValue.length - 1);
    console.log(newDisplayValue)
    document.getElementById('displayValue').innerHTML = newDisplayValue
}

// CHARGE INFORMATION SCREEN
if (!parseURLParams('chargeInfo')) document.getElementById('chargeInfo').style.display = 'none';

 if (!parseURLParams('cardNumber')) {
    document.getElementById('card-number').style.display = 'none'; 
 } else {
    document.getElementById('card-number').innerHTML = parseURLParams('cardNumber'); 
 }
 
 if (parseURLParams('chargeInfoTable')) {
    var chargeInfoTable = parseURLParams('chargeInfoTable');

    var chargeInfoTable =  JSON.parse(chargeInfoTable)

    var result = '';
    var total = '';

    chargeInfoTable.forEach(getRaw);

    function getRaw(item) {
        result = '';
        item.forEach(getI);
        result = '<tr>'+result+'</tr>';
        total += result
        console.log(result);
        console.log(total);
        document.getElementById('chargeInfoTable').innerHTML = '<table><tr><th>Date</th><th>System</th><th>Amount</th>'+total+'</tr></table>';
    }

    function getI(i) {
        result += '<td>'+i+'</td>';
        return result;
    }
}
