# Leitor de PDF com IA

Programa em Python que **lê o texto de um PDF e usa uma IA (Gemini) para responder perguntas sobre o conteúdo dele** — no exemplo pronto, ele lê um currículo e diz qual é a formação e quais tecnologias o candidato sabe.

## O que ele faz

1. Abre um arquivo PDF do seu computador
2. Extrai todo o texto que está dentro dele
3. Envia esse texto pra uma IA (Gemini), junto com uma pergunta
4. Mostra a resposta da IA no terminal

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

## Como colocar o caminho do PDF (a parte que mais gera dúvida)

No código, essa linha decide qual PDF vai ser lido:

```python
caminho = r"caminho.pdf"
```

Troque `caminho.pdf` pelo caminho completo do seu arquivo. As regras são:

1. **Sempre deixe o `r` antes das aspas.** Ele existe porque o Windows usa barra invertida (`\`) pra separar pastas, e sem o `r` o Python pode interpretar partes do caminho errado (por exemplo `\n` viraria quebra de linha em vez de fazer parte do nome da pasta).
2. **Copie o caminho certo do seu PDF:** no Windows, clique com o botão direito no arquivo → "Copiar como caminho" (ou segure Shift, clique com botão direito → "Copiar como caminho").
3. **Cole exatamente como veio**, mantendo o `r` e as aspas.

Exemplo real, igual ao caminho que você já usa:
```python
caminho = r"C:\Users\bened\OneDrive\Desktop\git hub\seupdf.pdf"
```

## Como usar

1. Ajuste a linha do `caminho` como explicado acima, apontando pro PDF que você quer analisar.
2. (Opcional) Troque a pergunta feita à IA, editando esta linha perto do final do arquivo:
```python
pergunta = f"Aqui está o conteúdo de um documento:\n\n{txt}\n\nCom base nesse documento, responda: faca sua pergunta aqui."
```
Você pode trocar o texto depois de "responda:" pra qualquer outra pergunta sobre o PDF.

3. Rode o programa:
```bash
python "leitor_de_pdf_com_ia.py"
```
4. A resposta da IA aparece direto no terminal.

## Erros comuns

- **"Nenhuma chave Gemini encontrada"** → você não configurou a variável de ambiente `GEMINI_KEY_1` corretamente, ou não reabriu o terminal depois de configurar.
- **Erro ao abrir o PDF / arquivo não encontrado** → o caminho na linha `caminho = r"..."` está errado ou o `r` foi removido sem querer.

## Segurança

O programa só lê o PDF que você indicar no seu próprio computador e envia o texto extraído pra API do Gemini pra gerar a resposta — nenhum arquivo é enviado pra nenhum outro lugar, e a chave de API fica só na sua máquina (nunca escrita no código).

## Autor

Benedito dos Santos — [GitHub](https://github.com/beneditodossantosjoao027-cloud)
