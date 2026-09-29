import base64, glob, hashlib

print("解碼中...")
parts = sorted(glob.glob("part_*.txt"))
enc = "".join(open(p).read() for p in parts).replace("\n", "")
data = base64.b85decode(enc)
open("app.AppImage", "wb").write(data)

expected = open("app.sha256").read().split()[0]
print("OK" if hashlib.sha256(data).hexdigest() == expected else "雜湊不符!")