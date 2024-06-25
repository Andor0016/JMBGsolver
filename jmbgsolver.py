def regionSearch(region):
    regions = {}
    return "test"

jmbg = input('Unesite JMBG: ')
if len(jmbg) != 13:
    print('JMBG mora imati 13 cifara')

dan = jmbg[0:2]
mesec = jmbg[2:4]
godina = jmbg[4:7]
region = jmbg[7:9]
pol = jmbg[9]
kontrolna_cifra = jmbg[12]

if(godina[0] == '0'):
    godina = '2' + godina
else:
    godina = '1' + godina

region = region_search(region)
print('Datum rodjenja: ' + dan + '.' + mesec + '.' + godina)

