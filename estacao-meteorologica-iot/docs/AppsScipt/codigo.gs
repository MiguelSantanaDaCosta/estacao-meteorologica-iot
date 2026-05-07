function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    
    //  ESP32)
    var timestamp1970 = data.timestamp + 946684800;
    var dataHora = new Date(timestamp1970 * 1000);
    
    var ultimaLinha = sheet.getLastRow() + 1;
    
    //  COLUNAS COMPLETAS
    sheet.getRange(ultimaLinha, 1, 1, 5).setValues([[
      dataHora,
      parseFloat(data.temperatura),
      parseFloat(data.umidade),
      parseFloat(data.gas || 0),
      parseFloat(data.luminosidade || 0)
    ]]);
    
    // Formatação
    sheet.getRange(ultimaLinha, 1).setNumberFormat("dd/mm/yyyy hh:mm:ss");
    
    // CABEÇALHOS 
    if (ultimaLinha == 1) {
      sheet.getRange(1, 1, 1, 5).setValues([[
        "Data/Hora", "Temperatura°C", "Umidade%", "Gas", "Luminosidade"
      ]]);
      sheet.getRange(1, 1, 1, 5).setFontWeight("bold").setBackground("#4285f4");
    }
    
    sheet.autoResizeColumns(1, 5);
    atualizarResumo(sheet);
    
    return ContentService.createTextOutput('{"status":"OK"}');
  } catch (error) {
    return ContentService.createTextOutput('{"status":"ERRO","msg":"'+error+'"}');
  }
}

function atualizarResumo(sheet) {
  var ultimaLinha = sheet.getLastRow();
  if (ultimaLinha < 2) return;
  
  // MÉDIA TOTAL (acumulada)
  var dados = sheet.getRange("B2:C" + ultimaLinha).getValues();
  var temps = dados.map(r=>r[0]).filter(t=>t>0);
  var umids = dados.map(r=>r[1]).filter(u=>u>0);
  
  //  TOTAL
  sheet.getRange("A7").setValue("📊 TOTAL");
  sheet.getRange("B7").setValue((temps.reduce((a,b)=>a+b)/temps.length || 0).toFixed(1)+"°C");
  sheet.getRange("C7").setValue((umids.reduce((a,b)=>a+b)/umids.length || 0).toFixed(1)+"%");
  sheet.getRange("D7").setValue("("+temps.length+" leituras)");
  
  // ÚLTIMA HORA
  var horaAtras = new Date(Date.now() - 60*60*1000);
  var ultHora = sheet.getRange("A2:A" + ultimaLinha).getValues()
    .filter(r=>new Date(r[0]) > horaAtras).length;
  sheet.getRange("A8").setValue("⏰ ÚLTIMA HORA");
  sheet.getRange("D8").setValue("("+ultHora+" leituras)");
}

function testarPost() {
  UrlFetchApp.fetch(ScriptApp.getService().getUrl(), {
    method: 'POST',
    contentType: 'application/json',
    payload: JSON.stringify({
      timestamp: Math.floor(Date.now()/1000)-946684800, // Simula ESP32
      temperatura: 24.5,
      umidade: 58.2,
      gas: 3500,
      luminosidade: 1200
    })
  });
}
