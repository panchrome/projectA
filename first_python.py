import pandas as pd
import numpy as np
#%%
def do_welcome(name):
    return 'Hello,{}'.format(name)
#%%
for i in np.arange(1,10):
    print (i, do_welcome('Saum Pan'))