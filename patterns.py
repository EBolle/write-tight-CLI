import re

ly_pattern = re.compile(r'\w+ly\b')    


patterns_list = [(ly_pattern, 'ly-pattern'), ]