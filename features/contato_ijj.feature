#language: pt

@preencherformulario
Funcionalidade: Envio de Dados ao Formulário
    Cenário: Envio de dados com assunto quero ser facilitador
    
    Como usuário do instituto joga junto
    Quero preecher o formulário do contato
    Para que possa enviar o formulário preenchido

    Dado que estou na página do instituto joga junto
    Quando preencho o formulário de contato
    E aperto o botão de enviar
    Então os dados são recebidos com sucesso