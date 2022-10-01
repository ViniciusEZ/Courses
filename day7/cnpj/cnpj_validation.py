def cnpj_validator(cnpj):
    try:
        no_punc = remove_punc(cnpj)
        if sequence(no_punc):
            return "Invalid!"
        cnpj_test = no_punc[:-2]
        index = 0
        n = 5
        s = 0
        for c in range(25):
            s += int(cnpj_test[index]) * n
            if n == 2:
                n = 10
            if index == len(cnpj_test) - 1:
                if 11 - (s % 11) < 9:
                    cnpj_test += str(11 - (s % 11))
                else:
                    cnpj_test += str(0)
                index = 0
                s = 0
                n = 6
                continue
            n -= 1
            index += 1
        return 'Valid!' if cnpj_test == no_punc else 'Invalid!'
    except Exception as e:
        return 'Invalid!'



def remove_punc(cnpj):
    import re
    return re.sub(r'[\D]', '', cnpj)


def sequence(cnpj):
    cnpj1 = remove_punc(cnpj)
    sequencial = cnpj1[0] * len(cnpj1)
    if sequencial == cnpj1:
        return True
    else:
        return False
