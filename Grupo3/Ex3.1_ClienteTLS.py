import socket
import ssl
from typing import Tuple

def conectar_servidor_tls(
    host: str = "127.0.0.1",
    porta: int = 8443,
    mensagem: str = "Olá, servidor TLS!",
    arquivo_certificado: str = "server.crt"
) -> None:
    """
    Conecta-se a um servidor TLS, envia uma mensagem e exibe a resposta (eco) retornada.

    :param host: Endereço (IP ou hostname) do servidor TLS.
    :param porta: Porta onde o servidor TLS está escutando.
    :param mensagem: Mensagem a ser enviada ao servidor.
    :param arquivo_certificado: Caminho para o certificado do servidor ou da CA usada para verificação.
                               Caso seja um certificado autoassinado, pode ser usado o próprio server.crt
                               para autorizar a conexão.
    """
    # Cria um contexto SSL para uso no lado cliente
    contexto_tls = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # Verifica se deseja validar o certificado do servidor
    # Para simplificar, usamos o próprio certificado autoassinado
    contexto_tls.load_verify_locations(arquivo_certificado)
    contexto_tls.verify_mode = ssl.CERT_REQUIRED

    with socket.create_connection((host, porta)) as sock:
        # Converte o socket em um socket seguro (TLS)
        with contexto_tls.wrap_socket(sock, server_hostname=host) as conexao_segurada:
            print("[Cliente] Conexão estabelecida com o servidor.")
            # Envia mensagem
            conexao_segurada.sendall(mensagem.encode('utf-8'))
            
            # Recebe a resposta (eco) do servidor
            resposta = conexao_segurada.recv(1024)
            print(f"[Cliente] Mensagem enviada: {mensagem}")
            print(f"[Cliente] Eco recebido: {resposta.decode('utf-8')}")

if __name__ == "__main__":
    conectar_servidor_tls()
