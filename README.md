Relatório

A função recebe uma string contendo um CPF (com ou sem pontos e traços), remove os caracteres especiais e realiza cálculos matemáticos para verificar se os dígitos verificadores (últimos dois números do CPF) estão corretos.
Foi adicionado console.log(validarCPF) para testar a função e ver o resultado dela na tela útil para verificação rápida.

Objetivos:
- Validar se um número de CPF informado é válido conforme as regras oficiais da Receita Federal do Brasil.
Limpeza do CPF:
- Remover qualquer caractere que não seja número (como “.” e “-”), garantindo que só restem dígitos.
Validação de formato:
- Verifica se o CPF tem exatamente 11 dígitos.
- Impede CPFs com todos os dígitos iguais, como 11111111111, que são inválidos.
Cálculo do primeiro dígito verificador:
- Multiplica os nove primeiros dígitos por pesos decrescentes (10 a 2).
- Calcula o resto da divisão (mod 11) para obter o primeiro dígito verificador.
- Se o resto for 10 ou 11, o dígito é 0.
Cálculo do segundo dígito verificador:
- Usa agora os 10 primeiros dígitos (incluindo o primeiro dígito verificador).
- Repete o processo anterior com pesos de 11 a 2.
- O resultado é o segundo dígito verificador.
Comparação final:
- Compara os dígitos calculados com os dois últimos dígitos do CPF informado.
Se ambos conferirem → CPF é válido 

B) Melhorias do projeto

A versão inicial do projeto apresentava apenas dois campos: Nome e Email.
Foram adicionados novos campos e aprimorou-se a interface.

- Senha (para autenticação);
- Data de Nascimento;
- Telefone;
- Endereço;
- Sexo (seleção em lista suspensa).
- Layout mais moderno e responsivo;
- Formulário centralizado e com cores neutras;
- Botão de envio com destaque;
- Validação de campos obrigatórios;
- Mensagem de cadastro realizado com sucesso.




C) Documentação do Sistema

Requisitos Funcionais:

RF001: O sistema deve permitir o cadastro de novos usuários.

RF002: O sistema deve validar os campos obrigatórios (nome, email e senha).

RF003: O sistema deve armazenar os dados em um banco de dados.

RF004: O sistema deve permitir a consulta dos usuários cadastrados.

RF005: O sistema deve permitir a atualização e exclusão de usuários.

RF006: O sistema deve garantir que o email seja único no cadastro.

Requisitos Não Funcionais

RNF001: O sistema deve ser acessível via navegador web.

RNF002: O layout deve ser responsivo (ajustar-se a diferentes tamanhos de tela).

RNF003: A interface deve ser simples e intuitiva.

RNF004: O sistema deve validar entradas de dados (ex: formato do email).

RNF005: O tempo de resposta para ações deve ser inferior a 2 segundos.

RNF006: O sistema deve armazenar as senhas de forma segura (criptografia).

Diagrama Entidade Relacionamento
<img width="1366" height="768" alt="Imagem1" src="https://github.com/user-attachments/assets/1ebe5bd3-5d86-4e13-8868-b36029286ac0" />

Diagrama de Caso de Uso
<img width="1366" height="768" alt="Imagem2" src="https://github.com/user-attachments/assets/37d9abb9-d255-4185-bbf5-5132ee634019" />






Descrição das linguagens

Java:
Java é uma linguagem de programação orientada a objetos, multiplataforma e amplamente utilizada no desenvolvimento de aplicações corporativas e web. Seu principal diferencial é a portabilidade — o código pode ser executado em diferentes sistemas operacionais sem modificações.

Objetivos principais:
Desenvolver aplicações seguras, robustas e portáveis.
Facilitar a criação de sistemas corporativos e web escaláveis.
Promover reutilização e manutenção fácil do código.

Focos dos projetos:
Sistemas empresariais (como ERPs e CRMs)
Aplicações web e APIs (Spring Boot, Jakarta EE)
Aplicativos Android
Microserviços e integrações entre sistemas

C:
C é uma linguagem de propósito geral, estruturada e de baixo nível, voltada para o máximo desempenho e controle sobre os recursos do computador. É considerada a base de muitas outras linguagens modernas e usada amplamente em sistemas que exigem eficiência.

Objetivos principais:
Garantir alto desempenho e uso otimizado de memória.
Proporcionar controle direto sobre o hardware e o sistema operacional.
Servir de base para o desenvolvimento de sistemas e softwares de infraestrutura.

Focos dos projetos:
Sistemas operacionais e drivers
Softwares embarcados e controladores (IoT, eletrônicos)
Compiladores e ferramentas de sistema
Jogos e aplicações de alto desempenho

COBOL:
COBOL (Common Business Oriented Language) é uma linguagem voltada para o processamento de dados comerciais e transações financeiras. É conhecida pela legibilidade e pela estabilidade, sendo muito utilizada em sistemas legados de bancos e governos.

Objetivos principais:
Processar grandes volumes de dados de forma confiável e precisa.
Garantir estabilidade e longevidade dos sistemas.
Facilitar a leitura e manutenção por equipes diversas.

Focos dos projetos:
Sistemas bancários, financeiros e governamentais
Processamento de folhas de pagamento e contabilidade
Aplicações em mainframes e sistemas legados
Manutenção e modernização de sistemas antigos

Requisitos funcionas em C:

RF001: Cadastrar Funcionário
O usuário pode adicionar nome, cargo e salário de um funcionário.

RF002: Listar Funcionários
O programa mostra todos os funcionários cadastrados.

RF003: Buscar Funcionário
O usuário pode procurar um funcionário pelo nome.
O programa mostra o cargo e salário se encontrar.

RF004: Limite de Funcionários
Pode cadastrar até 100 funcionários.

