import requests
import time
import schedule
import os

# Função para buscar a cotação do Euro em relação ao Real
def get_euro_to_real_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")  # API pública de exemplo
        data = response.json()
        rate = data['rates']['BRL']  # Obtém a taxa de Euro para Real
        return rate
    except Exception as e:
        print("Erro ao buscar cotação:", e)
        return None

# Função para emitir um alerta sonoro e uma mensagem
def emitir_alarme(rate):
    print(f"\n*** Alerta! A cotação do Euro caiu para R${rate:.2f} ***\n")
    # Tocar um som (funciona em alguns terminais)
    try:
        # No Windows, use 'beep' no lugar de 'echo' se preferir
        if os.name == 'nt':
            os.system('echo \a')  # Som de alarme em terminais compatíveis
        else:
            os.system('echo -e "\\a"')  # Alarme sonoro no terminal Linux/Mac
    except Exception as e:
        print("Não foi possível emitir som, apenas exibindo a mensagem:", e)

# Função para monitorar a cotação
def monitor_euro_to_real():
    rate = get_euro_to_real_rate()
    if rate and rate < 6.13:
        emitir_alarme(rate)
    else:
        print(f"Cotação atual do Euro: R${rate:.2f}")

# Agendar a verificação a cada 1 hora
schedule.every(1).hours.do(monitor_euro_to_real)

# Loop para manter o bot rodando
print("Monitorando a cotação Euro/Real...")
while True:
    schedule.run_pending()
    time.sleep(60)
