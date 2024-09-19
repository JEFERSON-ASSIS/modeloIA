prompt_validate_image = """
Aprove notas fiscais somente, nota_fiscal = True
Se houver alguma letra ou número manuscrita na imagem, manuscrito = True
Caso a nota fiscal seja do tipo grande, impressa em papel, tipo_grande = True
Responda no seguinte formato:
{
"nota_fiscal": "True/False",
"manuscrito": "True/False",
"tipo_grande": "True/False"
}
"""

PROMPT2 = """
    Busque os dados a partir desta OCR de uma nota fiscal: " {data}
    Se a nota for Sat, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "n° sat"
    Se a nota for nfe, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "NFE no"
    Se a nota for NFC-e, o "numero_nota_fiscal" sera após nfc-e "serie_nota_fiscal" sera a série"
    Caso não encontre algum dado deixe o campo em branco.
    Preencha este JSON:
    {
    "numero_nota_fiscal": "número da nota fiscal, se existente, tem até nove dígitos, pode começar com zeros"
    "serie_nota_fiscal": "série da nota fiscal, se existente",
    "CNPJ": "CNPJ da loja formato dd.ddd.ddd/dddd-dd",
    "consumidor_CNPJ_CPF": "CPF formato ddd.ddd.ddd-dd",
    "valor_total": "VALOR A PAGAR(VALOR PAGO)(Valo total da nota),se houver desconto o valor total é o valor com desconto",
    "data_emissao": "data nota fiscal formate como dd/mm/aaaa"
    }
    """
PROMPTOCR = """
    retorne um OCR completo da nota fiscal
    junte valores com um texto da nota a esquerda ou acima somente um valor por palavra, EXEMPLO: valor: 100,00, desconto: 10,00, valor total: 90,00
    Os campos necessários são os seguintes:
    - valor total: valor total, caso haja desconto, o valor total é o valor com desconto
    - numero nota fiscal
    - serie nota fiscal
    - CNPJ da loja
    - CPF do consumidor(se houver)
    - data de emissão
    divida em seções(---) e a cada seção retorne o texto da seção
    """

# PROMPTCHECK = """
#   Extraia os seguintes dados da nota fiscal:
#     Se a nota for Sat, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "n° sat".
#     Se a nota for nfe, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "NFE no".
#     Se a nota for NFC-e, o "numero_nota_fiscal" sera após nfc-e "serie_nota_fiscal" sera a série".
#     Caso não encontre algum dado deixe o campo em branco.
#     Preencha apenas este JSON, para apenas uma nota fiscal:
#     {
#     "numero_nota_fiscal": "número da nota fiscal, se existente, tem até nove dígitos, pode começar com zeros"
#     "serie_nota_fiscal": "série da nota fiscal, se existente",
#     "CNPJ": "CNPJ da loja formato dd.ddd.ddd/dddd-dd (d é um número)",
#     "consumidor_CNPJ_CPF": "código CPF formato ddd.ddd.ddd-dd (d é um número)",
#     "valor_total": "VALOR A PAGAR",
#     "data_emissao": "data nota fiscal formate como dd/mm/aaaa"
#     }
#   """    
  
  # PROMPT = """
#     Busque os dados somente a partir desta base, que contém o OCR de apenas uma nota fiscal: "  {data}
#     Se a nota for Sat, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "n° sat".
#     Se a nota for nfe, o "numero_nota_fiscal" sera o extrato e "serie_nota_fiscal" sera o "NFE no".
#     Se a nota for NFC-e, o "numero_nota_fiscal" sera após nfc-e "serie_nota_fiscal" sera a série".
#     Se o preço não for em reais, deixe o campo valor total em branco.
#     Caso não encontre algum dado deixe o campo em branco.
#     Preencha e responda este JSON:
#     {
#     "numero_nota_fiscal": "número da nota fiscal, se existente, tem até nove dígitos, pode começar com zeros, na duvida deixe os zeros da string",
#     "serie_nota_fiscal": "série da nota fiscal, se existente",
#     "CNPJ": "código CNPJ formato dd.ddd.ddd/dddd-dd (d é um número)",
#     "consumidor_CNPJ_CPF": "código CPF formato ddd.ddd.ddd-dd (d é um número)",
#     "valor_total": "valor total PAGO da nota fiscal",
#     "data_emissao": "data de emissão da nota fiscal"
#     }    
#     """

