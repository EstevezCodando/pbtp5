#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import ARP, sniff

mapeamentos_arp = {}

def processar_pacote_arp(pacote):
    """
    Função callback para tratar pacotes ARP recebidos.
    Verifica se o IP (pacote.psrc) já foi mapeado para outro MAC antes.
    Se houver divergência, emite alerta indicando possível ARP spoofing.
    """
    if pacote.op == 2:  # ARP Reply (is-at)
        ip_origem = pacote.psrc
        mac_atual = pacote.hwsrc

        if ip_origem in mapeamentos_arp:
            mac_antigo = mapeamentos_arp[ip_origem]
            if mac_antigo != mac_atual:
                print(f"[ALERTA] Possível ARP Spoofing detectado para IP {ip_origem}!")
                print(f"         MAC antigo: {mac_antigo}, MAC atual: {mac_atual}")
        # Atualiza ou insere o mapeamento IP -> MAC
        mapeamentos_arp[ip_origem] = mac_atual

def main():
    """
    Inicia a captura de pacotes ARP e chama processar_pacote_arp() para cada pacote capturado.
    """
    print("Monitorando pacotes ARP para detectar possíveis ataques de ARP Spoofing...")
    # Usa o filtro para capturar apenas pacotes ARP
    sniff(filter="arp", prn=processar_pacote_arp, store=False)

if __name__ == "__main__":
    main()
