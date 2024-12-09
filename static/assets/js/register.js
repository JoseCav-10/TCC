const cpf = document.getElementById("id_cpf");
const cartao_sus = document.getElementById("id_cartao_sus");
const password1 = document.getElementById("password1");
const password2 = document.getElementById("password2");
const fone = document.getElementById("id_fone");
const cep = document.getElementById("id_cep");
const endereco = document.getElementById("id_endereco");
const data_nascimento = document.getElementById("id_data_nascimento");
const sexo = document.getElementById("id_sexo");

let vetor = [cpf,cartao_sus,password1,password2,fone,cep,endereco,data_nascimento,sexo]

for (let i=0; i < vetor.length; i++){
    vetor[i].setAttribute('required', true);
};


cartao_sus.setAttribute('maxlength', '18');

cartao_sus.addEventListener('input', (event) => {
    let valor = cartao_sus.value;

    // Remove todos os caracteres que não sejam números
    valor = valor.replace(/\D/g, '');

    // Aplica a máscara de forma automática
    valor = valor.replace(/^(\d{3})(\d)/, '$1 $2'); 
    valor = valor.replace(/^(\d{3}) (\d{4})(\d)/, '$1 $2 $3');
    valor = valor.replace(/^(\d{3}) (\d{4}) (\d{4})(\d)/, '$1 $2 $3 $4');

    // Atualiza o campo de input com o valor formatado
    cartao_sus.value = valor;
});

cep.addEventListener('input', (event) => {
    let valor_cep = cep.value;

    // Remove todos os caracteres que não sejam números
    valor_cep = valor_cep.replace(/\D/g, '');

    // Aplica a máscara de forma automática
    valor_cep = valor_cep.replace(/^(\d{5})(\d)/, '$1-$2');

    // Atualiza o campo de input com o valor_cep formatado
    cep.value = valor_cep;
});


fone.setAttribute('maxlength', '15'); /* (88) 99999-9999*/

fone.addEventListener('input', (event) => {
    let valor_fone = fone.value;

    // Remove todos os caracteres que não sejam números
    valor_fone = valor_fone.replace(/\D/g, '');

    // Aplica a máscara de forma automática
   
    valor_fone = valor_fone.replace(/^(\d{2})(\d)/, '($1) $2'); // Coloca os parênteses no DDD
    valor_fone = valor_fone.replace(/(\d{4})(\d{4})$/, '$1-$2'); // Coloca o hífen no telefone fixo de 8 dígitos
    valor_fone = valor_fone.replace(/(\d{5})(\d)/, '$1-$2'); // Coloca o hífen no celular de 9 dígitos
    
    // Atualiza o campo de input com o valor_fone formatado
    fone.value = valor_fone;
});