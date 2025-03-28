#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import ARP, Ether, srp

def varrer_rede_arp(intervalo_rede: str) -> None:
    """
    Realiza uma varredura ARP no intervalo de IPs especificado,
    exibindo os hosts que respondem (IP e MAC).
    
    :param intervalo_rede: Intervalo de IPs (ex: "192.168.1.0/24").
    """
    # Cria pacote ARP de broadcast (MAC de destino como "ff:ff:ff:ff:ff:ff")
    pacote_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote_arp = ARP(pdst=intervalo_rede)
    pacote_combinado = pacote_broadcast / pacote_arp

    # Envia e recebe respostas ARP
    respostas, _ = srp(pacote_combinado, timeout=2, verbose=0)

    # Exibe IP e MAC de cada host que respondeu
    for _, resposta_arp in respostas:
        ip_host = resposta_arp.psrc
        mac_host = resposta_arp.hwsrc
        print(f"IP: {ip_host}, MAC: {mac_host}")

def main() -> None:
    """
    Função principal para executar a varredura ARP.
    """
    intervalo = "192.168.1.0/24"  # Ajuste conforme necessário
    varrer_rede_arp(intervalo)

if __name__ == "__main__":
    main()