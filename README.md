# 🤖 Inteligências Artificiais Generativas Aplicadas a Programação

## 🛠️ Ferramentas utilizadas

``` bash
python -m venv .venv
pip install streamlit
pip install openai
pip install agno
pip install sqlalchemy
pip install yfinance
pip install opencv-python
pip install pyautogui
pip install langchain-openai
pip install langchain-community
pip install langchain
pip install serial
pip install pyserial

# Extra:
pip install dotenv
```

## 🐍 Introdução Python

Pycharm é IDE especializada para a linguagem de programação Python, interpretada. Este tipo também é conhecido como "linguagem de scripts". Essa ferramenta é utilizada para facilitar a escrita de código, oferecendo recursos como destaque de sintaxe, autocompletar, depuração e integração com sistemas de controle de versão. O Pycharm é amplamente utilizado por desenvolvedores Python para criar uma variedade de aplicações, desde scripts simples até projetos complexos de software.

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, conhecida por sua sintaxe clara e legibilidade. Ela suporta múltiplos paradigmas de programação, incluindo programação orientada a objetos, funcional e procedural. Python é amplamente utilizado em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial, automação e muito mais. A linguagem é conhecida por sua vasta biblioteca padrão e uma comunidade ativa que contribui com uma ampla gama de pacotes e frameworks para facilitar o desenvolvimento de aplicações.

Comentários: Auxílio na programação, facilitar a comunicação e melhorar legibilidade. No python, estas linhas são iniciadas com "#". Estas linhas são ignoradas pelas linguagens.

### 🪐 Jupyter Notebook

Ferramenta integrada no Pycharm que serve como um livro de anotações virtal que pode mesclar escrita e texto, além de rodar código.

No mundo da programação, as palavras não podem ter acento, começar com números, começar com alguns caracteres especiais como "?" ou "!"

Ao nomear arquivos, o espaço não é utilizado. As duas técnicas adequadas são:
- **Underline** `senai_americana`
- **CamelCase** `senaiAmericana`

### 📝 Literais em Python

Em python, você possui os seguintes tipos de variáveis:
- Texto - `"SENAI"` - String
- Inteiros `1, 2, -3,, -10...` - Int
- Reais; `3.14, 1.73...` - Float
- Booleanos `True or False` - Bool

O funcionamento padrão de um programa de computador é:
> Entrada de Dados → Processamento de Dados → Saída de Dados

### 📌 Exemplo

Elaborar um srcipt em python que solicite que o usuário digite `largura` e `altura` de retângulo e depois calcula a área, perímetro e a diagonal

## 👨‍🏫 Sintaxe Python

Estruturas de Dados e Funções

Utilização do arquivo REVISAO.ipynb

## 🖼️ A história da Inteligência Artificial

A inteligência artificial (IA) é um campo da ciência da computação que se concentra na criação de sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana. A história da IA remonta à década de 1950, quando os pesquisadores começaram a explorar a possibilidade de criar máquinas inteligentes. Nos anos 1950 e 1960, os primeiros programas de IA foram desenvolvidos, como o Logic Theorist e o General Problem Solver. No entanto, esses programas eram limitados em sua capacidade de resolver problemas complexos. Nos anos 1970 e 1980, a IA passou por um período de estagnação conhecido como "inverno da IA", devido à falta de progresso significativo e ao alto custo dos sistemas de IA. No entanto, a partir dos anos 1990, a IA começou a ganhar impulso novamente, com o desenvolvimento de algoritmos de aprendizado de máquina e o aumento do poder computacional. Nos anos 2000, a IA se tornou cada vez mais presente em nossas vidas, com o surgimento de assistentes virtuais, sistemas de recomendação e veículos autônomos. Hoje, a IA continua a evoluir rapidamente, com avanços em áreas como aprendizado profundo, processamento de linguagem natural e visão computacional, prometendo transformar ainda mais a maneira como vivemos e trabalhamos.

Arquivos: Aula03/

## 🍽️  API

``` plain text
1. Prompt → 2. (API ⇄ Modelo) → 3. Saída

1 - Dados não estruturados
2 - Processamento
3 - Dados não estruturados
```

Essa estrutura é a base para a maioria dos sistemas de IA, onde um prompt é enviado para um modelo de IA por meio de uma API, e o modelo processa o prompt e retorna uma saída. A API atua como uma ponte entre o usuário e o modelo de IA, permitindo que os usuários interajam com o modelo de maneira eficiente e fácil.

