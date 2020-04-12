from time import sleep
import datetime
import emoji
print('\033[1;31m='*20, 'CONTAGEM REGRESSIVA', '='*20)
for c in range (10, -1, -1):
    sleep(1)
    print('\033[1;34m', c)
print(emoji.emojize('\033[1mFELIZ {} :boom: :boom: :boom:  !!!'.format(datetime.datetime.today().year+1), use_aliases=True))
