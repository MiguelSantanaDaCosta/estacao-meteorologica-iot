# emails.py
# =========================
# SISTEMA DE RELATORIOS - ETAPA 2
# =========================
# Gerencia Google Sheets e Email SMTP para estacao meteorologica
# Compatível com seu main.py atual

from machine import Pin, ADC, I2C
import time
import ujson
import urequests
import umail

# =========================
# CONFIGURAÇÕES
# =========================
SHEETS_URL = "https://script.google.com/macros/s/SEU_SCRIPT_ID/exec"
EMAIL_SMTP = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USER = "seuemail@gmail.com"
EMAIL_SENHA_APP = "abcd-efgh-ijkl-mnop"  # App Password do Gmail

# =========================
# GOOGLE SHEETS
# =========================
class GoogleSheets:
    """Envia dados para Google Sheets via Apps Script"""
    
    def __init__(self, url=SHEETS_URL):
        self.url = url

    def enviar_dados(self, dados):
        """Envia timestamp, temp e umidade para Sheets"""
        try:
            payload = ujson.dumps(dados)
            response = urequests.post(self.url, data=payload)
            
            if response.status_code == 200:
                response.close()
                return True
            response.close()
            return False
        except Exception as e:
            print("Sheets erro:", e)
            return False


# =========================
# EMAIL SMTP GMAIL
# =========================
class EmailManager:
    """Envia relatorios diários via SMTP Gmail"""
    
    def __init__(self, smtp_server=EMAIL_SMTP, port=EMAIL_PORT, 
                 email=EMAIL_USER, senha_app=EMAIL_SENHA_APP):
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.senha_app = senha_app

    def enviar_relatorio_diario(self, media_temp, media_umid, total_leituras, data_ref):
        """Envia email com resumo do dia"""
        try:
            smtp = umail.SMTP(self.smtp_server, self.port, ssl=True)
            smtp.login(self.email, self.senha_app)
            smtp.to("alessandrohoras@umc.br")
            
            # Monta email completo
            assunto = f"📊 Relatório Diário Estação - {data_ref}"
            corpo = f"""
RELATÓRIO DIÁRIO - ESTAÇÃO METEOROLÓGICA

Data: {data_ref}
Média Temperatura: {media_temp:.1f}°C
Média Umidade: {media_umid:.1f}%
Total de Leituras: {total_leituras}

Sistema funcionando normalmente!
Estação ESP32 Miguel
            """
            
            smtp.write(f"From: {self.email}\r\n")
            smtp.write(f"Subject: {assunto}\r\n")
            smtp.write("Content-Type: text/plain; charset=utf-8\r\n")
            smtp.write("\r\n")
            smtp.write(corpo)
            
            smtp.send()
            smtp.quit()
            print("✅ Email enviado!")
            return True
            
        except Exception as e:
            print("❌ Email erro:", e)
            return False


# =========================
# CONTADOR DIÁRIO
# =========================
class DiarioManager:
    """Calcula médias diárias e dispara relatórios"""
    
    def __init__(self):
        self.soma_temp = 0.0
        self.soma_umid = 0.0
        self.total_leituras = 0
        self.ultimo_dia = None

    def processar_leitura(self, temp, umid):
        """Processa nova leitura e verifica se é novo dia"""
        agora = time.localtime()
        dia_atual = agora[2]  # Dia do mês (1-31)

        # Primeiro dia ou novo dia?
        if self.ultimo_dia is None or dia_atual != self.ultimo_dia:
            relatorio = self._gerar_relatorio()
            
            # Reseta para novo dia
            self.soma_temp = 0.0
            self.soma_umid = 0.0
            self.total_leituras = 0
            self.ultimo_dia = dia_atual
            
            return {
                "nova_leitura": True,
                "relatorio": relatorio,
                "data_ref": time.strftime("%d/%m/%Y", agora)
            }
        
        # Acumula para o dia atual
        self.soma_temp += temp
        self.soma_umid += umid
        self.total_leituras += 1
        
        return {"nova_leitura": True}

    def _gerar_relatorio(self):
        """Gera dados do relatório (chamado no fim do dia)"""
        if self.total_leituras == 0:
            return None
            
        return {
            "media_temp": self.soma_temp / self.total_leituras,
            "media_umid": self.soma_umid / self.total_leituras,
            "total_leituras": self.total_leituras
        }


# =========================
# GERENCIADOR COMPLETO
# =========================
class RelatoriosManager:
    """Classe principal que junta tudo"""
    
    def __init__(self):
        self.sheets = GoogleSheets()
        self.email = EmailManager()
        self.diario = DiarioManager()

    def processar_dados(self, dados_completo):
        """Processa uma leitura completa (chamar no loop principal)"""
        temp = dados_completo["temperatura"]
        umid = dados_completo["umidade"]
        
        # 1. Processa contador diário
        resultado = self.diario.processar_leitura(temp, umid)
        
        # 2. Sempre envia para Sheets
        sheets_ok = self.sheets.enviar_dados({
            "timestamp": dados_completo["timestamp"],
            "temperatura": temp,
            "umidade": umid
        })
        
        # 3. Se tem relatório pronto, envia email
        if "relatorio" in resultado and resultado["relatorio"]:
            relatorio = resultado["relatorio"]
            self.email.enviar_relatorio_diario(
                relatorio["media_temp"],
                relatorio["media_umid"],
                relatorio["total_leituras"],
                resultado["data_ref"]
            )
        
        return {
            "sheets_ok": sheets_ok,
            "tem_relatorio": "relatorio" in resultado
        }

