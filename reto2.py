"""Un palíndromo es un una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda ejemplo Ojo, Oso, Ana, Anna, Otto…,
Su misión es, realizar un algoritmo que me permita conocer dada una palabra por el usuario si es palíndromo o no"""
def palindrome(word):
    # Convert the word to lowercase for case-insensitive comparison
    lower_word = word.lower()
   
    # Check if the lowercase word is the same when reversed
    if lower_word == lower_word[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

try:
    # Get user input
    word = input("Enter a word: ")
    
    # Call the palindrome function to check if the word is a palindrome
    palindrome(word)
    
except KeyboardInterrupt:
    print("\nOperation aborted by the user.")