# from plot_for_weather import plot_tem
# import plot_for_weather
# import plot_for_time
from glob import glob
from keyword import iskeyword
from os.path import dirname, join, split, splitext

basedir = dirname(__file__)

for name in glob(join(basedir, '*.py')):
    module = splitext(split(name)[-1])[0]
    if not module.startswith('_') and \
       module.isidentifier() and \
       not iskeyword(module):

       m = __import__(__name__+'.'+module)
       try:
           attrlist = m.__all__
       except AttributeError:
           attrlist = dir(m)
       for attr in attrlist:
           globals()[attr] = getattr(m, attr)

