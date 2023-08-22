MORSE_CODE = {  'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ': '|'}

print("======================================\nWelcome to morse code translator\n======================================")
game = 1
print('write (quit) if you want exit form programme')
while game == 1 :

    def msg(massage):
        ListLitter = []
        for litter in massage:
            if litter in MORSE_CODE:
                ListLitter.append(litter)
            elif litter == ' ':
                ListLitter.append(' ')
            else:
                print('your massage is wrong !')
        return ListLitter

    def morse(word):
        ListMorse = []
        for litter in word :
            if litter in MORSE_CODE:
                ListMorse.append(MORSE_CODE[litter])
        return ListMorse

    def Encrypt(encmsg):
        word = ''
        BeforeEnc = msg(encmsg) 
        AfterEnc = morse(BeforeEnc)
        for n in AfterEnc :
            word += n + ' '
        return word 


    msge = input('Enter your massage : ').upper()
    if msge == 'QUIT':
        game = 0
    else:
        print(f'your massage : \n{Encrypt(msge)}')

    

input('the programme is finished ... ')