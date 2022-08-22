from re import sub

def validarCPF(num):
    sum, validacao = 0, 0
    for i in range(10,1,-1):
        sum += int(num[10-i]) * i
    
    validacao = 11 - (sum % 11)
    validacao =  0 if validacao > 9 else validacao
    
    if validacao == int(num[9]):
        sum = 0 #
        for j in range(11,1,-1):  # 11,2,-1
            sum += int(num[11-j]) * j #

        # sum += validacao * 2
        validacao = 11 - (sum % 11)
        validacao = 0 if validacao > 9 else validacao
        
        if validacao == int(num[10]):
            print("CPF Válido")
            
        else: print("CPF Inválido")
    else: print("CPF Inválido")

cpf = str(input("Digite seu CPF:\n"))
# Remove os traços, pontos e espaços do CPF 
cpf = sub(r"[-.\s]", "", cpf)

print(validarCPF(cpf))
