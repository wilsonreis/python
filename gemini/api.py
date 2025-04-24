# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
from google import genai

client = genai.Client(api_key="AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Me fale sobre as principais diferenças dentro aprendizado de máquina supervisionado, entre Classificação e Regressão. Explique os mais detalhadamente possível ",
)

# Crie um arquivo na pasta output
with open('output/resposta.md', 'w') as arquivo:
    arquivo.write(response.text)