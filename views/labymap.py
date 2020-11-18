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
            with open(file, 'r') as rec:
                for el_f in rec.readlines():
                    lines.append(el_f.strip('\n'))
        except NameError:
            print("No files founded")
        return lines

    def create_lab(self):
        """ make list """
        lab = []
        req = self.upload_file('macgyver_ressources/ressource/labyrinth.txt')
        labyrinth_ch = []
        for el_lines in req:
            lab.append(el_lines)
        for el_lab in lab:
            labyrinth_ch.append(list(el_lab))
        return labyrinth_ch

    def show_laby(self):
        """ show labyrinth """
        labyrinth = self.create_lab()
        print(labyrinth)
