# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
from google import genai

client = genai.Client(api_key="AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=   "Quero um bom editor de fórmulas matemáticas, estatística ... e que seja fácil de utilizar e gratuito",
)

# Crie um arquivo na pasta output
#with open('output/response.md', 'w') as arquivo:
#    arquivo.write(response.text)

# Supondo que você tenha algo assim no seu código
with open('output/response.md', 'w', encoding='utf-8') as arquivo:
    arquivo.write(response.text)