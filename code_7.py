# 引数・戻り値なし
def print_banana():
    print('banana')
    
print_banana()    


# 引数あり・戻り値なし
def print_text(text):
    print(text)
    
print_text('orange')


# 引数・戻り値あり
def question_text(text):
    text_q = text + '?'
    return text_q

result_text = question_text('apple')
print(result_text)


# 複数の引数・戻り値あり
def question_exclamation_text(text1, text2):
    return_text1 = text1 + '?'
    return_text2 = text2 + '!'
    return return_text1, return_text2

r1, r2 = question_exclamation_text('pinapple', 'banana')
print(r1)
print(r2)