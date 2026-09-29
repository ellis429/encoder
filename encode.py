import base64, hashlib, sys

src = sys.argv[1]                 # 例如 app.AppImage
PART = 90_000_000                 # 每份約 90MB,低於 GitHub 的 100MiB 限制
WRAP = 100                        # 每行 100 字元,避免單行過長

data = open(src, "rb").read()
open("app.sha256", "w").write(f"{hashlib.sha256(data).hexdigest()}  {src}\n")

enc = base64.b85encode(data).decode("ascii")
text = "\n".join(enc[i:i+WRAP] for i in range(0, len(enc), WRAP)) + "\n"

n = 0
for i in range(0, len(text), PART):
    with open(f"part_{n:03d}.txt", "w") as f:
        f.write(text[i:i+PART])
    n += 1
print(f"完成:{n} 份")