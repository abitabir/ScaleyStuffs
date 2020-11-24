##Exercise 5: Cryptography, Caesar Cipher
##In cryptography, a Caesar cipher, also known as the shift cipher, is one of the simplest and
##most widely known encryption techniques. It is a type of substitution cipher in which each
##letter in the plain text is replaced by a letter some fixed number of positions down the alphabet.
##For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The
##method is named after Julius Caesar, who used it to communicate with his generals.
##Mathematically, a Caesar cipher can be expressed by
##the following equation:
##c = (p + a) mod 26
##Here, ‘mod 26’ means that you use clock arithmetic for
##values greater than 26, i.e., 0=26 mod 26, 1=27 mod
##26, 2=28 mod 26, …, 0=52 mod 26, 1=53 mod 26, …,
##10=62 mod 26, and so on.
##1. Write a function caesar_encrypt that encrypts a plain text into a cypher text using
##the Caesar Cipher algorithm. What parameters are needed? Should the function return
##something? For simplicity, assume that only alphabet letters are encrypted, other
##symbols remain the same.
##2. Write a function caesar_decrypt that decrypts a cipher text into a plain text using
##the Caesar Cipher algorithm. What parameters are needed?
##3. Given the cipher text below, and knowing it has been encrypted using a Caesar Cipher
##algorithm, could you decrypt it?
##"bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
##bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
##bmtt bpmu bw lw.”

#1.
plain_text = str(input("Enter plain text to convert it into caesar cipher."))
alphabet = "abcdefghijklmnopqrstuvwxyz"
import random
shift = random.randint(1, 25)
#c = (p + a) mod 26

def plain_text_to_caesar_cipher(plain_text):
    caesar_cipher = ""
    for character in plain_text:
            if character in alphabet:
                for i in range(len(alphabet)):
                    if alphabet[i] == character:
                        caesar_cipher += alphabet[i + shift]
            else:
                caesar_cipher += character
    return(caesar_cipher)

print("Your plain text converted into caesar cipher with shift", shift, "is:")
print(plain_text_to_caesar_cipher(plain_text))

#2.
cipher_text = str(input("Enter caesar cipher to convert it into plain text."))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decrypt(cipher_text):
    plain_text_variation = ""
    for character in cipher_text:
            if character in alphabet:
                for j in range(len(alphabet)):
                    if alphabet[j] == character:
                        plain_text_variation += alphabet[(j + i) % 26]
            else:
                plain_text_variation += character
    return(plain_text_variation)



print("All the possible variations of the original plain text from this Caesar cipher are as follows:")

for i in range(1, 25):
    print(caesar_decrypt(cipher_text))

print("And there you go! Now it is up to you to use your human mind to see which of these decryptions is the coherent one for human minds and language.")

#3.

#the decryption of "bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw." is "the good news about computers is that they do what you tell them to do. the bad news is that they do what you tell them to do"
