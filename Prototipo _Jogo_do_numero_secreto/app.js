//Aqui esta o codigo pra fazer um mini jogo com JS
alert("Boas vindas ao jogo do número secreto");
let numeroMaximo = 100;
let numeroSecreto =  cost = parseInt(Math.random() * numeroMaximo + 1); 
   console.log(numeroSecreto)
let chute  
let tentativas = 1;
// enquanto chute não for igual ao n.s
while (chute != numeroSecreto) {
    chute = prompt(`Escolha um numero entre 1 a ${numeroMaximo}`);  
// se o chute for igual ao numero secreto
    if (chute == numeroSecreto) {
        break;
    }else {
     if (chute > numeroSecreto) {
        alert(`O numero secreto é menor que o ${chute}`);
        } else {
        alert(`O numero secreto é maior que o ${chute}`);
    }
    tentativas++; 
}
}
let palavraTentatvia = tentativas > 1 ? "tentativas" : "tentativa"
alert(`Isso aí! Você acertou número secreto ${numeroSecreto} em ${tentativas} ${palavraTentatvia}.`);
