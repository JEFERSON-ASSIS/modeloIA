import json
from .Prompt import prompt_validate_image
from .llm import LLM

llm = LLM()

#===================================================================================
def validate_image(img):
    
    response = llm.call_ai_with_image(prompt_validate_image, img)
    data = json.loads(response.text)
         
    print(f"Gemini0: {response.usage_metadata.total_token_count} \n DATA: {data}")
                        
    # Removida a verificação de 'tipo_grande'
    if data.get('nota_fiscal') == "False" or data.get('manuscrito') == "True":
        return False

    return True






# import json
# from .Prompt import prompt_validate_image
# from .llm import LLM
# llm = LLM()

# #===================================================================================
# def validate_image(img):
    
#     response = llm.call_ai_with_image(prompt_validate_image,img)
#     data = json.loads(response.text)
         
#     print(f"Gemini0: {response.usage_metadata.total_token_count} \n DATA: {data}")
                        
#     if( data.get('nota_fiscal') == "False"or data.get('manuscrito') == "True" 
#         or data.get('tipo_grande') == "True"):
#         return False
#     return True