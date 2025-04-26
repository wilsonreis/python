# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
# AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA
import google.generativeai as genai
import requests

# Substitua pela sua chave de API do Gemini
GOOGLE_API_KEY = "AIzaSyDKnwYxtaWZ0-uvGrb1rgxPr3fT1BpahAA"

# URL do arquivo Python no Gist
GIST_URL = "https://gist.github.com/wilsonreis/6bb0bb26ab4a3b5d7c1b3779e2e9218d"

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
        Por favor, analise o seguinte código Python e : 
         - modifique a saida da console para uma arquivo markdown
         - somente gere o código sem explicação
         - não deixe de colocar  os gráficos, no arquivo de saída.
        
        
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
        with open('output/response.md', 'w', encoding='utf-8') as arquivo:
            arquivo.write(analise)
#        print("Análise do código:")
#        print(analise)
    else:
        print("Não foi possível obter a análise do código.")