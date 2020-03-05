import scrapy
from scrapy.http import Request
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
        if authentication_failed(response):
            self.logger.error("ERROR EN USUARIO O PASSWORD AL INGRESAR AL SISTEMA")
            return
        link = 'http://www.intranet.cardioprieto.com/index.php/hClinica/index'
        yield Request(url=link, callback=self.parse_listado_hc)

    def parse_listado_hc(self, response):
        
        #table = response.xpath('//*[@class="html body div.mainContainer div.main.col-lg-10 div.content div.row div.col-lg-12 div.panel.panel-default div.panel-body div.table-responsive table#dataTables-example.table.table-striped.table-bordered.table-hover"]//tbody')
        #rows = table.xpath('//tr')

        rows = response.xpath('/html/body/div[2]/div[2]/div/div/div/div/div[6]/div/table/tbody//tr')
        for row in rows:
            print(row.extract())
        #currentHC = {
        #        'numero' : row.xpath('td[1]//text').extract_first(),
        #        'nombre' : row.xpath('td[2]//text').extract_first(),
        #        'apellido' : row.xpath('td[3]//text').extract_first(),
        #        'documento' : row.xpath('td[3]//text').extract_first(),
        #        'linkHC' : row.xpath('td[4]//text').extract_first(),
        #        'linkEstudios' : row.xpath('td[5]//text').extract_first(),
        #        }
        #print(currentHC)
