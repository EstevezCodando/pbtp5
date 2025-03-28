import socket
import ssl
from typing import Tuple

def iniciar_servidor_tls(
    host: str = "0.0.0.0",
    porta: int = 8443,
    arquivo_certificado: str = "server.crt",
    arquivo_chave: str = "server.key"
) -> None:
    """
    Inicia um servidor TLS (echo server) que aguarda conexões,
    estabelece uma comunicação segura e ecoa os dados recebidos de cada cliente.

    :param host: Endereço no qual o servidor irá escutar (por padrão, 0.0.0.0).
    :param porta: Porta na qual o servidor irá escutar (por padrão, 8443).
    :param arquivo_certificado: Caminho para o arquivo de certificado (server.crt).
    :param arquivo_chave: Caminho para o arquivo de chave privada (server.key).
    """
    # Cria um contexto SSL para uso no lado servidor
    contexto_tls = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    contexto_tls.load_cert_chain(certfile=arquivo_certificado, keyfile=arquivo_chave)

    # Cria socket TCP básico
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as servidor_socket:
        servidor_socket.bind((host, porta))
        servidor_socket.listen(5)
        print(f"Servidor TLS iniciado em {host}:{porta} - Aguardando conexões...")

        while True:
            # Aguarda conexão de um cliente
            conexao_nao_segurada, endereco_cliente = servidor_socket.accept()
            try:
                # Converte a conexão em TLS
                with contexto_tls.wrap_socket(conexao_nao_segurada, server_side=True) as conexao_segurada:
                    print(f"[Servidor] Conexão estabelecida com {endereco_cliente}")

                    while True:
                        dados = conexao_segurada.recv(1024)
                        if not dados:
                            break  # Cliente encerrou a conexão
                        print(f"[Servidor] Recebido: {dados.decode('utf-8')}")
                        # Ecoa (retorna) os dados para o cliente
                        conexao_segurada.sendall(dados)
            except ssl.SSLError as e:
                print(f"[Servidor] Erro SSL: {e}")
            except ConnectionError:
                print("[Servidor] Conexão interrompida pelo cliente.")
            finally:
                conexao_nao_segurada.close()

if __name__ == "__main__":
    iniciar_servidor_tls()
