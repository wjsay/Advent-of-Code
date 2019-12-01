
import re, string

def main():
    fin = open('input.txt', 'rt')
    line = fin.readline().strip('\n')
    fin.close()
    regex = re.compile('(aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz)')
    length = len(line)
    while True:
        line = regex.sub('', line)
        new_length = len(line)
        if new_length == length:
            break
        length = new_length
    print(len(line))
# dabAaCBAcaDA


if __name__ == '__main__':
    main()