import re
fin = open('data.csv', 'r', encoding='utf-8')
fout = open('dataout.csv', 'w', encoding='utf-8')
for line in fin:
    occurenceQuote = re.search('""', line)
    if occurenceQuote is not None:
        positionQuotes = occurenceQuote.span()[1]
        positionKomma = re.search(',', line[positionQuotes:]).span()[0]
        line = line[:positionQuotes + positionKomma] + line[positionQuotes +
                                                            positionKomma + 1:]

    fout.write(line)
fin.close()
fout.close()
