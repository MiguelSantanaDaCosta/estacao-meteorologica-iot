# 📊 Google Sheets - Etapa 2

## Apps Script Completo (Cole)
```javascript
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    var timestamp1970 = data.timestamp + 946684800;
    var dataHora = new Date(timestamp1970 * 1000);
    var ultimaLinha = sheet.getLastRow() + 1;
    
    sheet.getRange(ultimaLinha, 1, 1, 5).setValues([[
      dataHora, parseFloat(data.temperatura), parseFloat(data.umidade),
      parseFloat(data.gas || 0), parseFloat(data.luminosidade || 0)
    ]]);
    
    sheet.getRange(ultimaLinha, 1).setNumberFormat("dd/mm/yyyy hh:mm:ss");
    
    if (ultimaLinha == 1) {
      sheet.getRange(1,1,1,5).setValues([["Data/Hora","Temp°C","Umid%","Gas","Lumi"]]);
    }
    
    return ContentService.createTextOutput('{"status":"OK"}');
  } catch(e) {
    return ContentService.createTextOutput('{"status":"ERRO"}');
  }
}
```