### 📒 Definições

API (Application Programming Interface) é um conjunto de regras e protocolos que permitem que diferentes softwares se comuniquem entre si. Ela define como os componentes de software devem interagir, permitindo que aplicativos, serviços e sistemas troquem informações e funcionalidades de maneira eficiente. As APIs são amplamente utilizadas para integrar diferentes sistemas, acessar dados e serviços de terceiros, e criar aplicações mais complexas e interconectadas.

#### 🎫 Token

Os tokens são unidades de texto que os modelos de linguagem processam. Eles podem ser palavras, partes de palavras ou até mesmo caracteres individuais, dependendo do modelo. O número de tokens em um prompt ou resposta pode afetar o custo e o tempo de processamento, já que muitos modelos têm limites de tokens para entrada e saída. Com isso, é importante considerar a quantidade de tokens ao criar prompts para garantir que eles sejam eficientes e dentro dos limites do modelo.

#### 🔑 Chave API

A chave API é um código único que é usado para autenticar e autorizar o acesso a uma API. Ela é fornecida pelo provedor da API e deve ser incluída em cada solicitação feita à API para garantir que o usuário tenha permissão para acessar os recursos e dados oferecidos pela API. A chave API é uma medida de segurança importante para proteger os dados e serviços da API contra acesso não autorizado.

##### 🔒 Protegendo a Chave

É crucial proteger a chave API para evitar o uso não autorizado e possíveis abusos. Algumas práticas recomendadas incluem:
- Não compartilhar a chave API publicamente, como em repositórios de código ou fóruns;
- Utilizar variáveis de ambiente para armazenar a chave API em vez de hardcodá-la no código;
- Implementar restrições de uso, como limitar o número de solicitações ou restringir o acesso a determinados endereços IP;
- Monitorar o uso da chave API para detectar atividades suspeitas e agir rapidamente em caso de comprometimento.
- Usar .env para armazenar a chave API e garantir que o arquivo .env esteja incluído no .gitignore para evitar que seja enviado para repositórios públicos.

No caso deste repositório, a chave API é armazenada diretamente no código até a aula 06, onde passaremos a utilizar o arquivo .env para protegê-la com a biblioteca python-dotenv com a variável de ambiente `API_KEY`.

É impossivel por padrão enviar um código para o GitHub que contenha uma chave API, pois o GitHub tem mecanismos de detecção automática de chaves API e irá bloquear o repositório ou alertar o usuário sobre a exposição da chave. Portanto, é importante garantir que a chave API seja removida do código antes de enviá-lo para o GitHub, utilizando práticas como as mencionadas acima para proteger a chave e evitar problemas de segurança.

## 🕒 Agno

O Agno é um framework de código aberto para a construção de agentes de inteligência artificial. Ele fornece uma estrutura para criar agentes que podem interagir com o ambiente, tomar decisões e aprender com suas experiências. O Agno é projetado para ser flexível e modular, permitindo que os desenvolvedores criem agentes personalizados para uma variedade de aplicações, desde assistentes virtuais até robôs autônomos.  O Agno suporta a integração com várias bibliotecas de aprendizado de máquina e processamento de linguagem natural, facilitando a criação de agentes inteligentes que podem entender e responder a comandos em linguagem natural. Ele também inclui ferramentas para monitorar o desempenho dos agentes e ajustar suas estratégias com base no feedback do ambiente. O Agno é uma ferramenta poderosa para pesquisadores e desenvolvedores que desejam explorar o campo da inteligência artificial e criar agentes que possam aprender e se adaptar a diferentes situações.

## 🕵️‍♂️ HackerTools

### 📒 Definição

HackerTools é um conjunto de ferramentas e recursos projetados para ajudar os profissionais de segurança cibernética a identificar, analisar e mitigar ameaças de segurança. Essas ferramentas podem incluir scanners de vulnerabilidades, analisadores de tráfego de rede, ferramentas de teste de penetração, entre outros. O objetivo do HackerTools é fornecer aos profissionais de segurança as ferramentas necessárias para proteger sistemas e redes contra ataques cibernéticos, identificando vulnerabilidades e implementando medidas de segurança eficazes.

## 🪙 YFinance

