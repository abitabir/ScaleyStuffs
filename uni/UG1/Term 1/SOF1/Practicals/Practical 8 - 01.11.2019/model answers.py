
#1.
def basket_price(basket, stock, prices):
    total = 0
    for item in basket:
        if (item not in prices 
            or item not in stock 
            or stock[item] < basket[item]):
            return -1
        else:
            total += basket[item] * prices[item]
    
    return total

def checkout(basket, stock, prices):
    total = basket_price(basket, stock,prices)
    if total < 0:
        return -1
    else:
        for item in basket:
            stock[item] -= basket[item]

        return total

def add_stock(items, stock):
    for item in items:
        quatity = stock.setdefault(item, 0)
        stock[item] += items[item]    
       
def price_increase(increase, prices):
    for  item in prices:
        prices[item] *= 1 + increase

    return prices

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 40,
    "apple": 20,
    "orange": 15,
    "pear": 30
}

basket_1 = {
    "banana": 4,
    "pear": 3
}

basket_2 = {
    "apple": 1,
    "pear": 3
}

print(basket_price(basket_1, stock, prices))
print(basket_price(basket_2, stock, prices))
print(checkout(basket_1, stock, prices))
print(stock)
print(checkout(basket_2, stock, prices))
print(stock)
add_stock({'apple':5, 'kiwi':10, 'banana':10}, stock)
print(stock)
print(price_increase(0.2, prices))
print(prices)





#2.
import operator

def _get_char_digit(letter, keypad):
    for digit, chars in keypad.items():
        if letter.lower() in chars:
            return digit

def _get_word_digits(word, keypad):
    digits = ''
    for letter in word:
        digits += _get_char_digit(letter, keypad)

    return digits

def _update_frequency(lst_words, word):
    updated = False
    for index in range(len(lst_words)):
        if lst_words[index][0] == word:
            lst_words[index][1] += 1
            updated = True

    if not updated: # means the word is not in the list
        lst_words.append([word,1])


        
def extract_textonyms(vocabulary, keypad):
    # The data structure used is a dictionary, where the keys are the digits
    # pattern, for example '4663'. The values are lists of string, containing
    # the words associated to that pattern. for example ['home', 'good'].
    # user_dict -> {'4663':[['home',5],['good',10],['hood',1]], '2':[['a',9]],
    #               ...}
    user_dict = {}
    for word in vocabulary:
        digits = _get_word_digits(word, keypad)
        lst_words = user_dict.setdefault(digits,[])
        _update_frequency(lst_words, word)
 
    return user_dict

def add_words(text, user_dict, keypad):
    for word in text:
        digits = _get_word_digits(word, keypad)
        lst_words = user_dict.setdefault(digits,[])
        _update_frequency(lst_words, word)
 
    return user_dict
        
            
def get_words(digits, user_dict):
    if digits in user_dict.keys():
        words = user_dict[digits]
        words.sort(key = operator.itemgetter(1), reverse=True)
        output=[]
        for pair in words:
            output.append(pair[0])

        return output
    else:
        return []


# extract from  "Twenty thoushand leagues under the sea" by Jules Verne.

vocabulary = ['the', 'year', 'was', 'signalised', 'by', 'a', 'remarkable',
              'incident', 'a', 'mysterious', 'and', 'puzzling', 'phenomenon',
              'which', 'doubtless', 'no', 'one', 'has', 'yet', 'forgotten',
              'Not', 'to', 'mention', 'rumours', 'which', 'agitated', 'the',
              'maritime', 'population', 'and', 'excited', 'the', 'public',
              'mind', 'even', 'in', 'the', 'interior', 'of', 'continents',
              'seafaring', 'men', 'were', 'particularly', 'excited',
              'Merchants', 'common', 'sailors', 'captains', 'of', 'vessels',
              'skippers', 'both', 'of', 'Europe', 'and', 'America', 'naval',
              'officers', 'of', 'all', 'countries', 'and', 'the',
              'Governments', 'of', 'several', 'States', 'on', 'the', 'two',
              'continents', 'were', 'deeply', 'interested', 'in', 'the',
              'matter', 'For', 'some', 'time', 'past', 'vessels', 'had',
              'been', 'met', 'by', 'an', 'enormous', 'thing', 'a', 'long',
              'object', 'spindle', 'shaped', 'occasionally', 'phosphorescent',
              'and', 'infinitely', 'larger', 'and', 'more', 'rapid', 'in',
              'its', 'movements', 'than', 'a', 'whale']

t9_keypad = {'2':['a','b','c'], '3':['d','e','f'],
             '4':['g','h','i'], '5':['j','k','l'],
             '6':['m','n','o'], '7':['p','q','r','s'],
             '8':['t','u','v'], '9':['w','x','y','z']}

user_voc = extract_textonyms(vocabulary,t9_keypad)
print(add_words(['home', 'good', 'hood', 'hood', 'hood', 'hood', 'good','good', 'home', 'a', 'a', 'a'],
                user_voc, 
                t9_keypad))
print(get_words('4663', user_voc))
                