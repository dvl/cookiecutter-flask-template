import decouple as d

DEBUG = d.config('DEBUG', cast=bool, default=False)
