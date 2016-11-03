#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class PikoTaro:

    def uh(self, objects):
        assert len(objects) == 2
        stack = []
        for i, o in enumerate(objects[::-1]):
            if type(o) == list:
                stack += o[::-1] if i == 0 else o
            elif type(o) == str and '-' in o:
                o = o.split('-')
                stack += o[::-1] if i == 0 else o
            else:
                stack.append(o)
        print('Uh!')
        return '-'.join(stack)


def ppap(iteration):
    pikotaro = PikoTaro()
    ap = pikotaro.uh([s.split()[-1] for s in ("I have a Pen", "I have a Apple")])
    print(ap)
    pp = pikotaro.uh([s.split()[-1] for s in ("I have a Pen", "I have Pineapple")])
    print(pp)
    ppap = pikotaro.uh((ap, pp))
    print(ppap)

    if iteration > 0:
        print('***')

        for i in range(iteration):
            ppap = pikotaro.uh((ppap, ppap))
            print(ppap)


if __name__ == "__main__":
    ppap(iteration=(int(sys.argv[1]) if len(sys.argv) > 1 else 5))
