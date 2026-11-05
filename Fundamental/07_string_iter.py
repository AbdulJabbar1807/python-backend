def reverse_words(strings):
    cln_str = strings.split()
    sort_cln_str = cln_str[::-1]
    return sort_cln_str

def main():
    strings = "   the   sky is  blue  "
    print(reverse_words(strings))
    
if __name__ == "__main__":
    main()