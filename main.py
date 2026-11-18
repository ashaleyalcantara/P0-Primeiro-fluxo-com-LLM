
import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera a chave de API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Chave de API não encontrada. Verifique o arquivo .env.")

# Inicializa o cliente Gemini
client = genai.Client(api_key=api_key)

# Recebe a frase do usuário
frase = input("Digite uma frase para análise sintática: ")

# Define as instruções para a análise sintática
prompt = f"""
Realize a análise sintática da seguinte frase em língua portuguesa:

<frase>
{frase}
</frase>

Identifique os seguintes elementos:
- Sujeito 
- Núcleo do sujeito;
- Predicado 
- Núcleo do predicado;
- Verbo;
- Objeto direto;
- Objeto indireto;
- Adjunto adverbial e seu tipo, quando identificado.

Organize os resultados em formato de lista, apresentando
cada elemento sintático em uma linha, seguido de sua identificação.

Quando um elemento não for identificado, informe
"Não identificado".

Considere exatamente a frase fornecida, mesmo que apresente
desvios gramaticais. Não solicite outra frase nem invente
elementos que não estejam presentes.

Após a lista, apresente uma explicação mais aprofundada,
abordando:
- A classificação do sujeito e a função de seu núcleo;
- A classificação do predicado e seu núcleo;
- A classificação do verbo quanto à transitividade;
- A relação entre o verbo e seus complementos;
- A função dos adjuntos adverbiais identificados.

Explique como os elementos se relacionam dentro da oração,
utilizando a própria frase como exemplo.

Apresente explicações claras, organizadas e tecnicamente
consistentes, sem mencionar hipóteses descartadas.

Retorne a resposta em texto simples, sem utilizar JSON ou tabelas.
"""

# Envia a frase ao modelo
interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=prompt
)

# Apresenta a resposta
print("\n" + "              ANÁLISE SINTÁTICA")

print(f"\nFrase analisada: {frase}")

print("\n" + interaction.output_text)

