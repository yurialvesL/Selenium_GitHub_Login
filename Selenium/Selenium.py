from types import NoneType
from selenium import webdriver
from time import sleep
import os

class ChromeAuto:
    def __init__(self):
        self.driver_path= 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options

            )
        self.usuario=os.getenv('github_usu') #seu usuário do github
        self.senha=os.getenv('github_se') #sua senha do github
    def clica_sign_in(self):
        try:
            btn_sign_up= self.chrome.find_elements_by_link_text('Sign up')[0].click()
            btn_sign_in=self.chrome.find_elements_by_link_text('Sign in →')[0].click()
           
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)
            
    def clica_perfil(self):
        try:
            perfil = self.chrome.find_elements_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')[0]
            perfil.click()

        except Exception as e:
            print('Erro ao clicar no perfil:', e)


    def desloga(self):
        try:
            perfil = self.chrome.find_elements_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')[0]
            perfil.click()
            sleep(2)
            desloga= self.chrome.find_elements_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')[0]
            desloga.click()

        except Exception as e:
            print('Erro ao deslogar ', e)
    
    def verifica_usuario(self,usuario):
        profile_link=self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html= profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    
    def acessa(self,site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login=self.chrome.find_elements_by_id('login_field')[0]
            input_password=self.chrome.find_elements_by_id('password')[0]
            btn_login= self.chrome.find_elements_by_name('commit')[0]
            sleep(3)
            input_login.send_keys(self.usuario)
            sleep(3)
            input_password.send_keys(self.senha)
            sleep(3)
            btn_login.click()
            

        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome=ChromeAuto()
    chrome.acessa('https://github.com')
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.clica_perfil()
    sleep(2)
    chrome.verifica_usuario('yurialvesL')
    
    sleep(4)
    chrome.sair()

