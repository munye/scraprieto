import scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
import json



def authentication_failed(response):
    if b'Los datos ingresados son incorrectos' in response.body:
        return True

class LoginSpider(scrapy.Spider):
    name = 'ListaHistoriaClinicaPaciente'

    start_urls = ['http://www.intranet.cardioprieto.com/index.php/hClinica/index']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'usuario': 'omar', 'pass': 'prieto'},
            callback=self.after_login

        )
            
    def after_login(self, response):
        cookiejar = response.meta.setdefault('cookie_jar', CookieJar())
        cookiejar.extract_cookies(response, response.request)
        print("COOOOOOOOKIEEEEEEE:", cookiejar._cookies)
        return
