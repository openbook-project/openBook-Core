from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import subprocess

#compile
subprocess.call( ['python3', 'main.py', 'test_data/test5.book', 'test_out/'] )


opts = Options()
browser = Firefox(options=opts)
browser.get('file:///home/shail/openBook-Core/test_out/test5/test5.html')
