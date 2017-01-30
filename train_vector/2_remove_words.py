# coding=utf-8
"""
删除非汉字字符
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
        # print type(line)
        ss = re.findall(ur'[\n\s\r\u4e00-\u9fa5]', line)
        # print line
        # print ss
        output.write("".join(ss))
