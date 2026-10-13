"""Package komari-theme.json + dist/ into meridian.zip for upload."""
import os
import zipfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

with zipfile.ZipFile("meridian.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("komari-theme.json", "meridian/komari-theme.json")
    for base, _, files in os.walk("dist"):
        for name in sorted(files):
            p = os.path.join(base, name)
            zf.write(p, os.path.join("meridian", p))
print("wrote meridian.zip")
