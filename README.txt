README

Esse gerador de seeds foi desenvolvido com o intuito de deixar o seeding do torneio local de Campinas de SSBU o menos enviesado possivel.

Inspirado no seed generator do start.gg, ele separa os jogadores em tiers baseado em suas posições no nosso ranking e deixa a ordem entre jogadores do mesmo tier aleatoria. Porem, empiricamente, o gerador do start.gg nao parecia verdadeiramente aleatorio. 

REQUERIMENTOS:
Python
	Bibliotecas: Pandas, Math, Numpy


COMO USAR:
1. Na pasta de PowerRankings, exportar o ranking do braacket mais recente
	IMPORTANTE: Assegurar que o ranking exportado contem todos os jogadores e nao so os X primeiros
2. Na pasta de Attendees colocar os tags dos jogadores participantes como esta no Braacket em qualquer ordem
3. No arquivo generate_seeds.py escolher a variancia e o numero de tiers desejados (Recomendado: variancia=1000, n_tiers=0)
4. Rodar o arquivo generate_seeds.py

FUNCIONAMENTO:

Clustering:
O algoritmo começa com todos os jogadores no mesmo tier e identifica os dois jogadores consecutivos com a maior distancia entre eles guardando essa distancia. Ele os divide em dois tiers diferentes. Logo ele procura o maior tier e verifica se a distancia entre o melhor e o pior jogador e maior que a distancia armazenada. Se for maior ele acha a maior distancia dentro desse tier e o divide em dois, voltando a buscar o maior tier. Caso a distancia for menor ele retorna a buscar a maior distancia entre dois jogadores do mesmo tier. Esse algoritmo se repete ate que o numero de tiers desejado seja obtido. O usuario pode escolher o numero de tiers desejado, mas o valor recomendado e do teto da metade dos participantes do torneio. Caso nenhum valor seja escolhido pelo usuario, o valor recomendado sera calculado e usado.

Aleatorizacao:
Apos o clustering em tiers os jogadores sao reordenados dentro dos seus tiers para dar uma variedade aos torneios. Isso se da somando um numero aleatorio a sua pontuacao e reordenando baseado primeiro em tiers e segundo em pontuacao. O numero e escolhido aleatoriamente entre -x e x, onde x e definido pelo usuario. Quanto maior o x mais aleatoria fica a ordenacao entre os jogadores do mesmo tier, quanto menor o x menos aleatoria fica a ordenacao. Empiricamente, para o tamanho dos Stations em 2022 um valor de 1000 deixa os tiers totalmente aleatorios, e um valor de 150 deixa com pouquissima variacao. Eu acredito que totalmente aleatorio e mais interessante pois algum semblante de ordem ja esta sendo mantida pelo clustering de qualquer maneira.

