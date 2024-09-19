from .validate_image import llm
from .Prompt import PROMPTOCR, PROMPT2
import json,time,re

def countDigits(word):
    numbers = re.findall(r'\d+', (word))
    numbers_string = ''.join(numbers)
    return len(numbers_string)

def CPF_CNPJ_Validation(json):
    if json.get("consumidor_CNPJ_CPF"):
        cpf_cnpj = countDigits(json.get("consumidor_CNPJ_CPF"))
        if  cpf_cnpj != 11 and cpf_cnpj != 14:
            json["consumidor_CNPJ_CPF"] = None 
            
    if json.get("CNPJ") and countDigits(json.get("CNPJ")) != 14:
        json["CNPJ"] = None
    print(json)
    return json

def data_format(data):
    data = CPF_CNPJ_Validation(data)
    for key,value in data.items():
        if(data[key]):
            data[key] = re.sub('[a-zA-Z]', "", value)
            if data[key] == "":
                data[key] = None
        else:
            data[key] = None # nao sei porque, mas evita erros
                
    return data

def onlyGeminis(image):
    
    response = llm.call_ai_with_imageOCR(PROMPTOCR, image)
    print(f"{response.text} \nTotal Token Count1: {response.usage_metadata.total_token_count}")
    
    response = llm.call_ai(PROMPT2.replace("{data}", response.text))
    print(f"Total Token Count2: {response.usage_metadata.total_token_count}")
    return data_format(json.loads(response.text))