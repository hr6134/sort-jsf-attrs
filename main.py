#!/usr/bin/env python
import re
import sys


attr_order = ('id', 
              'name',
              'alt',
              'value',
              'action', 
              'execute', 
              'style', 
              'styleClass', 
              'status', 
              'disable', 
              'rendered', 
              'render', 
              'limitRender',
              'onclick',
              'onchange',
              'oncomplete',
             )

tag_list = ('rich', 
            'h', 
            'a4j', 
            'f',
           )

# VALIDATORS
def validate(text):
    while True:
        attr_val = validate_attr_order(text)
        print attr_val
        if not attr_val:
            break
        replaced = replace(attr_val)
        print '-'*40
        print replaced
        print '*'*40
        text = text.replace(attr_val, replaced)
    return text

def validate_attr_order(text):
    '''
    validate attributes of tag until first error
    '''
    for i in take_tags(text):
        attrs = take_attr(i)
        n = 0
        for j in attrs:
            try:
                index = attr_order.index(j)
            except ValueError:
                continue
            if index < n:
                return i
            else:
                n = index

    return ''

# PARSERS
def take_attr(line):
    return re.findall(ur'(\w+)=(?:".*?"|\'.*?\')', line, re.S)

def take_tags(text):
    return re.findall('(^\s*<(?:' + '|'.join(tag_list) + '):\w+.*?>)', text, re.S | re.M)

# MODIFIERS
def replace(text):
    attrs = take_attr(text)
    sub_lists(attrs, attr_order)
    terminator = text.strip()[-2:]

    tag = re.findall(ur'\s*<\w+:\w+', text)[0]
    result = tag
    length = len(tag) + 1
    first = True
    if tag[0] == '\n':
        length -= 1

    for i in attr_order:
        try:
            current = re.findall(i + '=(?:".*?"|\'.*?\')', text, re.S)[0]
        except IndexError:
            continue
        if first:
            result += ' ' + current
            first = False
        else:
            result += '\n' + ' '*length + current

    for i in attrs:
        try:
            current = re.findall(i + '=(?:".*?"|\'.*?\')', text, re.S)[0]
        except IndexError:
            continue
        result += '\n' + ' '*length + current

    if terminator == '/>':
        return result + '/>'
    else:
        return result + '>'

# UTILS
def sub_lists(l1, l2):
    for i in l2:
        remove_all(l1, i)

def remove_all(l1, elem):
    while elem in l1:
        l1.remove(elem)


if __name__=="__main__":
    f = open(sys.argv[1])
    text = f.read()
    result = validate(text)
    f.close()

    f = open(sys.argv[1], 'w')
    f.write(result)
    f.close()
