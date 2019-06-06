"""these are the test string used, feel free to change tem """

text = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.'

text_2 = 'And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'



def line_formater(text, limit):
    formated_lines = []
    sentence = ''
    words = text.split()
    
    for word in words:
        if len(sentence + word + ' ') <= limit:
            sentence += word + ' '
            
        else:
            formated_lines.append(sentence)
            sentence = word + ' '
    simple_text_output = '\n'.join(formated_lines)
    print('simples ', limit,' character lines:\n\n', simple_text_output, '\n\n')

    return formated_lines, limit


def line_justified(formated_lines, limit):
    justified_sentence = []

    for line in formated_lines:
        space_counter = 0
        words = line.split(' ')
        while len(line) < limit:
            try: 
                words[space_counter] = words[space_counter] + ' '
                line = ' '.join(words)
                space_counter += 1 
            except:
                line = ' '.join(words)
                line = line.rstrip()
                space_counter = 0
                
        justified_sentence.append(line)   
    justified_text_output = '\n'.join(justified_sentence)      
    print('justified', limit,'char lines:\n\n', justified_text_output)


def main():
    lines, limit = line_formater(text_2, 20)
    line_justified(lines, limit)

#main()
