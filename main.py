from bdc_sample.postgisAccessor import PostgisAccessor
from bdc_sample.drivers.embrapa import Embrapa
from bdc_sample.drivers.inSitu import InSitu
from bdc_sample.drivers.dpi import Dpi


if __name__ == '__main__':
    storager = PostgisAccessor(host='localhost', username='postgres', password='postgres', database='amostras')

    embrapa = Embrapa('/data/Embrapa/Pontos_Coletados_Embrapa', storager=storager)

    embrapa.load_data_sets()

    embrapa.store()

    driver = InSitu('/data/inSitu', storager=storager)

    driver.load_data_sets()

    driver.store()

    dpi = Dpi('/data/Ieda/', storager=storager)

    dpi.load_data_sets()

    dpi.store()