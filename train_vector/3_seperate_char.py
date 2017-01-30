# coding=utf-8
"""
把每个汉字字符分开
"""
import os
import logging
import sys
import re
import codecs

if __name__=='__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)

    inp, outp = sys.argv[1:3]

    output = codecs.open(outp, 'w', encoding="utf-8")
    in_put = codecs.open(inp, 'r', encoding="utf-8")

    for line in in_put:
        list_l = list(line)
        for i, ch in enumerate(list_l):
            if ch != u" ":
                list_l[i] = ch + u" "
        output.write("".join(list_l))
