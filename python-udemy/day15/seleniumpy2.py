from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

        self.chrome_service = Service(executable_path=self.chrome_driver_path, )
        self.browser = webdriver.Chrome(
            service=self.chrome_service,
            options=self.chrome_options
        )
        return self.browser

    def access_site(self, url):
        self.browser.get(url)

    def leave(self):
        self.browser.quit()

    def click_sign_in(self):
        try:
            self.browser.find_element(By.LINK_TEXT, 'Sign in').click()
        except Exception as e:
            print(f'Error in sign in click: {e}')

    def write_credentials(self):
        try:
            email = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.ID, 'login_field')))
            passcode = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.ID, 'password')))
            btn_sign_in = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.NAME, 'commit')))
            email.send_keys('ez998@outlook.com')
            passcode.send_keys('998688124CFal')
            btn_sign_in.click()
        except Exception as e:
            print(f'Error in write credentials: {e}')

    def click_profile(self):
        try:
            profile = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')))
            profile.click()
        except Exception as e:
            print(f'Error in click profile: {e}')

    def click_log_out(self):
        try:
            btn_singout = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')))
            btn_singout.click()
        except Exception as e:
            print(f'Error in click sign out: {e}')

    def check_user(self, username):
        profile_link = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-profile-link')))
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert username in profile_link_html



if __name__ == '__main__':
    gitbrow = ChromeAuto()
    gitbrow.make_chrome_browser()
    gitbrow.access_site('https://github.com/')
    gitbrow.click_sign_in()
    gitbrow.write_credentials()
    gitbrow.click_profile()
    gitbrow.check_user('ViniciusEZ')
    gitbrow.click_log_out()
    gitbrow.click_sign_in()
    gitbrow.write_credentials()
    gitbrow.click_profile()
    gitbrow.check_user('ViniciusEZ2')


# user-profile-link
