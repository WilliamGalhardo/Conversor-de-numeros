print('='*100)
print('Seja bem vindo ao nosso Conversor de números Decimais para: Binário, Octal e Hexadecimal')
print('='*100)
resposta = 'Sim'

while resposta == 'Sim' or resposta == 'sim':
    print('Opções Disponiveis: \n \n', '[1] Binário\n', '[2] Octal\n', '[3] Hexadecimal\n', '[4] Sobre\n', '[5] Sair')
    print()
    opcao = int(input('Escolha a opção desejada: '))

    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('='*35)
        print('Opção inválida')
        print('Tente novamente')
        print('='*35)
    resposta = 'Sim'
    if opcao == 1:
        while resposta == 'Sim' or resposta == 'sim':
            n = int(input('Digite um número DECIMAL que você deseja converter para BINÁRIO: '))
            x = ''

            while n != 0:
                x = x+str(n % 2)
                n = n//2
            print('O número DECIMAL em BINÁRIO é: ')

            for i in range(len(x)-1, -1, -1):
                print(x[i], end='')
            print()
            resposta = str(input('\nDeseja realizar uma outra conversão para BINÁRIO?  (Sim/Não)\n'))
    resposta = 'Sim'

    if opcao == 2:
        while resposta == 'Sim' or resposta == 'sim':
            n = int(input('Digite um número DECIMAL que você deseja converter para OCTAL: '))
            x = ''

            while n != 0:
                x = x+str(n % 8)
                n = n//8
            print('O número DECIMAL em OCTAL é: ')

            for i in range(len(x)-1, -1, -1):
                print(x[i], end='')
            print()
            resposta = str(input('\nDeseja realizar uma outra conversão para OCTAL? (Sim/Não)\n'))
            print()
    resposta = 'Sim'
    if opcao == 3:
        while resposta == 'Sim' or resposta == 'sim':
            n = int(input('Digite um número DECIMAL que você deseja converter para HEXADECIMAL: '))
            x = ''

            while n != 0:
                r = n % 16
                if int(r) == 10:
                    x += 'A'
                elif int(r) == 11:
                    x += 'B'
                elif int(r) == 12:
                    x += 'C'
                elif int(r) == 13:
                    x += 'D'
                elif int(r) == 14:
                    x += 'E'
                elif int(r) == 15:
                    x += 'F'
                else:
                    x += str(r)
                n = n//16
            print('O número DECIMAL em HEXADECIMAL é: ')

            for i in range(len(x)-1, -1, -1):
                print(x[i], end='')
            print()
            resposta = str(input('\nDeseja realizar uma outra conversão para HEXADECIMAL? (Sim/Não)\n'))
            print()
    resposta = 'Sim'

    if opcao == 4:
        print()
        print('='*70)
        print('Projeto Interdiciplinar - Universidade Cruzeiro do Sul')
        print('='*70)
        print('Intergrantes do Grupo:')
        print('Nome:Gabriel Chaves Medeiro RGM:29751161')
        print('Nome:Guilherme Koga Pereira RGM:29678056')
        print('Nome:Lucas Dos Santos Antunes RGM:29682231')
        print('Nome:Vitor Suave Rodrigues RGM:29987451')
        print('Nome:William Ferreira Galhardo RGM:29381959')
        print('=' * 70)
        resposta = str(input('\nDeseja realizar uma conversão? (Sim/Não)\n'))
        print()
        if resposta == 'Não' or resposta == 'não' or resposta == 'Nao' or resposta == 'nao':
            print()
            print('=' * 70)
            print('Obrigado por utilizar o nosso conversor de bases!!')
            print('=' * 70)
            print('Até outro dia!!')
            break
    if opcao == 5:
        print('=' * 70)
        print('Obrigado por utilizar o nosso conversor de bases!!')
        print('=' * 70)
        print('Até outro dia!!')
        break