YFinance é uma biblioteca Python que permite acessar dados financeiros de forma fácil e eficiente. Ela fornece uma interface para obter informações sobre ações, índices, moedas e outros instrumentos financeiros, incluindo preços históricos, dados de mercado em tempo real, dividendos e muito mais. Com o YFinance, os usuários podem realizar análises financeiras, criar gráficos e desenvolver estratégias de investimento com base em dados precisos e atualizados. A biblioteca é amplamente utilizada por investidores, analistas financeiros e desenvolvedores que desejam integrar dados financeiros em seus projetos de análise e visualização.

## ♾️ Arduino IDE

A Arduino IDE (Integrated Development Environment) é um ambiente de desenvolvimento integrado utilizado para programar placas de microcontroladores da família Arduino. Ele fornece uma interface amigável para escrever, compilar e carregar código em placas Arduino, facilitando o processo de desenvolvimento de projetos eletrônicos. A IDE suporta a linguagem de programação C/C++ e inclui uma série de bibliotecas pré-construídas que simplificam a interação com sensores, atuadores e outros componentes eletrônicos. Com a Arduino IDE, os usuários podem criar uma ampla variedade de projetos, desde simples pisca-pisca de LEDs até sistemas complexos de automação e robótica.

A estrutura básica de um sketch (programa) em Arduino é composta por duas funções principais: `setup()` e `loop()`. A função `setup()` é executada uma vez quando o programa é iniciado e é usada para configurar as definições iniciais, como a configuração de pinos e a inicialização de variáveis. A função `loop()` é executada repetidamente após a execução do `setup()` e contém o código principal do programa que será executado continuamente enquanto a placa estiver ligada. Essa estrutura permite que os programas Arduino sejam simples e eficientes, facilitando o desenvolvimento de projetos eletrônicos interativos.

### ESP32

O ESP32 é um microcontrolador de baixo custo e alta performance desenvolvido pela Espressif Systems. Ele é amplamente utilizado em projetos de Internet das Coisas (IoT) devido à sua capacidade de se conectar a redes Wi-Fi e Bluetooth, além de oferecer uma variedade de recursos integrados, como sensores, interfaces de comunicação e suporte para múltiplos núcleos de processamento. O ESP32 é conhecido por sua eficiência energética, tornando-o ideal para aplicações que exigem baixo consumo de energia, como dispositivos portáteis e sensores remotos. Com sua versatilidade e facilidade de uso, o ESP32 se tornou uma escolha popular entre desenvolvedores e entusiastas de eletrônica para criar uma ampla gama de projetos conectados.

#### Baixando na IDE

Para baixar o suporte ao ESP32 na Arduino IDE, siga os seguintes passos:
1. Abra a Arduino IDE.
2. Vá para "File" (Arquivo) > "Preferences" (Preferências).
3. Na seção "Additional Boards Manager URLs" (URLs adicionais do Gerenciador de Placas), adicione a seguinte URL: `https://dl.espressif.com/dl/package_esp32_index.json`.
4. Clique  99em "OK" para salvar as preferências.
5. Em seguida, vá para "Tools" (Ferramentas) > "Board" > "Boards Manager" (Gerenciador de Placas).
6. Na barra de pesquisa, digite "ESP32" e selecione a opção "esp32 by Espressif Systems".
7. Clique em "Install" (Instalar) para baixar e instalar o suporte ao ESP32 na Arduino IDE.

#### Códigos

##### Loop básico para piscar um LED conectado ao pino 4 do ESP32

```cpp
#define PINO 4

void setup() {
  Serial.begin(115200);
  pinMode(PINO, OUTPUT);
  digitalWrite(PINO, LOW);
}

void loop() {
  digitalWrite(PINO, HIGH);
  delay(1000);
  digitalWrite(PINO, LOW);
  delay(1000);
}
```

##### Loop para controlar o estado do LED conectado ao pino 4 do ESP32 com comandos "LIGAR" e "DESLIGAR" enviados pela porta serial

```cpp
#define PINO 4

String comando = ""; // str
void setup() {
  Serial.begin(115200);
  pinMode(PINO, OUTPUT);
  digitalWrite(PINO, LOW);
}

void loop() {
  while(Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      comando.trim();

      if (comando == "LIGAR") {
        digitalWrite(PINO, HIGH);
        Serial.println("Pino 4 LIGADO");
      } else if (comando == "DESLIGAR"){
        digitalWrite(PINO, LOW);
        Serial.println("Pino 4 DESLIGADO");
      } else {
        Serial.println("Comando inválido");
      }
      comando = "";
    } else {
      comando += c;
    }
  }
}
```

