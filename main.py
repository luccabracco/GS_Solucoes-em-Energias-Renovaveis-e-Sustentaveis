import random
import time


class ModuloEspacial:
    def __init__(self, nome):
        self.nome = nome
        self.temperatura = 22.0
        self.nivel_energia = 100.0
        self.comunicacao_ok = True

    def ler_sensores_simulados(self):
        self.temperatura += random.uniform(-2.0, 15.0)
        self.nivel_energia -= random.uniform(1.0, 25.0)
        self.comunicacao_ok = random.choice([True, True, True, True, False])

    def analisar_dados_e_decidir(self):
        alertas = []
        acoes = []

        if self.nivel_energia < 30.0:
            alertas.append("ALERTA CRÍTICO: Nível de energia sustentável abaixo de 30%!")
            acoes.append("AÇÃO: Desativando sistemas de suporte não essenciais para conservação de energia.")

        if self.temperatura > 45.0:
            alertas.append("ALERTA: Superaquecimento detectado nos painéis.")
            acoes.append("AÇÃO: Acionando sistema de resfriamento autônomo e redirecionando escudos térmicos.")

        if not self.comunicacao_ok:
            alertas.append("AVISO: Falha na telemetria e comunicação com a base da Terra.")
            acoes.append("AÇÃO: Iniciando protocolo de reinicialização da antena principal.")

        return alertas, acoes


def iniciar_missao():
    modulo = ModuloEspacial("Módulo de Sustentabilidade Hélios-1")
    print("=" * 50)
    print(" INICIANDO SISTEMA DE MONITORAMENTO ESPACIAL ")
    print("=" * 50)

    for ciclo in range(1, 6):
        print(f"\n>>> [ CICLO DE OPERAÇÃO {ciclo} ] <<<")
        modulo.ler_sensores_simulados()

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
        time.sleep(2)


if __name__ == "__main__":
    iniciar_missao()