#!/usr/bin/env python3

import random
import string

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

print(''.join(random.choice(chars) for i in range(random.randint(8,12))))
