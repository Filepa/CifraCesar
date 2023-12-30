def deciframe(p:str, chave_k:int):
    import string
    alfabeto = string.ascii_lowercase
    chave = [num for num in str(chave_k)]
    palavra = [letra for letra in p]
    while len(chave) < len(palavra):
        chave.extend(chave)
    for i in range(len(palavra)):
        if palavra[i] == ' ':
            chave.insert(i, 0)
    chave = chave[:len(palavra)]
    for i in range(len(palavra)):
        if palavra[i] == ' ':
            continue
        else:
            indice = alfabeto.index(palavra[i])-int(chave[i])
            if indice >= len(alfabeto):
                indice -= len(alfabeto)
            palavra[i] = alfabeto[indice]
    texto = ''
    for j in range(len(palavra)):
        texto += palavra[j]
    return texto