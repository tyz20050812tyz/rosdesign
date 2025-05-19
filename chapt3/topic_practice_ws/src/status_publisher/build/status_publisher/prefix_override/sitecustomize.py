import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tyzros/chapt3/topic_practice_ws/src/status_publisher/install/status_publisher'
