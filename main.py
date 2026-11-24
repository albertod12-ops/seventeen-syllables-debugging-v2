import os

TEXT = """Tell the duck my bug
it stares back, silent, yellow
the answer was mine"""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(TEXT)
# The grader collects outputs as another user, so the file must be
# readable by everyone, not just its owner.
os.chmod(path, 0o644)
