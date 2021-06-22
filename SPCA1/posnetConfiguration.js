function parseURLParams(variable) {
    var url_string = window.location;
    var url = new URL(url_string);
    var paramValue = url.searchParams.get(variable);
    return paramValue;
}

if (!parseURLParams('vTerminalId')) document.getElementById('posnetConfiguration').style.display = 'none';
if (parseURLParams('vTerminalId')) document.getElementById('terminalId').value = parseURLParams('vTerminalId');
if (parseURLParams('vMerchantId')) document.getElementById('merchantId').value = parseURLParams('vMerchantId');
if (parseURLParams('vTax')) document.getElementById('tax').value = parseURLParams('vTax');

function redirectBackSavingVariables() {
    var terminalId = document.getElementById('terminalId').value;
    var merchantId = document.getElementById('merchantId').value;
    var tax = document.getElementById('tax').value;
    var URL = window.location.pathname;
    window.location.href = URL  + '?' + 'vTerminalId=' + terminalId + '&MerchantId=' + merchantId + '&Vtax=' + tax; 
}




