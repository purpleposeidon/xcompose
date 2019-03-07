#!/usr/bin/python3
# coding: utf8

import sys, unicodedata

specials = {
    '%' : 'percent',
    '-' : 'minus',
    '_' : 'underscore',
    '>' : 'greater',
    '<' : 'less',
    ',' : 'comma',
    '.' : 'period',
    '$' : 'dollar',
    '!' : 'exclam',
    '?' : 'question',
    '+' : 'plus',
    '/' : 'slash',
    '#' : 'numbersign',
    '@' : 'at',
    '|' : 'bar',
    '`' : 'grave',
    '~' : 'asciitilde',
    '^' : 'asciicircum',
    '&': 'ampersand',
    '(' : 'parenleft',
    ')' : 'parenright',
    '[' : 'bracketleft',
    ']' : 'bracketright',
    '{' : 'braceleft',
    '}' : 'braceright',
    "'" : 'apostrophe',
    '"' : 'quotedbl',
    '\\': 'backslash',
    ':' : 'colon',
    ';' : 'semicolon',
    '=' : 'equal',
    ' ' : 'space',
    '*' : 'asterisk',
    '♫' : 'Multi_key',
    '\t': 'tab',
}

for l in sys.stdin.readlines():
    l = l.strip('\n')
    if not l or l.startswith("#"):
        print(l)
        continue
    becomes = l[-1]
    l = l[:-1]
    sys.stdout.write("<Multi_key>")
    for c in l:
        sys.stdout.write(' <'+specials.get(c, c)+'>')
    n = hex(ord(becomes))[2:].upper()
    name = unicodedata.name(becomes)
    sys.stdout.write(' : "{}" U{} # {}\n'.format(becomes, n, name))
