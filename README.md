# Leitor de PDF com IA

Programa em Python que **lê o texto de um PDF e usa uma IA (Gemini) para responder perguntas sobre o conteúdo dele** — funciona com currículo, contrato, apostila, ou qualquer PDF que tenha texto.

## O que ele faz

1. Procura sozinho os arquivos PDF que estão na mesma pasta do script
2. Se houver mais de um, pergunta qual você quer usar
3. Extrai todo o texto do PDF escolhido
4. Pergunta a você, no terminal, o que quer saber sobre o documento
5. Envia o texto + sua pergunta pra uma IA (Gemini)
6. Mostra a resposta da IA no terminal

Se uma chave de API travar por limite de uso (cota), o programa troca sozinho pra próxima chave/modelo disponível, sem parar de funcionar.

## Como instalar

1. Instale o Python (3.10 ou mais novo): https://www.python.org/downloads/ — marque a opção **"Add Python to PATH"** durante a instalação.

2. Instale as bibliotecas usadas pelo programa, abrindo o terminal (Prompt de Comando) e digitando:
```bash
pip install requests pdfplumber
```

## Como configurar sua chave da API (obrigatório)

O programa não tem nenhuma chave escrita dentro dele — cada pessoa usa a própria, de forma segura, por **variável de ambiente**.

1. Gere sua chave gratuita em: https://aistudio.google.com/apikey
2. No Windows, abra o Prompt de Comando e digite (trocando `SUA_CHAVE_AQUI` pela chave que você copiou):
```cmd
setx GEMINI_KEY_1 "SUA_CHAVE_AQUI"
```
3. Feche e abra o terminal de novo (a variável só passa a valer depois de reabrir).

> Você pode cadastrar até 10 chaves diferentes (`GEMINI_KEY_1` até `GEMINI_KEY_10`, repetindo o comando `setx` pra cada uma), assim, se uma bater o limite de uso, o programa troca pra próxima sozinho. Ter só a `GEMINI_KEY_1` já é suficiente pra funcionar.

## Como usar (agora ficou bem mais fácil)

Não precisa mais editar o código pra colocar o caminho do PDF nem a pergunta. É só isso:

1. Coloque o arquivo `.pdf` que você quer analisar **na mesma pasta** onde está o script `leitor_de_pdf_com_ia.py`.
2. Rode o programa:
```bash
python "leitor_de_pdf_com_ia.py"
```
3. Se houver só um PDF na pasta, ele já usa esse automaticamente. Se houver mais de um, o programa lista todos e pergunta qual número você quer usar.
4. Digite sua pergunta quando ele pedir, por exemplo:
```
O que você quer perguntar sobre esse PDF? qual é a formação do candidato?
```
5. A resposta da IA aparece direto no terminal.

Quer perguntar outra coisa sobre o mesmo PDF? É só rodar o programa de novo e digitar uma pergunta diferente — não precisa mexer em nada no código.

## Segurança

O programa só lê o PDF que está na mesma pasta dele no seu computador e envia o texto extraído pra API do Gemini pra gerar a resposta — nenhum arquivo é enviado pra nenhum outro lugar, e a chave de API fica só na sua máquina (nunca escrita no código).

## Autor

Benedito dos Santos — [GitHub](https://github.com/beneditodossantosjoao027-cloud)
