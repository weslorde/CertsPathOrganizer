import os
import shutil


def listar_arquivos_caminho(caminho):
    try:
        lista_arquivos = os.listdir(caminho)
        #print(f"Arquivos em '{caminho}':")
        for pastaCerts in lista_arquivos:
        # pastaCerts = lista_arquivos[0]
        # if(1):
            try:
                caminho_completo = os.path.join(caminho, pastaCerts)
                lista_certs = os.listdir(caminho_completo)
                PastaCopiaCert = os.path.join(caminho_completo, "Cert")
                try: os.makedirs(PastaCopiaCert)
                except: pass
                PastaCopiaFlutter = os.path.join(PastaCopiaCert, "Flutter")
                try: os.makedirs(PastaCopiaFlutter)
                except: pass
                for filename in lista_certs:
                    filePath = os.path.join(caminho_completo, filename)
                    if(filename[-3:] == "crt"):
                        print("crt")
                        CaminhoCopia = os.path.join(PastaCopiaCert, "ChurrasTech.cert.der")
                        shutil.copy(filePath, CaminhoCopia)
                        ###
                        CaminhoCopia = os.path.join(PastaCopiaFlutter, "device.pem.crt")
                        shutil.copy(filePath, CaminhoCopia)

                    elif(filename[-15:] == "private.pem.key"):
                        print("private")
                        CaminhoCopia = os.path.join(PastaCopiaCert, "ChurrasTechPrivate.key.der")
                        shutil.copy(filePath, CaminhoCopia)
                        ###
                        CaminhoCopia = os.path.join(PastaCopiaFlutter, "private.pem.crt")
                        shutil.copy(filePath, CaminhoCopia)

                    elif(filename[-7:] == "CA1.pem"):
                        print("CA1")    
                        CaminhoCopia = os.path.join(PastaCopiaFlutter, "rootCA.pem")
                        shutil.copy(filePath, CaminhoCopia)
                    ###
                    print("                       "+pastaCerts+" foi")
            except: print("                       "+pastaCerts+" nao foi")

    except FileNotFoundError:
        print("Erro: Pasta não encontrada.")
    except PermissionError:
        print("Erro: Permissão negada para acessar a pasta.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exemplo de uso:
pasta = 'D:/OneDrive - FEI/Trabalho_Atividades_Projetos/ProjetoEsp32/AWS CERTIFICADOS/ChurrasTechCertificates/1ContaNova'

listar_arquivos_caminho(pasta)

