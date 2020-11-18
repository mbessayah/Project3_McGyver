# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Exploit list to find letter """

from views.labymap import Labymap

labyrinth = Labymap()


class Find:
    """ Exploit to find specific letter """

    @staticmethod
    def search(letter):
        """ Find positions to specific letter """
        l_search = []
        lab = labyrinth.create_lab()
        for chn in lab:
            position_y = lab.index(chn)
            for position_x, req in enumerate(chn):
                if req == letter:
                    l_search.append([position_x, position_y])
        return l_search
