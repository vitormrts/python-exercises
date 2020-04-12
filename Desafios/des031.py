from math import ceil
import emoji
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n = ceil((n1+n2)/2)
print('Sua média foi {:.1f}!'.format(n))
if n == 6:
    print(emoji.emojize('Sua média foi razoável, mas você passou de ano :no_mouth:. ', use_aliases=True))
if n < 6:
    print(emoji.emojize('Sua média foi baixa. Portanto, infelizmente, você não passou de ano :cry:.', use_aliases=True))
if n > 6:
    print(emoji.emojize('Sua média foi boa, você passou de ano. PARABÉNS! :grin:', use_aliases=True))