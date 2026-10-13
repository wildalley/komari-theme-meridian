"""Package komari-theme.json + dist/ into nezha-live.zip for upload."""
import os
import zipfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

with zipfile.ZipFile("nezha-live.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("komari-theme.json", "nezha-live/komari-theme.json")
    for base, _, files in os.walk("dist"):
        for name in sorted(files):
            p = os.path.join(base, name)
            zf.write(p, os.path.join("nezha-live", p))
print("wrote nezha-live.zip")
