__author__ = 'joe.hobot'
import gzip
matched_lines = []
file = raw_input('Imput Filepath: ')
with gzip.open( file, 'rb') as f:
    grep = raw_input('Enter Search: ')
    for line in f:
        if grep in line:
            matched_lines.append(line)

file_content = ''.join(matched_lines)

print(file_content)
