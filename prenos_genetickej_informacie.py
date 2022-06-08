gen_inf='TACCCGTAGAATCGTATCTGTACT'
nukletidy=[['UUU','UUC'],['UUA','UUG','CUU','CUC','CUA','CUG'],['AUU','AUC','AUA'],['AUG'],['GUU','GUC','GUA','GUG'],['UCU','UCC','UCA','UCG','AGU','AGC'],['CCU','CCC','CCA','CCG'],
           ['ACU','ACC','ACA','ACG'],['GCU','GCC','GCA','GCG'],['UAU','UAC'],['UAA','UAG','UGA'],['CAU','CAC'],['CAA','CAG'],['AAU','AAC'],['AAA','AAG'],['GAU','GAC'],['GAA','GAG'],
           ['UCU','UGC'],['UGG'],['CGU','CGC','CGA','CGG','AGA','AGG'],['GGU','GGC','GGA','GGG']]
kyseliny=['fenylalanín','leucín','isoleucín','začiatok','valín','serín','prolín','treonín','alanín','tyrozín','koniec','histidín','glutamín','asparagín','lyzín','kyselina asparágová',
          'kyselina glutamová', 'cysteín','tryptofán','arginín','glycín']
g_zoznam=[]
for i in range(0,int((len(gen_inf))/3)):
    g_zoznam.append(gen_inf[(i)*3:(i+1)*3])
print(f'Začiatok:     {gen_inf}')
g_format=''
for i in range(len(g_zoznam)):
    cast=g_zoznam[i]
    g_format+=cast
    g_format+=' '
print(f'Úprava:       {g_format}')

for i in range(len(g_zoznam)):
    for j in range(len(g_zoznam[i])):
        cast = g_zoznam[i][j]
        if cast == 'C':
            g_zoznam[i]= g_zoznam[i][:j]+'G'+g_zoznam[i][(j+1):]
        elif cast == 'G':
            g_zoznam[i]= g_zoznam[i][:j]+'C'+g_zoznam[i][(j+1):]
        elif cast == 'A':
            g_zoznam[i]= g_zoznam[i][:j]+'T'+g_zoznam[i][(j+1):]
        elif cast == 'T':
            g_zoznam[i]= g_zoznam[i][:j]+'A'+g_zoznam[i][(j+1):]

g_format=''
for i in range(len(g_zoznam)):
    cast=g_zoznam[i]
    g_format+=cast
    g_format+=' '
print(f'Replikácia:   {g_format}')

for i in range(len(g_zoznam)):
    for j in range(len(g_zoznam[i])):
        cast = g_zoznam[i][j]
        if cast == 'C':
            g_zoznam[i]= g_zoznam[i][:j]+'G'+g_zoznam[i][(j+1):]
        elif cast == 'G':
            g_zoznam[i]= g_zoznam[i][:j]+'C'+g_zoznam[i][(j+1):]
        elif cast == 'A':
            g_zoznam[i]= g_zoznam[i][:j]+'U'+g_zoznam[i][(j+1):]
        elif cast == 'T':
            g_zoznam[i]= g_zoznam[i][:j]+'A'+g_zoznam[i][(j+1):]

g_format=''
for i in range(len(g_zoznam)):
    cast=g_zoznam[i]
    g_format+=cast
    g_format+=' '
print(f'Transkripcia: {g_format}')

for i in range(len(g_zoznam)):
    for j in range(len(g_zoznam[i])):
        cast = g_zoznam[i][j]
        if cast == 'C':
            g_zoznam[i]= g_zoznam[i][:j]+'G'+g_zoznam[i][(j+1):]
        elif cast == 'G':
            g_zoznam[i]= g_zoznam[i][:j]+'C'+g_zoznam[i][(j+1):]
        elif cast == 'A':
            g_zoznam[i]= g_zoznam[i][:j]+'U'+g_zoznam[i][(j+1):]
        elif cast == 'U':
            g_zoznam[i]= g_zoznam[i][:j]+'A'+g_zoznam[i][(j+1):]

g_format=''
for i in range(len(g_zoznam)):
    cast=g_zoznam[i]
    g_format+=cast
    g_format+=' '
print(f'              {g_format}')

for i in range(len(g_zoznam)):
    cast = g_zoznam[i]
    for x in range(len(nukletidy)):
        for y in range(len(nukletidy[x])):
            if cast==nukletidy[x][y]:
                g_zoznam[i]=kyseliny[x]
            else:
                pass

g_format=''
for i in range(len(g_zoznam)):
    cast=g_zoznam[i]
    g_format+=cast
    g_format+=', '

print(f'Translácia:   {g_format[:-2]}')



