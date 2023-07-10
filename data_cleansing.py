import re
import pandas as pd

abusive = pd.read_csv('data/abusive.csv', encoding='utf-8')
new_kamusalay = pd.read_csv('data/new_kamusalay.csv', encoding='latin1')
new_kamus_alay = {}
for k,v in new_kamusalay.values:
    new_kamus_alay[k] = v


def processing_word(input_text):
    new_text = [] # set up new list
    new_new_text = [] # set up new new list
    text = input_text.split(" ") # split input_text menjadi list of words
    for word in text: # untuk setiap word in 'text'
        if word in abusive['ABUSIVE'].tolist(): # check word di dalam list_of_abusive_words
            continue # jika ada, skip
        else:
            new_text.append(word) # jika tidak ada, masukkan ke dalam list new_text
   
    for word in new_text:
        new_word = new_kamus_alay.get(word, word) # check ke new_kamus_alay, apakah word ada di dictionarynya. kalau ga ada, return word yang sama. kalau ada, kembalikan value barunya (value yang ada di dict)
        new_new_text.append(new_word)
    
    text = " ".join(new_new_text)
    return text

def processing_text(input_text):
    
    if input_text is not None:
        text = input_text.lower()  # Mengubah teks menjadi huruf kecil

        pattern_1 = r'(user|retweet|\\t|\\r|ur1|xd|orang|kalo)'
        text = re.sub(pattern_1, '', text)  # Menghapus kata-kata yang ada dalam pattern_1

        pattern_2 = r'@[^\s]+'
        text = re.sub(pattern_2, '', text)  # Menghapus mention (@) dalam teks

        pattern_3 = r'#([^\s]+)'
        text = re.sub(pattern_3, '', text)  # Menghapus hashtag (#) dalam teks

        pattern_4 = r'[\,\@\_\-\!\:\;\?\'\.\")\(\{\}\<\>\+\%\$\^\#\/\`\~|\&\|)]'
        text = re.sub(pattern_4, '', text)  # Menghapus karakter khusus dalam teks

        pattern_5 = r'\b\w{1,3}\b'
        text = re.sub(pattern_5, '', text)  # Menghapus kata dengan panjang 1-3 karakter

        pattern_6 = r'\\[a-z0-9]{1,5}'
        text = re.sub(pattern_6, '', text)  # Menghapus karakter escape (\) diikuti oleh huruf dan angka

        pattern_7 = r'\d+'
        text = re.sub(pattern_7, '', text)  # Menghapus angka dalam teks

        pattern_8 = r'(https|https:)'
        text = re.sub(pattern_8, '', text)  # Menghapus URL (https atau http) dalam teks

        pattern_9 = r'[\\\]\[]'
        text = re.sub(pattern_9, '', text)  # Menghapus karakter \, [ dan ] dalam teks

        pattern_10 = r'[^\x00-\x7f]'
        text = re.sub(pattern_10, '', text)  # Menghapus karakter non-ASCII dalam teks

        pattern_11 = r'(\\u[0-9A-Fa-f]+)'
        text = re.sub(pattern_11, '', text)  # Menghapus karakter unicode escape (\uXXXX) dalam teks

        pattern_12 = r'(\s+|\\n)'
        text = re.sub(pattern_12, '', text)  # Menghapus spasi dan karakter newline (\n) dalam teks

        pattern_13 = r'\bwk\w+'
        text = re.sub(pattern_13, '', text)  # Menghapus kata yang dimulai dengan "wk" dalam teks
        text = text.strip()

    return text