#!/usr/bin/python3
import pyfiglet
from termcolor import colored
from colorama import Fore
import socket
import urllib.request as url

def figure():
    #banner = pyfiglet.figlet_format("HACK ME")
    print((colored(pyfiglet.figlet_format("Reco"), color="green")))
    print(colored(Fore.RED + "********* Created By 0xCypher ************\n"))

def list():
    print("1. Convert Domain to IP\n2. Source Code Download\n0. Exit\n")
    nub = int(input("Press number: "))
    if nub==1:
        domain_to_ip_converter()
    elif nub==2:
        source_code_download()
    elif nub==0:
        exit()
        


def domain_to_ip_converter():

    domain = input("Enter Domain Name: ")
    ip = socket.gethostbyname(domain)
    print('IP Adress:',colored(ip,'green'))
    print("\n1. Again Convert Domain to IP\n2. Main Menu\n0. Exit\n")
    nub_d = int(input("Enter Number: "))
    if nub_d==1:
        domain_to_ip_converter()
    elif nub_d==2:
        list()
    elif nub_d==0:
        exit()

def source_code_download():
    print(colored("Example: https://example.com","blue"))
    website_name = input("Enter Website Name: ")
    src = url.urlopen(website_name)
    src_read = src.read()
    print("\n",src_read)

figure()
list()
