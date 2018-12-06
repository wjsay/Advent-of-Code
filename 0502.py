
import re

def work(line):
    regex = re.compile('(aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz)')
    length = len(line)
    while True:
        line = regex.sub('', line)
        new_length = len(line)
        if new_length == length:
            break
        length = new_length
    return len(line)

def main():
    fin = open('input.txt', 'rt')
    line = fin.readline().strip('\n')
    fin.close()
    minV = 50000
    for cc in ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz',]:
        new_line = re.sub('[' + cc + ']', '', line)
        minV = min(minV, work(new_line))
    print(minV)


if __name__ == '__main__':
    main()