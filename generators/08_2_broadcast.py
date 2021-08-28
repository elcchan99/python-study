from libs import select
from libs.apachelog import apache_log
from libs.broadcast import broadcast, Consumer
from libs.linesdir import lines_from_dir


c1 = Consumer(name="Ada")
c2 = Consumer(name="Bob")
c3 = Consumer(name="Cat")

lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
logs = select.first(logs, 3)
hosts = (r["host"] for r in logs)

broadcast(hosts, [c1, c2, c3])
