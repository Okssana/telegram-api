import pandas as pd 
import ssl

### NLTK libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# https://www.youtube.com/watch?v=IBmZAYR0pns

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('all')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

### Source-1 ###
url = 'https://raw.githubusercontent.com/stopwords-iso/stopwords-ru/master/stopwords-ru.txt'

stopwords1 = pd.read_csv(url, header=None)
stopwords1 = stopwords1[0].tolist()

### Source-2 ###
stopwords2_file = 'stop_words_russian.txt'
# Read file stopwords2
with open(stopwords2_file, 'r') as file:
    stopwords2 = file.read()

stopwords2 = stopwords2.split('\n')

### Source-3 ###

stopwords3 = stopwords.words('russian')
print(type(stopwords1), type(stopwords2), type(stopwords3))

### Source-4 ###
# Manually gathered 

stopwords4 = [ 'г.', '«', '6', '»', '(', ')',  '2', ',', ':', '1', 
 ';', '№', 'твк', '4', '5', '7', '8', '9', '10', '31', '34',  '22.00',
 '24.00.',  '.',  '00',   '130', '000', '000,00',  '.',   'п.4',  '*',
  'о.м','д','☐','дд/мм/гггг', 'м.',
 'п', '1.',  '2.',  '+',  '3.',  '5.',   '+',  '7.',  '8.',   '9.',  '_',  '10.',   '12.',  '13.',  '14.',  '15.',  '16.', '17.', 
 '#',  '/',  '•',  '{', '}', 
 '11',  'п', 'ст', '57', '<', '|', '>', 'п',   'br',  'nan',  '@',   'mail.ru', '``', '\\xa0', "''", 
 '1618033989', 'message', '!', "'", '?', 'de', 'дата', '&', 'уважением', 'please', 'mailto', 'тема', 
 'сообщение', 'legalintel.ru', 
 'копия',  'написал', '[', ']',  '’', 'исходное', 'привет', 'приветствую'
]


### Source-5: English stopwords
stopwords5 = stopwords.words('english')

### Souece-6: Manually gathered

stopwords6 = ['привет', 'отправлено', 'sent', 'le', 'e-mail','email', 'u', 'information', '=', 
              'from', 'for', 'to', 'cc', 'bcc', 'subject', 'date', 're', 'fw', 'fwd', 'dear', 'regards', 'regard', 'best', 
              'best regards', 'subject', 'тема', 'la', 'добрый', 'отправлено', 'android', 'fw', 'forwarded', 'samsung', 
              'смартфона', 'galaxy', 'account', 'http', 'https', 'www',
              'ipad', 'iphone', 'ipod', 'touch', 'apple', 'mail', 'mail.ru', 'yandex', 'yandex.ru', 'gmail', 'gmail.com',
              'yahoo', 'yahoo.com', 'outlook', 'outlook.com', 'aol', 'aol.com', 'hotmail', 'hotmail.com', 'live', 'live.com',
              'comcast', 'comcast.net', 'verizon', 'verizon.net', 'cox', 'cox.net', 'att', 'att.net', 'sbcglobal', 'sbcglobal.net',
              'me', 'me.com', 'icloud', 'icloud.com', 'mac', 'mac.com', 'gmx', 'gmx.com', 'gmial', 'gmial.com', 'inbox', 'inbox.com',
              'mail', 'mail.com', 'inbox', 'inbox.com', 'protonmail', 'protonmail.com', 'zoho', 'zoho.com', 'yandex', 'yandex.com',
              'yandex', 'yandex.ru', 'rambler', 'rambler.ru', 'rambler', 'rambler.com', 'rambler', 'rambler.net', 'rambler', 'rambler.ua',
              '+03:00', 'us', '–', '-', 
              '\\', '0', 'gt', 'lt', 'pm', 'gmt+04:00', 'gmt+03:00', 'gmt+02:00', 'gmt+01:00', 'gmt+00:00', 'gmt-01:00', 'gmt-02:00', 'gmt-03:00',
              'gmt-04:00', 'gmt-05:00', 'gmt-06:00', 'gmt-07:00', 'gmt-08:00', 'gmt-09:00', 'gmt-10:00', 'gmt-11:00', 'gmt-12:00', 'gmt+05:00',
              'gmt+06:00', 'gmt+07:00', 'gmt+08:00', 'gmt+09:00', 'gmt+10:00', 'gmt+11:00', 'gmt+12:00', 'gmt+13:00', 'gmt+14:00', 'gmt-13:00',
              'gmt-14:00', 'gmt-15:00', 'gmt-16:00', 'gmt-17:00', 'gmt-18:00', 'gmt-19:00', 'gmt-20:00', 'gmt-21:00', 'gmt-22:00', 'gmt-23:00',
              'gmt-24:00', 'href=',   'received', 'also', '\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0\\xa0',
              '-original', 'mymail',
              'либо', 'е', 'e', 'и/или', 'или', 'и', 'and/or', 'тел', 'gmt+3',
              'явно', 'may', 'tel', 'would', 'could', 'should', 'can', 'will', 'may', 'might', 'must', 'need', 'ought', 'shall', 'should',
              'et', 'sa', 'пожалуйста', 'любые', 'какого', 'какое', 'какие', 'каким', 'какими', 'каких', 'какую', 'какая', 'какой', 'какие',
              'любой', 'à'

              ]

### Source-7: English stopwords
# stopwords7 = stopwords.words('french')

# ### Source-8: Italian stopwords
# stopwords8 = stopwords.words('italian')

# ### Source-9: More Russian stopwords
stopwords9 = ['привет', 'отправлено', 'sent', 'le', 'e-mail','email', 'u', '=',
              '...', '—', '—', '%', 'd0', 'd1', '3']

# Merge stopwords1, stopwords2, stopwords3
stopwords_merged = stopwords1+stopwords2+stopwords3+stopwords4+stopwords5+stopwords6+stopwords9