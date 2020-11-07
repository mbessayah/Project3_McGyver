# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from find import Find


check_way = Find()


class SpawnItems:

    spawn_items = check_way.search('C')

    for aleatory in range(1):
        Check_Items = (random.sample(spawn_items, 3))

    needle = [Check_Items[0][0] * 43, Check_Items[0][1] * 43]
    plastic_tube = [Check_Items[1][0] * 43, Check_Items[1][1] * 43]
    ether = [Check_Items[2][0] * 43, Check_Items[2][1] * 43]


