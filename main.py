import shutil, os
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), os.path.join(out, "entry.png"))
