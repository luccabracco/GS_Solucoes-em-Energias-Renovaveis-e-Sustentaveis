class ModuloEspacial:
    def __init__(self, nome):
        self.nome = nome
        self.temperatura = 0.0
        self.nivel_energia = 0.0
        self.comunicacao_ok = True

    def inserir_dados_manuais(self):
        print("\n      === INSERÇÃO DE DADOS DO MÓDULO ===")
        try:
            self.temperatura = float(input("Digite a temperatura atual (°C): "))
            self.nivel_energia = float(input("Digite o nível de energia (0 a 100%): "))

            status_com = input("A comunicação está operante? (s/n): ").strip().lower()
            self.comunicacao_ok = True if status_com == 's' else False
            return True
        except ValueError:
            print("\nEntrada inválida! Por favor, insira apenas números para temperatura e energia.")
            return False

    def analisar_dados_e_decidir(self):
        alertas = []
        acoes = []

        if self.nivel_energia < 30.0:
            alertas.append("CRÍTICO! Nível de energia sustentável abaixo de 30%!")
            acoes.append("Desativando sistemas de suporte não essenciais para conservação de energia.")

        if self.temperatura > 45.0:
            alertas.append("Superaquecimento detectado nos painéis.")
            acoes.append("Acionando sistema de resfriamento autônomo e redirecionando escudos térmicos.")

        if not self.comunicacao_ok:
            alertas.append("Falha na telemetria e comunicação com a base da Terra.")
            acoes.append("Iniciando protocolo de reinicialização da antena principal.")

        return alertas, acoes


def iniciar_missao():
    modulo = ModuloEspacial("Módulo de Sustentabilidade Hélios-1")
    print("\n" + "=" * 50)
    print("   INICIANDO SISTEMA DE MONITORAMENTO ESPACIAL")

    print("=" * 50)
    print("            >>> MENU PRINCIPAL <<<")
    print("=" * 50 + "\n")
    print("1 - Inserir dados operacionais")
    print("0 - Sair do programa")

    while True:
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '0':
            print("\nEncerrando o sistema de monitoramento.")
            return
        elif opcao == '1':
            break
        else:
            print("\n[ERRO] Opção inválida. Digite 1 para iniciar ou 0 para sair.")

    ciclo = 1
    while True:
        print(f"\n        >>> [ CICLO DE OPERAÇÃO {ciclo} ] <<<")

        sucesso = modulo.inserir_dados_manuais()

        if not sucesso:
            continue

        print()
        print("         === RELATÓRIO DO SISTEMA ===")
        print(f"Módulo Monitorado : {modulo.nome}")
        print(f"Temperatura       : {modulo.temperatura:.2f}°C")
        print(f"Energia Renovável : {modulo.nivel_energia:.2f}%")
        print(f"Status Conexão    : {'ONLINE' if modulo.comunicacao_ok else 'OFFLINE'}")

        alertas, acoes = modulo.analisar_dados_e_decidir()

        if alertas:
            print("\nALERTAS DO SISTEMA:")
            for alerta in alertas:
                print(f"  - {alerta}")

        if acoes:
            print("DECISÕES AUTOMATIZADAS:")
            for acao in acoes:
                print(f"  - {acao}")

        if not alertas and not acoes:
            print("\nStatus Operacional: Estável. Nenhuma intervenção necessária.")

        print("-" * 50)

        continuar = input("\nDeseja inserir dados para um novo ciclo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nEncerrando o sistema de monitoramento.")
            break

        ciclo += 1


if __name__ == "__main__":
    iniciar_missao()