RF005: Menu de Opções
O programa mostra um menu com as opções:
1: Adicionar
2: Listar
3: Buscar
0: Sair

Requisitos não funcionas:

RNF001: Linguagem Utilizada
O programa é desenvolvido em linguagem C.
Usa apenas bibliotecas padrão: stdio.h e string.h.

RNF002: Execução em Terminal
O programa é feito para rodar em linha de comando (terminal).
Não tem interface gráfica (GUI).

RNF003: Entrada e Saída
O programa recebe dados do usuário via teclado.
Mostra resultados no console (tela de texto).

RNF004: Desempenho
O programa é rápido e leve, pois trabalha apenas com dados em memória.
Funciona bem para até 100 funcionários.

RNF005: Portabilidade
Pode ser compilado e executado em qualquer sistema operacional com
suporte a C (Windows, Linux, macOS).

Requisitos Funcionais em COBOL:

RF001: Cadastro de Alunos
O programa permite cadastrar nomes e notas de 5 alunos.

RF002: Cálculo da Média
Calcula a média das notas da turma automaticamente após o cadastro.

RF003:Exibição de Informações
Mostra uma lista com o nome e nota de cada aluno.
Exibe a média geral da turma ao final.

RF004: Interação via Terminal
O sistema interage com o usuário por mensagens no console, solicitando os
dados.

Requisitos Não Funcionais:

RNF001: Linguagem de Programação
O programa é escrito em COBOL.

RNF002: Interface de Texto
Usa linha de comando (terminal) para entrada e saída de dados (sem
interface gráfica).

RNF003: Capacidade Fixa
Suporta exatamente 5 alunos (definido por NUM-ALUNOS VALUE 5).

RNF004: Execução Sequencial
As ações do programa seguem uma ordem linear e simples: entrada de
dados, cálculo, exibição.

RNF005: Desempenho
O programa é leve e rápido, já que processa poucos dados e não usa
arquivos externos

Requisitos Funcionais em JAVA Sistema de Alunos:

RF001:Adicionar Aluno
O sistema permite cadastrar um aluno, fornecendo nome e nota final.

RF002: Listar Alunos
O sistema mostra todos os alunos cadastrados com seus respectivos nomes
e notas.

RF003: Buscar Nota de Aluno
O sistema permite buscar a nota de um aluno pelo nome exato.
Se o aluno existir, exibe a nota; se não, informa que o aluno não foi
encontrado.

RF004: Menu Interativo
O sistema exibe um menu com opções para o usuário escolher:
1: Adicionar aluno
2: Listar alunos
3: Buscar nota
0: Sair do programa

Requisitos não funcionais:

RNF001: Linguagem
O programa é implementado em Java.

RNF002: Interface
Utiliza interface de texto (terminal/console) para entrada e saída.

RNF003: Estrutura de Dados
Usa HashMap para armazenar o nome do aluno e sua nota.
Usa ArrayList para manter a ordem dos nomes cadastrados.

RNF004: Capacidade
Suporta cadastro de quantos alunos o usuário desejar (limitado pela memória
disponível).

RNF005: Usabilidade
O menu é simples, com opções numeradas para facilitar o uso.
As mensagens são claras para o usuário.

Requisitos Funcionais em JAVA Sistema de Votos:

RF001: Apresentar Opções de Votação
O sistema deve mostrar as opções disponíveis para votação (neste caso, 3
opções fixas).

RF002: Registrar Votos
O usuário pode votar em uma das opções digitando o número
correspondente.

RF003: Encerrar Votação
O usuário pode encerrar a votação digitando 0.

RF004: Validar Entrada
O sistema deve aceitar apenas números válidos dentro do intervalo (0 a
número de opções).
Caso a entrada seja inválida, deve exibir mensagem de erro e solicitar nova
entrada.

RF005: Exibir Resultado Final
Ao encerrar a votação, o sistema exibe o total de votos de cada opção.

Requisitos não funcionais:

RNF001: Linguagem
O programa é implementado em Java.

RNF002: Interface
Utiliza interface de texto (terminal/console) para interação com o usuário.

RNF003: Estrutura
Usa arrays para armazenar as opções e os votos correspondentes.

RNF004: Capacidade
Suporta 3 opções de voto fixas (podem ser alteradas no código).

RNF004: Usabilidade
Fornece mensagens claras para o usuário sobre o status do voto e erros de
entrada.

RNF005: Portabilidade
Pode ser executado em qualquer sistema com Java instalado.

Relatório das principais dificuldades de migração:

De COBOL para PYTHON:
COBOL usa uma forma diferente e mais antiga de programar, Python é mais
moderno e flexível. Os dados e arquivos são tratados de forma diferente,
então é difícil adaptar.
A sintaxe do COBOL é muito longa e formal, Python é curta e simples, o que
pode confundir. Programas COBOL antigos podem ser difíceis de entender
para converter.

De Java para Python:
Java é baseado em classes e regras rígidas, Python é mais livre e fácil. Em
Java, você sempre precisa dizer o tipo de dado, em Python não.
Algumas funções e bibliotecas de Java não existem em Python, então precisa
criar de novo. O jeito de tratar erros é diferente.
O código em Python é menos detalhado e usa indentação, pode ser estranho
para quem vem de Java.

De C para Python:
C usa muitos comandos para controlar a memória, Python faz isso sozinho. C
é rígido com tipos de dados, Python não precisa.
Algumas coisas feitas em C, como mexer direto com memória, não existem
em Python.
Programas em C são rápidos; em Python podem ficar mais lentos se não
cuidar.
Python é bom porque a linguagem é simples e flexível, mas precisa ajustar o
jeito de pensar o código, os dados e as funções.
