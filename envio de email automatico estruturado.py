import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class GerenciadorEmail:
    def __init__(self):
        
        self.remetente = 'e-mail do remetente'
        self.senha = 'senha de aplicativo cadastrada na conta'
        self.destinatario = 'e-mail do destinatairo'
        self.assunto = 'Estudando Python'
        self.corpo = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Material de Estudo - Python</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                    <tr>
                        <td align="center" style="padding: 40px 0;">
                            <a href="https://www.python.org/" target="_blank">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Logo do Python" width="200" style="display: block; margin: 0 auto;">
                            </a>
                            <p style="margin-top: 20px; text-align: center;">Olá,</p>
                            <p style="text-align: center;">Este é um e-mail contendo material de estudo para aprender Python.</p>
                            <p style="text-align: center;">Se você está começando agora ou deseja aprimorar suas habilidades, este conteúdo será útil para a sua jornada.</p>
                            <p style="text-align: center;">Aproveite os recursos e comece a explorar o mundo da programação com Python!</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
        self.servidor_smtp, self.porta = self.definir_servidor()
        
    def definir_servidor(self):
       
        if self.remetente.endswith('@gmail.com'):
            return 'smtp.gmail.com', 587
        elif self.remetente.endswith('@outlook.com') or self.remetente.endswith('@hotmail.com'):
            return 'smtp-mail.outlook.com', 587
        elif self.remetente.endswith('@solutta.com'):
            return 'smtp.office365.com', 587
        else:
            print('Domínio do remetente não é suportado por este programa.')
            exit()
   
    def configuracao_msg(self):
       
        msg = MIMEMultipart()
        msg['From'] = self.remetente
        msg['To'] = self.destinatario
        msg['Subject'] = self.assunto
        msg.attach(MIMEText(self.corpo, 'html'))
        return msg

    def enviar_email(self):
      
        msg = self.configuracao_msg()
        
        try:
            servidor = smtplib.SMTP(self.servidor_smtp, self.porta)
            servidor.starttls()
            servidor.login(self.remetente, self.senha)
            servidor.sendmail(self.remetente, self.destinatario, msg.as_string())
            print('E-mail enviado com sucesso!')
        except Exception as e:
            print(f'Ocorreu algum erro durante o envio: {e}')
        finally:
            servidor.quit()

GerenciadorEmail().enviar_email()
