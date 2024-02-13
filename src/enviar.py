from flask import Flask, jsonify, request
#LIBRERIAS PARA ENVIAR MENSAJES VIA WHTSAPP
from heyoo import WhatsApp
app = Flask(__name__)
#EJECUTAMOS ESTE CODIGO CUANDO SE INGRESE A LA RUTA ENVIAR
@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    try:
        # TOKEN DE ACESSO DO FACEBOOK
        token = 'EAAE0F3xZA3ZCsBOzqsZBxMpzqAEl9HZARNwRiZAvUrvkobxjZA27dXJ1WNI6Ptge3RgfgQo2Q5wrfjv64oDz957pLBYt5mV8fkvqvunS1R2RxZBetsDsxlArRGc75ABLREvqq4Vsql8li78cXffDmFID4P902KPZBglKFg1AEoOznj8JyasOtOCCHIUH9VsksnwwbLhyCq8PkVLoN9NKA1ZBRaZAyhSG6y47PZA7gMvLEOxr9IZD'
        # IDENTIFICADOR DO NÚMERO DE TELEFONE
        idNumeroTelefone = '237607696094045'
        # TELEFONE QUE RECEBE (O NOSSO TELEFONE REGISTRADO)
        telefoneEnvia = '35991383664'
        # MENSAGEM A SER ENVIADA
        textoMensagem = "Olá novato, cumprimentos"
        # URL DA IMAGEM A SER ENVIADA
        # urlImagem = 'https://i.imgur.com/r5lhxgn.png'
        # INICIALIZA O ENVIO DE MENSAGENS
        mensagemWa = WhatsApp(token, idNumeroTelefone)
        # ENVIA UMA MENSAGEM DE TEXTO
        mensagemWa.send_message(textoMensagem, telefoneEnvia)

        return jsonify("mensagem enviada com sucesso"), 200
    
    except Exception as e:
        print(e)
        return jsonify({'mensagem': e}), 500


# INICIA O FLASK