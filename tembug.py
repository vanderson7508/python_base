"""
def repete_vogal(word):
    #Retorna a palavra com as vogais repetidas.
    final_word = ""
    for index, letter in enumerate(word):
        print(f"index={index} {letter=}")
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
        print(f"{final_word}")
    return final_word
    
print(repete_vogal("banana"))

"""
def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâôêéáíó":
            breakpoint()
            final_word = letter * 2
        else:
            final_word = letter
    return final_word
print(repete_vogal("banana"))
