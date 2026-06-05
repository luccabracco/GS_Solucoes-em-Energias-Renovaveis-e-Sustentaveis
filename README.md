#  Monitoramento de Sistemas Energéticos - Missão Espacial Experimental

## Participantes

- Lucca Bracco / RM: 570175
- João Pedro Ferrari / RM: 573037
- Vitor Nascimento / RM: 571873

##  Introdução
Este projeto é uma solução computacional desenvolvida para a Global Solution de Soluções em Energias Renováveis e Sustentáveis. O objetivo do sistema é monitorar as condições operacionais de uma missão espacial, focando no gerenciamento de energias renováveis e sustentáveis para garantir a segurança e eficiência do módulo.

##  Funcionalidades Implementadas
O programa foi desenvolvido em Python e oferece as seguintes capacidades:

* **Inserção Manual e Interativa de Dados:** O utilizador pode definir os valores exatos de temperatura, nível de energia renovável e estado de comunicação para cada ciclo da missão.
* **Validação de Dados Estrita:** Implementação de estruturas de controlo (`try/except`) que impedem o encerramento inesperado do programa caso sejam introduzidos caracteres inválidos (por exemplo, texto em campos numéricos).
* **Geração Automática de Alertas:** Identificação instantânea de anomalias com base nos dados introduzidos (ex: superaquecimento dos painéis ou falha na telemetria).
* **Tomada de Decisão Automatizada:** Estruturas lógicas que reagem imediatamente a situações críticas, simulando ações de mitigação (ex: desativação de sistemas não essenciais se a energia descer abaixo dos 30%)
* **Visualização Organizada:** Apresentação clara de relatórios de estado a cada ciclo operacional[cite: 14, 24].
* **Ciclo Contínuo de Operação:** Permite testar múltiplos cenários de forma consecutiva sem necessidade de reiniciar a aplicação.

## Link da Demonstração na Prática

