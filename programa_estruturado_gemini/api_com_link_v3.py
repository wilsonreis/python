# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
import google.generativeai as genai
import requests

# Substitua pela sua chave de API do Gemini
GOOGLE_API_KEY = "AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA"

# URL do arquivo Python no Gist
GIST_URL = "https://gist.github.com/wilsonreis/d53f9cda31b9c48062c1603bb27204c8"

def analisar_codigo_com_gemini(url_codigo, api_key):
    """
    Envia um código Python para o Gemini para análise.

    Args:
        url_codigo: URL do arquivo Python a ser analisado.
        api_key: Sua chave de API do Gemini.

    Returns:
        A resposta do Gemini, ou None em caso de erro.
    """

    try:
        # Obter o conteúdo do arquivo Python do Gist
        response = requests.get(url_codigo)
        response.raise_for_status()  # Levanta uma exceção para códigos de erro HTTP
        codigo_python = response.text

        # Inicializar o modelo Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Construir a mensagem para o Gemini
        prompt = f"""
        Por favor, analise o seguinte código Python você fez algumas considerações :

        - if __name__ == '__main__':
        -   # Criando dados de exemplo (substitua por seus próprios dados)
        -   # Vamos usar 3 variáveis independentes (características) e 5 observações
        -   X = np.array([
        -       [1, 2, 3, 4],  # Observação 1 (1 é para o intercepto)
        -       [1, 5, 6, 7],  # Observação 2
        -       [1, 8, 9, 10], # Observação 3
        -       [1, 11, 12, 13],# Observação 4
        -       [1, 14, 15, 16]  # Observação 5
        -   ])
        
        - me explique porque a observação 1 vai ser o intercepto. Sempre devemos ter a observação 1 como intercepto
            
        ])

        Código:
        ```python
        {codigo_python}
        ```
        """

        # Enviar a solicitação para o Gemini
        response = model.generate_content(prompt)

        return response.text  # Retorna apenas o texto da resposta

    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o código do Gist: {e}")
        return None
    except Exception as e:
        print(f"Erro ao interagir com o Gemini: {e}")
        return None

if __name__ == "__main__":
    # Chamar a função para analisar o código
    analise = analisar_codigo_com_gemini(GIST_URL, GOOGLE_API_KEY)

    # Imprimir a análise
    if analise:
        # Supondo que você tenha algo assim no seu código
        with open('response.md', 'w', encoding='utf-8') as arquivo:
            arquivo.write(analise)
#        print("Análise do código:")
#        print(analise)
    else:
        print("Não foi possível obter a análise do código.")