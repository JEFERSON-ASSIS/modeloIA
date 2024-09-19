from integration.onlyGeminis import onlyGeminis
from integration.validate_image import validate_image 
    
def receive_image3(request):
    file = request.files['image']
    image = file.read() 
    
    try:
        return onlyGeminis(image) if validate_image(image) else {
            "numero_nota_fiscal": None,
            "serie_nota_fiscal": None,
            "CNPJ": None,
            "consumidor_CNPJ_CPF": None,
            "valor_total": None,
            "data_emissao": None 
        }
        
    except Exception as e:
        print(f'Error processing: {e}')
        return {
            "numero_nota_fiscal": None,
            "serie_nota_fiscal": None,
            "CNPJ": None,
            "consumidor_CNPJ_CPF": None,
            "valor_total": None,
            "data_emissao": None
        }

    

