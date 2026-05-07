text
# 📧 Email SMTP Gmail - Desafio Extra (1pt)

## 🎯 Configuração Rápida (2min)

1. **myaccount.google.com** → **Segurança**
2. **Verificação em 2 etapas** → **Ativar** (se não tiver)
3. **Senhas de app** → **Mail** → **Gerar**
4. **Copie 16 caracteres:**
abcd efgh ijkl mnop

text

## Código emails.py (Parte EmailManager)

```python
EMAIL_SMTP = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USER = "miguelsantanadacosta@gmail.com"
EMAIL_SENHA_APP = "abcd efgh ijkl mnop"  # ← SEU código

class EmailManager:
    def __init__(self, smtp_server=EMAIL_SMTP, port=EMAIL_PORT, 
                 email=EMAIL_USER, senha_app=EMAIL_SENHA_APP):
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.senha_app = senha_app

    def enviar_relatorio_diario(self, media_temp, media_umid, total_leituras, data_ref):
        smtp = umail.SMTP(self.smtp_server, self.port, ssl=True)
        smtp.login(self.email, self.senha_app)
        smtp.to("alessandrohoras@umc.br")
        
        corpo = f"""
RELATÓRIO DIÁRIO - ESTAÇÃO ESP32

Data: {data_ref}
Média Temperatura: {media_temp:.1f}°C
Média Umidade: {media_umid:.1f}%
Total Leituras: {total_leituras}

Estação funcionando! - Miguel Santana
        """
        
        smtp.write(f"From: {self.email}\r\n")
        smtp.write(f"Subject: Relatório {data_ref}\r\n")
        smtp.write("Content-Type: text/plain; charset=utf-8\r\n\r\n")
        smtp.write(corpo)
        smtp.send()
        smtp.quit()
        print("✅ Email enviado!")
```

## 🧪 Teste Imediato

**emails.py** `DiarioManager.processar_leitura()` linha ~85:
```python
dia_atual = 1  # ← FORCE (email em 3 leituras!)
```

**ESP32 Terminal:**
Sheets OK
✅ Email enviado!

text

**Inbox:** alessandrohoras@umc.br

## 🔄 Produção
dia_atual = agora # Email meia-noite automático

text

## 📧 Email Recebido
Assunto: Relatório 07/05/2026
Data: 07/05/2026
Média Temperatura: 24.1°C
Média Umidade: 40.5%
Total Leituras: 5

text

## Dependências
wokwi-esp32/umail.py # Lib SMTP MicroPython

text

**Configure → Teste → Produção = DESAFIO EXTRA 100%!**
