"""Download Inter and Noto Sans (OFL) into assets/fonts.
This script avoids bundling font binaries directly in the template.
"""
import pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]  # project root
fonts_dir = ROOT / "src" / "app" / "assets" / "fonts"
fonts_dir.mkdir(parents=True, exist_ok=True)

# Minimal set (regular only to keep it light). Edit URLs as needed.
FONTS = {
    "Inter-Regular.ttf": "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bslnt,wdth,wght%5D.ttf",
    "NotoSans-Regular.ttf": "https://github.com/google/fonts/raw/main/ofl/notosans/NotoSans%5Bwdth,wght%5D.ttf",
}

def download(url: str, out: pathlib.Path):
    print(f"Downloading {url} -> {out}")
    urllib.request.urlretrieve(url, out)

def main():
    for name, url in FONTS.items():
        out = fonts_dir / name
        try:
            download(url, out)
        except Exception as e:
            print(f"Failed: {name} ({e})")
    print("Done. Update QSS if needed to point to local fonts.")

if __name__ == "__main__":
    main()
