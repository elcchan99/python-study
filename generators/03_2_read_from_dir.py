from libs import select
from libs.linesdir import lines_from_dir


lines = lines_from_dir(r"access_log_*.log", "www")
for line in select.first(lines, 10):
    print(line, end="")
