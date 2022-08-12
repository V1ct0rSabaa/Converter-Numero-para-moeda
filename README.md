# Converter-Numero-para-moeda
## Introdução
Um programa de CLI/prompt de comando que recebe um valor numérico e retorna quantas cédulas e moedas seriam suficientes para representar o valor recebido, semelhante a um caixa eletrônico onde o cliente digita 200 reais e recebe 4 notas de cinquenta reais. 
A ideia para este programa veio inicialmente do projeto [Dollars To Cents](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Dollars-To-Cents-App.md)
## Detalhes do código
O código fonte foi desenvolvido em um único arquivo, com uma filtragem básica de input de dados através de try except e utilizando int invés de float devido a instabilidade de casas decimais, por exemplo se um desenvolvedor define uma variável n1 = 3.15, o valor armazenado pode ser na verdade 3.15092, logo essa falta de precisão pode se acumular ao longo das operações aritméticas gerando algum erro, devolvendo ao usuário um valor errado, uma questão bem problemática em cenários financeiros.
