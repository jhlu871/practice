# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 08:08:31 2016

@author: Jason
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv('aapl.csv',index_col=0).iloc[::-1]
txt = '''
    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.'''

fig = plt.figure()
ax1 = fig.add_axes((.1,.5,.8,.5))
with PdfPages('test.pdf') as pdf:
    fig = plt.figure()
    ax1 = fig.add_axes((.1,.5,.8,.4))
    df.plot(y='Adj Close',ax=ax1)
    fig.text(.1,.1,txt)
    pdf.savefig()
    plt.close()

    fig = plt.figure()
    ax1 = fig.add_axes((.1,.1,.8,.8))
    df.plot(y='Open',ax=ax1)
    pdf.savefig()
    plt.close()