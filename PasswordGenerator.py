import string
from random import *

characters = string.ascii_uppercase + string.ascii_lowercase + string.hexdigits
password = "".join(choice(characters) for x in range(randint(8, 16)))
print(password)

