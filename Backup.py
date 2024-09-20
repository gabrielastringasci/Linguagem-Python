#Programa para fazer cópia de arquivos e pasta de um diretório para outro!
#Autor: Gabriela Aparecida Stringasci
#
#Janela para selecionar a pasta a ser copiada
import os
import tkinter.filedialog
import shutil
import datetime
import tkinter as tk

root = tk.Tk()
root.withdraw()

#Abrir caixa de diálogo para seleção de pasta
nome_pasta_selecionada = tkinter.filedialog.askdirectory()
lista_arquivos = os.listdir(nome_pasta_selecionada)


#fazer backup dos arquivos e pasta dentro da pasta original
nome_pasta_copia = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")
nome_completo_pasta_copia = os.path.join(nome_pasta_selecionada, nome_pasta_copia)

#criar a pasta de backup uma vez
os.mkdir(nome_completo_pasta_copia)

for arquivo in lista_arquivos:
    nome_completo_arquivo = os.path.join(nome_pasta_selecionada, arquivo)
    print(nome_completo_arquivo)
    nome_final_arquivo = os.path.join(nome_completo_pasta_copia, arquivo)
    print(nome_final_arquivo)
    if os.path.isfile(nome_completo_arquivo):  # Verificar se é um arquivo
        shutil.copy2(nome_completo_arquivo, nome_completo_pasta_copia)

print('Backup concluído com sucesso!')
