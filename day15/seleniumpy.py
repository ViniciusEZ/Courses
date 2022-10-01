from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeAuto:
    def __init__(self):
        self.root_folder = Path(__file__).parent.parent
        self.chrome_driver_path = self.root_folder / 'day15' / 'chromedriver'

    def make_chrome_browser(self, *options):
        self.chrome_options = webdriver.ChromeOptions()
        if options is not None:
            for option in options:
                self.chrome_options.add_argument(option)

        self.chrome_service = Service(executable_path=self.chrome_driver_path,)
        self.browser = webdriver.Chrome(
            service=self.chrome_service,
            options=self.chrome_options
        )
        return self.browser

    def access_site(self, url):
        self.browser.get(url)

    def leave(self):
        self.browser.quit()

    def click_login(self):
        try:
            btn_sign_in = self.browser.find_element(By.LINK_TEXT, 'Login')
            btn_sign_in.click()
        except Exception as e:
            print(f'Error in Login: {e}')

    def write_credentials(self):
        try:
            email_cre = self.browser.find_element(By.NAME, 'email')
            password_cre = self.browser.find_element(By.NAME, 'password')
            email_cre.send_keys('ez998@outlook.com')
            password_cre.send_keys('998688124CFAL')
            self.browser.find_element(By.CSS_SELECTOR, 'button.marginBottom8-emkd0_').click()
        except Exception as e:
            print(f'Error in write your credentials: {e}')

    def click_user(self):
        try:
            finder = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div.container-1eFtFS > div > div > div.sidebar-1tnWFu > nav > div.scroller-WSmht3.thin-31rlnD.scrollerBase-_bVAAt.fade-1R6FHN > ul > li:nth-child(19) > div')))
            finder.click()
        except Exception as e:
            print(e)

    def write_message(self):
        try:
            writer_msg = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div.container-1eFtFS > div > div > div.chat-2ZfjoI > div.content-1jQy2l > main > form > div > div.scrollableContainer-15eg7h.webkit-QgSAqd > div > div.textArea-2CLwUE.textAreaSlate-9-y-k2.slateContainer-3x9zil > div > div.markup-eYLPri.editor-H2NA06.slateTextArea-27tjG0.fontSize16Padding-XoMpjI > div')))
            writer_msg.click()
            writer_msg.send_keys("""Depois de 4 horas de muita dor e sofrimento, saiba, Epicos, que isto é uma mensagem gerada por um script""")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    chrome1 = ChromeAuto()
    chrome1.make_chrome_browser()
    chrome1.access_site('https://discord.com/')
    chrome1.click_login()
    chrome1.write_credentials()
    chrome1.click_user()
    chrome1.write_message()




