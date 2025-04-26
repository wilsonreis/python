# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
from google import genai

client = genai.Client(api_key="AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=   "Você disse: Regressão Linear Múltipla: A solução para os coeficientes em regressão linear múltipla pode ser expressa usando operações de matrizes, incluindo a multiplicação."
                "Crie um código python, bem detalhado, que mostre a aplicação da multiplicação de matrizes na regressão linear múltipla",
)

# Crie um arquivo na pasta output
#with open('output/response.md', 'w') as arquivo:
#    arquivo.write(response.text)

# Supondo que você tenha algo assim no seu código
with open('response.md', 'w', encoding='utf-8') as arquivo:
    arquivo.write(response.text)