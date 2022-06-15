import re

ly_pattern = re.compile(r'\w+ly\b')    
sm_pattern = re.compile(r'\b(would|should|could)\b', flags=re.IGNORECASE)

patterns_list = [(ly_pattern, 'ly-pattern'), (sm_pattern, 'sm-pattern')]
