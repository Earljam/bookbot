def main():
    book_path = "books/frankenstein.txt"
    full_text = open_book(book_path)
    print(f"--- Begin report of {book_path} ---")
    number_of_words = word_count(full_text)
    print(f"{number_of_words} words found in this document\n")

    letter_count = letter_counter(full_text)
    
    letter_count.sort(reverse=True, key=sort_aggregate)
    for i in letter_count:
        print(f"The '{i['letter']}' character was found {i['result']} times")
    

def open_book(bookpath_string):
    with open(bookpath_string) as f:
        return f.read()
    
def word_count(text):
    count = text.split()
    return len(count)

def letter_counter(book):
    
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    letter_list = alphabet.split(',')
    letter_count_list = []
    
    # filling out initial letter : count dictionary
    for letter in letter_list:
        letter_count_dictionary = {}
        letter_count_dictionary["letter"] = letter
        letter_count_dictionary["result"] = book.lower().count(letter)
        letter_count_list.append(letter_count_dictionary)

    return(letter_count_list)

    
def sort_aggregate(aggregate):
    return aggregate["result"]

main()