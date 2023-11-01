import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_oteta_liikaa(self):
        self.varasto.lisaa_varastoon(3)

        # halutaan ottaa 4, mutta saadaan vain varastossa oleva 3
        self.assertAlmostEqual(self.varasto.ota_varastosta(4), 3)

    def test_ei_laiteta_liikaa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_annettu_vaara_tilavuus(self):
        varasto = Varasto(-5)

        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_annettu_vaara_saldo(self):
        varasto = Varasto(5, alku_saldo=-5)

        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_lisays_vaara(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_otto_vaara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.saldo, 4)

    def test_oikea_tulostus(self):
        self.varasto.lisaa_varastoon(4)

        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 4, vielä tilaa 6")