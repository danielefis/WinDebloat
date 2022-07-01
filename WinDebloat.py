# -*- coding: utf-8 -*-
import subprocess

'''
Script para remover manualmente aplicativos padrão Windows 10/11
'''


print("Você removerá manualmente aplicações e pacotes com [1- para SIM] e [2- para NÃO].")
manual = int(input("Continuar? [1-SIM] [2-NÃO]: "))
if manual == 1:
    escolha = int(input("Remover Cortana? [1-SIM] [2-NÃO]: "))
    if escolha == 1:
            subprocess.Popen(["powershell","Get-AppxPackage *Microsoft.549981C3F5F10* | Remove-AppxPackage* | Remove-AppxPackage"])
else:
    exit()

manual = int(input("Remover Hub de Comentários? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsFeedbackHub* | Remove-AppxPackage"])

manual = int(input("Remover Mapas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsMaps* | Remove-AppxPackage"])

manual = int(input("Remover Microsoft To Do? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Todos* | Remove-AppxPackage"])

manual = int(input("Remover Filmes e TV? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *ZuneVideo* | Remove-AppxPackage"])

manual = int(input("Remover Office? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage"])

manual = int(input("Remover Paint? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Paint* | Remove-AppxPackage"])

manual = int(input("Remover Músicas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *ZuneMusic* | Remove-AppxPackage"])

manual = int(input("Remover Microsoft Notícias? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *BingNews* | Remove-AppxPackage"])

manual = int(input("Remover Bloco de Notas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsNotepad* | Remove-AppxPackage"])

manual = int(input("Remover OneDrive? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *OneDriveSync* | Remove-AppxPackage"])

manual = int(input("Remover PowerAutomate? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *PowerAutomateDesktop* | Remove-AppxPackage"])

manual = int(input("Remover Teams/Chat? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","	Get-AppxPackage *Teams* | Remove-AppxPackage"])