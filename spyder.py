import scrapy

def authentication_failed(response):
    if b'Los datos ingresados son incorrectos' in response.body:
        return True

class LoginSpider(scrapy.Spider):
    name = 'ListaHistoriaClinicaPaciente'
    start_urls = ['http://www.intranet.cardioprieto.com/index.php/hClinica/index']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'usuario': 'osmar', 'pass': 'prieto'},
            callback=self.after_login
        )
            
    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("ERROR EN USUARIO O PASSWORD AL INGRESAR AL SISTEMA")
            return

        print("CHOTA")
