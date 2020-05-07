# Selenium-WebDriver
This is the sample code for the selenium webdriver

You have to first check whether your computer has selenium and webdriver
if yes:
    then move further code.
else:
    Install selenium and webdriver

To check in your computer
-Open terminal and type following command
$pip list

if Not then install the following command
$pip install selenium
$pip install webdriver_manager

-Use with Chrome:

from webdriver_manager.chrome import ChromeDriverManager
webdriver.Chrome(ChromeDriverManager().install())

-Use with FireFox:

from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

-Use with IE

from webdriver_manager.microsoft import IEDriverManager
driver = webdriver.Ie(IEDriverManager().install())

-Use with Opera

from webdriver_manager.opera import OperaDriverManager
driver = webdriver.Opera(executable_path=OperaDriverManager().install()

-Use with Edge

from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
