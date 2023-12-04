from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
import time

class ForexConverter:
    def __init__(self):
        self.converter = CurrencyRates()
        self.btc_converter = BtcConverter()
        self.historique = []

    def convert(self, montant, devise_origine, devise_destination):
        if devise_destination == 'BTC':
            resultat = self.btc_converter.convert_to_btc(montant, devise_origine)
        else:
            resultat = self.converter.convert(devise_origine, devise_destination, montant)
        print(f"{montant} {devise_origine} = {resultat} {devise_destination}")
        self.historique.append((time.time(), montant, devise_origine, devise_destination, resultat))
        return resultat

    def get_historique(self):
        for timestamp, montant, devise_origine, devise_destination, resultat in self.historique:
            print(f"{time.ctime(timestamp)} : {montant} {devise_origine} = {resultat} {devise_destination}")

monnaie_a = input("Entrez la devise d'origine : ")
monnaie_b = input("Entrez la devise de destination : ")
montant = float(input("Entrez le montant à convertir : "))

forex_converter = ForexConverter()
forex_converter.convert(montant, monnaie_a, monnaie_b)
forex_converter.get_historique()