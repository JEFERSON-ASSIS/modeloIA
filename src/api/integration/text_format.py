import json, re, time
from .llm import LLM
from .Prompt import PROMPT
import vertexai.preview.generative_models as generative_models
llm = LLM()

def data_format(data):
    for key,value in data.items():
        # print(value)
        if(data[key]):
            data[key] = value = re.sub('[a-zA-Z]', '', value)
            if value == "" :
                data[key] = None
    
    return data

def countDigits(word):
    numbers = re.findall(r'\d+', (word))
    numbers_string = ''.join(numbers)
    print(len(numbers_string))
    return len(numbers_string)

def CPF_CNPJ_Validation(json):
    if json.get("consumidor_CNPJ_CPF"):
        if countDigits(json.get("consumidor_CNPJ_CPF")) != 11:
            json["consumidor_CNPJ_CPF"] = None
    if json.get("CNPJ"):
        if countDigits(json.get("CNPJ")) != 14:
            json["CNPJ"] = None
    print(json)
    return json

def text_format(data):
    # receives data
    data = json.dumps(data)
    
    t5 = time.time()
    prompt = PROMPT.replace("{data}", data)
    # call gemini
    try:
        response = llm.call_ai(prompt)
        data = json.loads(response.text)
        data = data_format(data)
        data = CPF_CNPJ_Validation(data)
        
    except Exception as e:
        print(f'Error processing: {e}')
        
    t6 = time.time()
    print("Tempo de execução 2 gemini: ", t6-t5)
    print(f"Total Token Count: {response.usage_metadata.total_token_count}")
    return {'data': data, 'status_code': 200}