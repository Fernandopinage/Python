def media(*num,situacao = False):
    
    r = dict()
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)

    if situacao:
        if r['media'] >= 8:
                r['situacao'] = 'boa'
        elif r['media'] <= 7 and r['media'] >= 6:
                 r['situacao'] = 'recuperação'
        elif r['media'] <= 5:
                 r['situacao'] = 'reprovado'  
            
    return r



r = media(3,5,9.5, situacao=True)
print(r)