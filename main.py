def main():
    book_path = "books/frankenstein.txt"
    full_text = open_book(book_path)
    print(full_text)
    number_of_words = word_count(full_text)
    print (number_of_words)

    letter_counter(full_text)

    

def open_book(bookpath_string):
    with open(bookpath_string) as f:
        return f.read()
    
def word_count(text):
    count = text.split()
    return len(count)

def letter_counter(book):
    letter_count_dictionary = {}
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    letter_list = alphabet.split(',')
    
    # filling out initial letter : count dictionary
    for letter in letter_list:
        letter_count_dictionary[letter] = book.lower().count(letter)

    print(letter_count_dictionary)

main()