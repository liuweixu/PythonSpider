from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://cgartt.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://cgartt.com/'))
