"""Update tensorflow version in docs. Run this from the repo-root."""
import argparse
import re

try:
  import pathlib2 as pathlib
except ImportError:
  import pathlib


EXTS = [".ipynb",".md",".yaml",".html"]
EXPAND_TABLES = [
    "site/en/install/source_windows.md",
    "site/en/install/source.md",]

class Version(object):
  def __init__(self, in_string):
    self.major, self.minor, self.patch = in_string.split(".")
    assert self.major.isdigit()
    assert self.minor.isdigit()
    assert self.patch.isdigit()

  def full(self):
    return ".".join([self.major, self.minor, self.patch])

  def short(self):
    return ".".join([self.major, self.minor])


parser = argparse.ArgumentParser()
parser.add_argument("--old_version", type=Version, required=True,
                    help="The old version to replace")
parser.add_argument("--new_version", type=Version, required=True,
                    help="The new version to replace it with")

if __name__=="__main__":
  args = parser.parse_args()

  for ext in EXTS:
    for file_path in pathlib.Path("site/en").glob(f"**/*{ext}"):
      content = file_path.read_text()
      if str(file_path) in EXPAND_TABLES:
        content = re.sub(
            f"(<tr>.*?){re.escape(args.old_version.short())}(.*?</tr>)",
            f"\g<1>{args.new_version.short()}\g<2>\n\g<0>",
            content,
        )
        file_path.write_text(content)
        continue

      content = file_path.read_text()

      content = content.replace(args.old_version.full(), args.new_version.full())
      content = content.replace(
          f"github.com/tensorflow/tensorflow/blob/r{args.old_version.short()}",
          f"github.com/tensorflow/tensorflow/blob/r{args.old_version.short()}",
      )
      file_path.write_text(content)
