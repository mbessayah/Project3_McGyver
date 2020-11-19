# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" OBJ : Create a labyrinth game
    MacGyver must to leave the labyrinth with three objects

Attribute letters in labyrinth.txt file

D : Start position (Mac_Gyver)
S : End position (Guardian)
M : The wall
C : The way"""

from controllers import console

if __name__ == '__main__':
    console = console.Console()
    console.start_laby()
