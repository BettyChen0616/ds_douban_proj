#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:00:01 2020

@author: chenjiayu

"""

import douban_scraper as ds
import pandas as pd
path = "/Users/chenjiayu/github/ds_douban_proj/chromedriver"

ds.login_douban(path)
df = ds.get_comments(27069428,25,path,1)


