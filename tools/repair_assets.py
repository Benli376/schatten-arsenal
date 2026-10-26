import base64, hashlib, pathlib, lzma
p=pathlib.Path("shadow-assets.tar.xz")
bad=p.read_bytes()
encoded=base64.b64encode(bad).decode("ascii")
# Repair one lost base64 character at offset 3500 and restore final padding.
good_b64=encoded[:3500]+"J"+encoded[3500:6777]+"o="
fixed=base64.b64decode(good_b64,validate=True)
digest=hashlib.sha1(b'blob '+str(len(fixed)).encode()+bytes([0])+fixed).hexdigest()
expected="25373735a51a4de4cc5261f16ecb1bc27c0562c2"
if digest!=expected:
    raise SystemExit(f"Texture archive checksum mismatch: {digest}; expected {expected}")
lzma.decompress(fixed)
p.write_bytes(fixed)
print(f"Verified {len(fixed)} bytes of Schatten-Arsenal texture assets.")
