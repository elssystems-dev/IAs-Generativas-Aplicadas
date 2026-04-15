import serial #Leitura da porta serial
import serial.tools.list_ports #pip install pyserial
import time
# import IAcomROI

def listar_portas_seriais() -> list:
    return [porta.device for porta in serial.tools.list_ports.comports()]

def abrir_porta_serial(porta: str, baudrate: int = 115200, timeout: float = 1.0) -> serial.Serial:
    serial_port = serial.Serial(porta, baudrate, timeout=timeout)
    time.sleep(2)
    return serial_port

def ler_do_arduino(serial_port: serial.Serial) -> str:
    if not serial_port.isOpen():
        raise serial.SerialException("A porta serial não está aberta")

    linha = serial_port.readline().decode("utf-8", errors="ignore")
    return linha

def escrever_para_arduino(serial_port: serial.Serial, mensagem: str) -> None:
    if not serial_port.isOpen():
        raise serial.SerialException("A porta serial não está aberta")
    payload = mensagem.strip() + "\n"
    serial_port.write(payload.encode("utf-8"))
    serial_port.flush()

def main() -> None:
    print("Portas seriais disponíveis")
    for porta in listar_portas_seriais():
        print(f"- {porta}")
    porta_escolhida = input("Digite uma porta serial: ")
    baudrate = input("Digite a velocidade (115200): ")

    try:
        serial_port = abrir_porta_serial(porta_escolhida, int(baudrate))
        print(f"Conectado em {porta_escolhida} com {baudrate} bps")
    except Exception as e:
        print(f"Erro ao abrir a porta serial: {e}")
        return

    try:
        while True:
            comando = input("Digite uma comando (LIGAR/DESLIGADO): ")
            if comando == "LIGAR":
                escrever_para_arduino(serial_port, comando)
                print("Enviado. Aguardando resposta...")
                resposta = ler_do_arduino(serial_port)
                if resposta:
                    print(f"Arduino retornou {resposta}")
                else:
                    print("Nenhuma resposta recebida")
            elif comando == "DESLIGADO":
                escrever_para_arduino(serial_port, comando)
                print("Enviado. Aguardando resposta...")
                resposta = ler_do_arduino(serial_port)
                if resposta:
                    print(f"Arduino retornou {resposta}")
                else:
                    print("Nenhuma resposta recebida")
            else:
                print("Digite um comando válido")
    except KeyboardInterrupt:
        print("\nEncerrando...")
    finally:
        serial_port.close()
        print("Porta serial fechada.")

if __name__ == "__main__":
    main()

