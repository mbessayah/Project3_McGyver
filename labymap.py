# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Labymap:
    """ Transform and exploit txt files """

    def upload_file(self, req):
        """ Check files """
        lines = []
        # READ FILE LABYRINTH
        FILE = req
        try:
            with open(FILE, 'r') as f:
                for el_f in f.readlines():
                    lines.append(el_f.strip('\n'))
        except:
            print("No files founded")
        return lines

    def create_lab(self):
        """ make list """
        lab = []
        req = self.upload_file('labyrinth.txt')
        LABYRINTH = []
        for el_lines in req:
            lab.append(el_lines)
        # LIST IN LIST
        for el_lab in lab:
            LABYRINTH.append(list(el_lab))
        return LABYRINTH

    def show_laby(self):
        labyrinth = self.create_lab()
        print(labyrinth)
