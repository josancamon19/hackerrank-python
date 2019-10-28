import re

# Just copy and paste -> I do not think regex really matters
regex_pattern = r"[,.]"
print("\n".join(re.split(regex_pattern, input())))
