Dico_conversion = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M'}


def int_to_roman(N):
    Input, Result = str(N), ''
    while len(Input)>0:
        Result += (Dico_conversion['1'+'0'*(len(Input)-1)]*int(Input[0]) if Input[0] in ['1','2','3'] else '') + (Dico_conversion['1'+'0'*(len(Input)-1)] if Input[0]=='4' else '') + (Dico_conversion['5'+'0'*(len(Input)-1)] if Input[0] in ['4','5','6','7','8'] else '') + (Dico_conversion['1'+'0'*(len(Input)-1)]*(int(Input[0])-5) if Input[0] in ['6','7','8'] else '') + (Dico_conversion['1'+'0'*(len(Input)-1)]+Dico_conversion['1'+'0'*len(Input)] if Input[0]=='9' else '')
        Input = Input[1:]
    return(Result)
        
print(295, ' = ', int_to_roman(295)) # CCXCV
print(3983, ' = ', int_to_roman(3983)) # MMMCMLXXXIII
print(549, ' = ', int_to_roman(549)) # DXLIX
print(78, ' = ', int_to_roman(78)) # LXXVIII
