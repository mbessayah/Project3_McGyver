# !/usr/bin/env python
# -*- coding: utf-8 -*-


from labymap import Labymap

labyrinth = Labymap()


class Find:
    """ Exploit to find specific letter """

    def search(self, letter):
        l_search = []
        lab = labyrinth.create_lab()
        for chn in lab:
            y = lab.index(chn)
            for x, req in enumerate(chn):
                if req == letter:
                    l_search.append([x, y])
        return l_search
