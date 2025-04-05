# YouTube Music Desktop Wrapper

Um simples aplicativo desktop multiplataforma que encapsula o site oficial do YouTube Music usando Python e PyWebView.

## Descrição

Este projeto fornece uma janela dedicada para acessar o YouTube Music, oferecendo uma experiência mais integrada ao desktop. Ele utiliza `pywebview` para exibir o conteúdo web e injeta JavaScript para extrair informações da música atualmente em reprodução, exibindo-as no título da janela.

*Nota: Este projeto começou como uma tentativa de usar a API não oficial `ytmusicapi`, mas devido a desafios com autenticação, pivotou para a abordagem de web wrapper, que se mostrou mais estável e funcional para os objetivos atuais.*

## Funcionalidades Atuais

* Exibe o site oficial do YouTube Music em uma janela desktop.
* Detecta a música atual (título, artista, capa) e atualiza o título da janela.
* Login é feito diretamente na página web segura do Google/YouTube.

## Funcionalidades Planejadas

* Controle da reprodução via teclas de mídia do teclado.
* Ícone do aplicativo personalizado.
* Opção de rodar em segundo plano com ícone na bandeja do sistema (System Tray).
* Salvar e restaurar tamanho/posição da janela.
* (Talvez) Integração com Discord Rich Presence.

## Requisitos

* Python 3.x
* Bibliotecas Python: `pywebview` (e suas dependências como `pythonnet` no Windows, `pyobjc` no macOS). Veja `requirements.txt`.
* Dependências do `pywebview` específicas do SO (geralmente instaladas automaticamente ou já presentes):
    * Windows: Edge WebView2 Runtime (geralmente incluído em W10/W11).
    * macOS: Safari/WebKit (já incluído).
    * Linux: `libwebkit2gtk-4.0` ou superior (instalar via gerenciador de pacotes, ex: `sudo apt install libwebkit2gtk-4.0-37`).

## Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_GITHUB]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```
3.  **Ative o ambiente virtual:**
    * Windows: `.\venv\Scripts\activate`
    * Linux/macOS: `source venv/bin/activate`
4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Veja a próxima seção sobre como criar o `requirements.txt`)*

## Como Criar `requirements.txt`

Com o ambiente virtual ativado, gere o arquivo de dependências:
```bash
pip freeze > requirements.txt
```

Verifique o arquivo gerado e remova linhas que não sejam dependências diretas do projeto (como pkg-resources ou o próprio pyinstaller se estiver instalado no venv).

## Como Executar
Com o ambiente virtual ativado e as dependências instaladas:

```bash
python ytmusic_wrapper.py

```

## Como Funciona (Resumo Técnico)
- pywebview é usado para criar a janela principal e carregar a URL do YouTube Music.
- Uma thread separada executa periodicamente.
- Nessa thread, window.evaluate_js() injeta código JavaScript na página web.
- O JavaScript usa document.querySelector() com seletores CSS específicos para encontrar os elementos HTML do título, artista e capa na barra de player do YouTube Music.
- Os dados extraídos são retornados ao Python como uma string JSON.
- O Python interpreta o JSON e atualiza o título da janela (window.set_title()).

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.