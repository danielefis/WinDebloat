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
            print("Removido!")
else:
    exit()

manual = int(input("Remover Hub de Comentários? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsFeedbackHub* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Mapas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsMaps* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Vincular ao Celular? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *YourPhone* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Solitaire Collection? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *MicrosoftSolitaireCollection* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Xbox e aplicativos relacionados? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Xbox* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Microsoft To Do? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Todos* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Filmes e TV? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *ZuneVideo* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Office? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Paint? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Paint* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Músicas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *ZuneMusic* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Microsoft Notícias? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *BingNews* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Bloco de Notas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsNotepad* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Clima? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *BingWeather* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Email? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *microsoft.windowscommunicationsapps* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover OneDrive? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *OneDriveSync* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover PowerAutomate? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *PowerAutomateDesktop* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Teams/Chat? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Teams* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Notas Autoadesivas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *MicrosoftStickyNotes* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Gravador de Voz? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsSoundRecorder* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Spotify? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *SpotifyAB.SpotifyMusic* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Microsoft Edge? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *MicrosoftEdge* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Calculadora? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsCalculator* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Alarmes e Relógio? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *WindowsAlarms* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Obter Ajuda? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *GetHelp* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Pessoas Microsoft? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *People* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Fotos? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Windows.Photos* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Câmera? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Microsoft.WindowsCamera* | Remove-AppxPackage"])
    print("Removido!")

manual = int(input("Remover Aplicativo Dicas? [1-SIM] [2-NÃO]: "))
if manual == 1:
    subprocess.Popen(["powershell","Get-AppxPackage *Microsoft.Getstarted* | Remove-AppxPackage"])
    print("Removido!")
