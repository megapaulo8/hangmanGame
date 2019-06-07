import requests
from random import randint
from string import punctuation

guillotine = 
['''
  +-----+
  |     |
        |
        |
        |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
        |
        |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
  |     |
        |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
 /|     |
        |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
 /|\    |
        |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
 /|\    |
 /      |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  0     |
 /|\    |
 / \    |
        |
        |
=========
'''
,
'''
  +-----+
  |     |
  X     |
 /|\    |
 / \    |
        |
        |
=========
'''
]

def paint():
    if len(errors) == 0:
        print (guillotine[0])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 1:
        print (guillotine[1])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 2:
        print (guillotine[2])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 3:
        print (guillotine[3])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 4:
        print (guillotine[4])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 5:
        print (guillotine[5])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 6:
        print (guillotine[6])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) == 7:
        print (guillotine[7])
        print ('Letra: {} \nErros: {}'.format(trace,errors))
    if len(errors) > 7:
        print (guillotine[8])
        print('Voce Perdeu!!! A word era: '+ word)
        answer = input('Quer jogar novamente?(S/N): ')
        try_again(answer)

def sorting():
    print('Aguarde, estamos pensando na word...')
    url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
    p = requests.get(url)
    words = p.text.lower()
    words = words.split()
    qtd = len(words)
    sort = randint(0,qtd)
    return words[sort]

def kicking(last_word):
    num = 0
    
    while num != 2:
        if last_word.isalpha():
            last_word = last_word[0].lower()
            num = 2
            return last_word
        else:
            last_word = input("Digite uma Letra: ") 

def hit_everything():
    if trace == letters:
        return True
    if len(errors) > 7:
        return False

answer = True

def try_again():
    answ = input('Deseja jogar novamente? (S/N): ')
    if answ == 'S':
        return True
    else:
        if answ == 'N':
            return False

while answer != False:
    errors=[], letters=[], trace=[]
    word = sorting()
    for i in range(len(word)):
        letters.append(word[i])
        trace.append('_')

    while trace != letters and len(errors) <= 7:
        paint()
        kick = input('Digite alguma letra: ')
        kick = kicking(kick)
        if kick in errors or kick in trace:
            print("Letra repetida")
            pass
        elif kick in punctuation:
            print("Caractere inválido")
        elif kick in word:
            for t in range(len(letters)):
                if kick == letters[t]:
                    trace[t]=letters[t]
        else:
            errors.append(kick)
        if trace == letters:
            print('Parabéns!!! Você acertou, a palavra era {}'.format(word))
            answer = try_again()
        if len(errors) > 7:
            print (guillotine[8])
            print('Infelizmente você perdeu, a palavra era: '.format(word))
            answer = try_again()

