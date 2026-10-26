import base64, hashlib, pathlib, lzma
p=pathlib.Path("shadow-assets.tar.xz")
bad=p.read_bytes()
encoded=base64.b64encode(bad).decode("ascii")
segment="OjBk3qTHHZ6yLV+t8kb7J6b1rb7VdCXi8LiADDn/p6h89gXiJfzdI1FCYjEPuF5XDnL2fy9uAQi20LXmecgLl0RHbUjnaJDYKwEUTqwNvGV6fykJFW+oSyxeXcvT/X9L0tI57zr2Q092EjjNG7wCcGJ/5dkbk4ejnB2ufp7yoQiyTNfX3P7dCBfCiqKTok0pM3KKYjK3+FM0C0wC6OLZBgOkou52neB4MIVC0Pn9w1ig0VXZ8a8H7FbAznDYnDKdOt8NOvMHRBh6pNpA1ldBqS/GvJ3vEkUHkBCIfhkCH5jvJHcsrtq+OOTCFuHWmcsRHAti6BtCjkj52ey+Dz1Aoh5ULv/eJ+VwYrBWuG38Z/tzuJZJXdEpkgyHWXCembXgf7FpLq3bNibGyiM8yFnKeuUC63I2DxnXoANq321QbkC0v6PINDzspB1V7yr50sf1MxtafZu51yAFNuFI7R65bDv4UF3+0mnrGUcMBmVMx5FfQuN5vVeFxinyNspmSjxbJK8MCLsVJltIBEavrSVBE/YLuTMlmkeYZjX3vJimqYWch4RupDymkufn5oaIQJ4iu/FoQQgvq2IkhSRjygucv3W1uJd9ukhTurdQxk3S2NazK6d+D1rAxYmYhqX7AZ5zgIKKOOBSgaVwnHlmH2YFVbrVf4p1VlLjYodFUVTXcBB/cZFrDVoL7qlV+zzJLCUkQWufhC5giAMPqdMLiOwwuya5Eqn26npbDoyAKQewXK+g/HeEewL7GHEKtvdO0orbxk4WPsdOpcWu1P/5H69JjT2n0VJne3SP"
# One base64 character was lost while transporting this XZ archive.
# The original 800-character span is preserved here verbatim.
good_b64=encoded[:3200]+segment+encoded[3999:6779]
fixed=base64.b64decode(good_b64,validate=True)
digest=hashlib.sha1(("blob %d\\0"%len(fixed)).encode()+fixed).hexdigest()
expected="25373735a51a4de4cc5261f16ecb1bc27c0562c2"
if digest!=expected:
    raise SystemExit(f"Texture archive checksum mismatch: {digest}; expected {expected}")
lzma.decompress(fixed)
p.write_bytes(fixed)
print(f"Verified {len(fixed)} bytes of Schatten-Arsenal texture assets.")
