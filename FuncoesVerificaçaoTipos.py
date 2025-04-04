# Funçao para conferir o tipo

def ConferirTipoInt(pergunta):

    while True: 
        try: # Se o tipo for errado
            valor = int(input(pergunta))
            return valor
       
        except ValueError:
            print("Digite um tipo valido! ")
        
    
def ConferirTipoFloat(pergunta):
    while True: 
        try: # Se o tipo for errado
            valor = float(input(pergunta)) 
            return valor 
        except ValueError:
            print("Digite um tipo valido! ")
