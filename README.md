# Youtube Music Desktop - Projeto de Aprendizagem em Python

Este é um projeto de aprendizagem em Python que tem como objetivo criar uma aplicação desktop inspirada no Youtube Music. A aplicação permite:

- Pesquisa de músicas no YouTube utilizando `yt-dlp`
- Reprodução de áudio com o `QMediaPlayer` do PyQt5
- Interface gráfica aprimorada, inspirada no layout do Youtube Music, com painel lateral, barra de busca, lista de resultados e controles de reprodução
- Integração de login com a conta do Youtube Music (através de um navegador embutido com `QWebEngineView`)
- Execução de buscas em segundo plano usando threads (QThread) para evitar travamentos na interface

> **Observação:**  
> A funcionalidade de envio de "scrobble" para o Last.fm foi removida temporariamente da aplicação (comentada ou removida do `main.py`) devido ao erro:  
> `AttributeError: module 'lastfm' has no attribute 'scrobble_track'`  
> Em versões futuras, a integração com o Last.fm será implementada novamente, juntamente com a autenticação completa e extração aprimorada de metadados.

## Funcionalidades Planejadas (Futuro Aprimoramento)

- **Autenticação completa no Last.fm:**  
  Implementar o fluxo de autenticação para que cada usuário obtenha e armazene seu `SESSION_KEY` e possa enviar seus próprios scrobbles.
- **Interface Aprimorada:**  
  Utilizar recursos avançados do PyQt5 (ícones, temas customizados, layouts responsivos, etc.) para refinar a experiência do usuário.
- **Extração Aprimorada de Metadados:**  
  Integrar APIs adicionais, como a API do YouTube Data, para obter de forma mais confiável o nome do artista, título da música, álbum, etc.
- **Tratamento de Erros e Feedback para o Usuário:**  
  Adicionar mensagens de erro, indicadores de carregamento (loading spinners) e logs para melhorar a usabilidade e facilitar a depuração.
- **Empacotamento da Aplicação:**  
  Utilizar ferramentas como PyInstaller para empacotar o aplicativo em um executável desktop.

## Estrutura do Projeto

```bash
youtube_music_desktop/
│
├── env/                   # Ambiente virtual (criado pelo Python)
├── src/                   # Código-fonte do projeto
│   ├── main.py            # Arquivo principal, onde a aplicação será iniciada
│   ├── ui_main.py         # Código referente à interface gráfica (UI) com PyQt5
│   ├── youtube_helper.py  # Módulo para busca e extração do áudio do YouTube
│   └── lastfm.py          # Módulo para integração com a API do Last.fm
│
├── assets/                # Recursos como ícones e imagens
│   └── icons/
│
└── README.md              # Documentação do projeto
```

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/youtube_music_desktop.git
   cd youtube_music_desktop

   ```

2. **Crie e Ative o Ambiente Virtual:**

python -m venv env

- No Windows:

```bash
python -m venv env
```

- No Linux/macOS:

```bash
source env/bin/activate
```

3. **Instale as Dependências:**

As dependências utilizadas são:

- PyQt5

- PyQtWebEngine

- yt-dlp

- requests

Caso haja um arquivo `requirements.txt` (recomendado), instale com:

```bash
pip install -r requirements.txt
```

Caso não exista, instale manualmente:

```bash
pip install PyQt5 PyQtWebEngine yt-dlp requests
```

4. **Executando a Aplicação:**

Navegue até a pasta `src` e execute o arquivo principal:

```bash
cd src
python main.py
```

## Observações

- FFmpeg:
  Durante a execução, o `yt-dlp` pode emitir avisos sobre a ausência do `ffmpeg`. Recomenda-se instalar o `ffmpeg` e adicioná-lo ao PATH para garantir a melhor qualidade de extração de áudio.
  Mais informações: ffmpeg.org

- Integração com Last.fm:
  A funcionalidade de scrobble foi removida temporariamente devido a um problema de atributo. Futuras versões do projeto irão integrar essa funcionalidade com autenticação e captura de metadados aprimorada.

## Contribuição

Este projeto é um aprendizado em desenvolvimento de aplicações desktop com Python e PyQt5. Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções.

## Licença

Este projeto está licenciado sob a MIT License.
