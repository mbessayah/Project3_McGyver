# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Exploit & transform on list """


class Labymap:

    """ Transform and exploit txt files """

    @staticmethod
    def upload_file(req):
        """ Check files """
        lines = []
        # READ FILE LABYRINTH
        file = req
        try:
            with open(file, 'r') as f:
                for el_f in f.readlines():
                    lines.append(el_f.strip('\n'))
        except:
            print("No files founded")
        return lines

    def create_lab(self):
        """ make list """
        lab = []
        req = self.upload_file('views/labyrinth.txt')
        labyrinth_ch = []
        for el_lines in req:
            lab.append(el_lines)
        # LIST IN LIST
        for el_lab in lab:
            labyrinth_ch.append(list(el_lab))
        return labyrinth_ch

    def show_laby(self):
        labyrinth = self.create_lab()
        print(labyrinth)
