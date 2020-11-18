# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Define position of guardian """

from controllers.find import Find
from views.screen import Screen

# Game's Class


class Guardian:
    """ Define position of guard """

    check_gard = Find()
    for GUARD in check_gard.search('S'):
        GUARD[0] = (GUARD[0] * Screen.scall_screen[0])
        GUARD[1] = (GUARD[1] * Screen.scall_screen[1])
