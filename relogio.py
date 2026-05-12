import time
import os
import platform

def shutdown():
    sistema = platform.system().lower()

    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")

        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown -h now")

        else:
            print("Sistema operacional não suportado para shutdown automático.")

    except Exception as e:
        print(f"Erro ao tentar desligar o computador: {e}")


def temporizador():
    print("=== TEMPORIZADOR ===")

    try:
        segundos = int(input("Digite o tempo em segundos para o temporizador: "))

        while segundos > 0:
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}:{secs:02d}"

            bip = "\a" if 0 < segundos <= 10 else ""

            print(f"\rTempo restante: {timer} {bip}", end="", flush=True)

            time.sleep(1)
            segundos -= 1

        print("\n\nIniciando o desligamento automático...")

        shutdown()

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

    except KeyboardInterrupt:
        print("\nTemporizador interrompido pelo usuário.")


if __name__ == "__main__":
    temporizador()