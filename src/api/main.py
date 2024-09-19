import os
from flask import Flask, request, jsonify
import requests
from io import BytesIO
from PIL import Image
from werkzeug.datastructures import FileStorage
from integration.receive_image import receive_image3  # Importa a função como está

app = Flask(__name__)

@app.route("/receiveImage", methods=["POST"])
def process_image():
    data = request.get_json()  # Recebe o JSON da requisição
    if 'image' not in data:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    try:
        # Baixa a imagem da URL fornecida
        image_url = data['image']
        response = requests.get(image_url)
        response.raise_for_status()  # Verifica se houve algum erro ao baixar a imagem

        # Converte os bytes da resposta para uma imagem
        image = Image.open(BytesIO(response.content))

        # Salva a imagem em um buffer de bytes para simular um upload de arquivo
        image_bytes = BytesIO()
        image.save(image_bytes, format='JPEG')  # Ajuste o formato conforme necessário
        image_bytes.seek(0)  # Retorna o ponteiro para o início do arquivo

        # Cria um objeto FileStorage para simular o `request.files` que o receive_image3 espera
        image_file = FileStorage(stream=image_bytes, filename="image.jpg", content_type="image/jpeg")

        # Simula o `request` com `files` para passar para receive_image3
        mock_request = type('MockRequest', (object,), {'files': {'image': image_file}})

        # Chama a função receive_image3 passando o mock_request
        result = receive_image3(mock_request)

        # Retorna o resultado do processamento com a função receive_image3
        print("Imagem processada com sucesso.")
        return jsonify({"message": "Imagem recebida e processada com sucesso", "result": result}), 200

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return jsonify({"error": "Erro ao processar a imagem"}), 500


if __name__ == '__main__':
    # Ajusta para pegar a porta de uma variável de ambiente, o que é necessário em ambientes como o Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)













# from flask import Flask, request
# from integration.receive_image import receive_image3


# app = Flask(__name__)

# @app.route("/")
# def main():
#     return "API Notas Fiscais"

# @app.route("/receiveImage", methods=["POST"])
# def process_image():
#     return receive_image3(request)

# if __name__ == '__main__':
#     app.run()