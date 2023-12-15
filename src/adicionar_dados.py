from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.core.configs import settings
from src.core.security import gerar_hash_senha
from src.models.categoria_model import CategoriaModel
from src.models.marca_model import MarcaModel
from src.models.produto_model import ProdutoModel
from src.models.usuario_model import UsuarioModel


async_session = sessionmaker(
    bind=create_async_engine(settings.DB_URL, echo=True),
    class_=AsyncSession,
    expire_on_commit=False,
)


async def adicionar_categorias(async_session) -> None:
    print("-" * 100)
    print("Criando as categorias no banco de dados.")

    async with async_session as session:
        categortia_toneira = CategoriaModel(nome="Torneira")
        categortia_porta_toalha = CategoriaModel(nome="Porta Toalha")
        categortia_chuveiro = CategoriaModel(nome="Chuveiro")
        categortia_porcelanato_polido = CategoriaModel(nome="Porcelanato Polido")
        categortia_porcelanato_acetinado = CategoriaModel(nome="Porcelanato Acetinado")

        session.add(categortia_toneira)
        session.add(categortia_porta_toalha)
        session.add(categortia_chuveiro)
        session.add(categortia_porcelanato_polido)
        session.add(categortia_porcelanato_acetinado)

        await session.commit()

    print("Categorias criadas com sucesso.")
    print("-" * 100)


async def adicionar_marcas(async_session) -> None:
    print("-" * 100)
    print("Criando as marcas no banco de dados.")

    async with async_session as session:
        marca_fani = MarcaModel(nome="Fani")
        marca_deca = MarcaModel(nome="Deca")
        marca_docol = MarcaModel(nome="Docol")
        marca_portinari = MarcaModel(nome="Portinari")
        marca_eliane = MarcaModel(nome="Eliane")

        session.add(marca_fani)
        session.add(marca_deca)
        session.add(marca_docol)
        session.add(marca_portinari)
        session.add(marca_eliane)

        await session.commit()

    print("Marcas criadas com sucesso.")
    print("-" * 100)


async def adicionar_produtos(async_session) -> None:
    print("-" * 100)
    print("Criando os produtos no banco de dados.")

    async with async_session as session:
        # Torneira Fani
        produto_fani_torneira_1 = ProdutoModel(
            nome="Torneira de mesa, Linha Flex 99, 1195 99",
            nome_referencia="Torneira de mesa",
            codigo="1195 99",
            marca_id=1,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=449.99,
        )
        produto_fani_torneira_2 = ProdutoModel(
            nome="Torneira de parede, Linha Jade Clássica 182, 1199 182",
            nome_referencia="Torneira de parede",
            codigo="1199 182",
            marca_id=1,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=560,
        )
        produto_fani_torneira_3 = ProdutoModel(
            nome="Torneira de mesa, Linha: Flex 99, 1207 99",
            nome_referencia="Torneira de mesa",
            codigo="1207 99",
            marca_id=1,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=325.50,
        )
        produto_fani_torneira_4 = ProdutoModel(
            nome="Torneira de mesa, Linha: Flex 99, 1208 99",
            nome_referencia="Torneira de mesa",
            codigo="1208 99",
            marca_id=1,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=335.50,
        )
        produto_fani_torneira_5 = ProdutoModel(
            nome="Torneira de mesa, Linha: Lyra 29, 1166 29",
            nome_referencia="Torneira de mesa",
            codigo="1166 29",
            marca_id=1,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=250.49,
        )

        session.add(produto_fani_torneira_1)
        session.add(produto_fani_torneira_2)
        session.add(produto_fani_torneira_3)
        session.add(produto_fani_torneira_4)
        session.add(produto_fani_torneira_5)

        # Torneira Deca
        produto_deca_torneira_1 = ProdutoModel(
            nome="Torneira De Parede Com Bica Móvel Para Cozinha Link Cromado, 1168.C.LNK",
            nome_referencia="Torneira De Parede Com Bica Móvel Para Cozinha Link Cromado",
            codigo="1168.C.LNK",
            marca_id=2,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=524.90,
        )
        produto_deca_torneira_2 = ProdutoModel(
            nome="Toneira De Mesa Para Cozinha Bica Alta Colore Cromado E Preto, 1189.C.PT",
            nome_referencia="Toneira De Mesa Para Cozinha Bica Alta Colore Cromado E Preto",
            codigo="1189.C.PT",
            marca_id=2,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=2303.88,
        )
        produto_deca_torneira_3 = ProdutoModel(
            nome="Bica De Mesa Para Cozinha Deca You Cromado, 1291.C99",
            nome_referencia="Bica De Mesa Para Cozinha Deca You Cromado",
            codigo="1291.C99",
            marca_id=2,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=1908.90,
        )
        produto_deca_torneira_4 = ProdutoModel(
            nome="Misturador Monocomando de Mesa para Cozinha Deca Colore Cromado e Preto, 2289.C.PT",
            nome_referencia="Misturador Monocomando de Mesa para Cozinha Deca Colore Cromado e Preto",
            codigo="2289.C.PT",
            marca_id=2,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=3500.88,
        )
        produto_deca_torneira_5 = ProdutoModel(
            nome="Torneira De Parede Com Arejador Para Cozinha Max Cromado, 1159.C34",
            nome_referencia="Torneira De Parede Com Arejador Para Cozinha Max Cromado",
            codigo="1159.C34",
            marca_id=2,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=341.88,
        )

        session.add(produto_deca_torneira_1)
        session.add(produto_deca_torneira_2)
        session.add(produto_deca_torneira_3)
        session.add(produto_deca_torneira_4)
        session.add(produto_deca_torneira_5)

        # Torneira Docol
        produto_docol_torneira_1 = ProdutoModel(
            nome="Torneira para banheiro Lift, Cod. 00871906",
            nome_referencia="Torneira para banheiro Lift",
            codigo="Cod. 00871906",
            marca_id=3,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=1643.90,
        )
        produto_docol_torneira_2 = ProdutoModel(
            nome="Bica para banheiro 305 Mix&Match grafite escovado, Cod. 00916470",
            nome_referencia="Bica para banheiro 305 Mix&Match grafite escovado",
            codigo="Cod. 00916470",
            marca_id=3,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=1547.30,
        )
        produto_docol_torneira_3 = ProdutoModel(
            nome="Torneira para banheiro Nova Lóggica, Cod. 01106406",
            nome_referencia="Torneira para banheiro Nova Lóggica",
            codigo="Cod. 01106406",
            marca_id=3,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=378.80,
        )
        produto_docol_torneira_4 = ProdutoModel(
            nome="Torneira para banheiro Docol Stillo, Cod. 00820206",
            nome_referencia="Torneira para banheiro Docol Stillo",
            codigo="Cod. 00820206",
            marca_id=3,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=836.40,
        )
        produto_docol_torneira_5 = ProdutoModel(
            nome="Torneira para banheiro Benefit PressMatic, Cod. 00490706",
            nome_referencia="Torneira para banheiro Benefit PressMatic",
            codigo="Cod. 00490706",
            marca_id=3,
            categoria_id=1,
            unidade_de_venda="UN",
            valor=589.98,
        )

        session.add(produto_docol_torneira_1)
        session.add(produto_docol_torneira_2)
        session.add(produto_docol_torneira_3)
        session.add(produto_docol_torneira_4)
        session.add(produto_docol_torneira_5)

        # Porta Toalha Fani
        porta_toalha_fani_1 = ProdutoModel(
            nome="Porta-toalha reto longo, Linha: Soft 195, 4400 195",
            nome_referencia="Porta-toalha reto longo",
            codigo="4400 195",
            marca_id=1,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=698.45,
        )
        porta_toalha_fani_2 = ProdutoModel(
            nome="Porta-toalha Reto Curto, Linha: Soft 195, 4410 195",
            nome_referencia="Porta-toalha Reto Curto",
            codigo="4410 195",
            marca_id=1,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=620.50,
        )
        porta_toalha_fani_3 = ProdutoModel(
            nome="Porta-toalha duplo longo, Linha Lunna 185, 4900 185",
            nome_referencia="Porta-toalha duplo longo",
            codigo="4900 185",
            marca_id=1,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=890.90,
        )

        session.add(porta_toalha_fani_1)
        session.add(porta_toalha_fani_2)
        session.add(porta_toalha_fani_3)

        # Porta Toalha Deca
        porta_toalha_deca_1 = ProdutoModel(
            nome="Porta toalhas barra 60cm, 2040.C104.060",
            nome_referencia="Porta toalhas barra 60cm",
            codigo="2040.C104.060",
            marca_id=2,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=872.41,
        )
        porta_toalha_deca_2 = ProdutoModel(
            nome="Porta Toalha Barra Clean 60 Cm Cromado, 2040.C.060.CLN",
            nome_referencia="Porta Toalha Barra Clean 60 Cm Cromado",
            codigo="2040.C.060.CLN",
            marca_id=2,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=993.90,
        )
        porta_toalha_deca_3 = ProdutoModel(
            nome="Porta Toalha Barra Polo 50 Cm Cromado, 2040.C33.050",
            nome_referencia="Porta Toalha Barra Polo 50 Cm Cromado",
            codigo="2040.C33.050",
            marca_id=2,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=754.90,
        )

        session.add(porta_toalha_deca_1)
        session.add(porta_toalha_deca_2)
        session.add(porta_toalha_deca_3)

        # Porta Toalha Docol
        porta_toalha_docol_1 = ProdutoModel(
            nome="Porta-toalhas de rosto Docol Flat, Cod. 01013606",
            nome_referencia="Porta-toalhas de rosto Docol Flat",
            codigo="Cod. 01013606",
            marca_id=3,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=749.82,
        )
        porta_toalha_docol_2 = ProdutoModel(
            nome="Porta-toalhas duplo Docol Flat, Cod. 01013706",
            nome_referencia="Porta-toalhas duplo Docol Flat",
            codigo="Cod. 01013706",
            marca_id=3,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=1580.10,
        )
        porta_toalha_docol_3 = ProdutoModel(
            nome="Porta toalha Docolflat Ônix, Cod. 009613CE",
            nome_referencia="Porta toalha Docolflat Ônix",
            codigo="Cod. 009613CE",
            marca_id=3,
            categoria_id=2,
            unidade_de_venda="UN",
            valor=1030.29,
        )

        session.add(porta_toalha_docol_1)
        session.add(porta_toalha_docol_2)
        session.add(porta_toalha_docol_3)

        # Chuveiro Fani
        chuveiro_fani_1 = ProdutoModel(
            nome="Chuveiro articulado de teto, Linha: Mix Plus 501, 3100 501",
            nome_referencia="Chuveiro articulado de teto",
            codigo="3100 501",
            marca_id=1,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=2483.52,
        )
        chuveiro_fani_2 = ProdutoModel(
            nome="Chuveiro flexível de parede, Linha: Flex 99, 3000 99",
            nome_referencia="Chuveiro flexível de parede",
            codigo="3000 99",
            marca_id=1,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=897.45,
        )
        chuveiro_fani_3 = ProdutoModel(
            nome="Chuveiro flexível de parede com desviador, Linha: Flex 99, 3300 99",
            nome_referencia="Chuveiro flexível de parede com desviador",
            codigo="3300 99",
            marca_id=1,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=1853.79,
        )

        session.add(chuveiro_fani_1)
        session.add(chuveiro_fani_2)
        session.add(chuveiro_fani_3)

        # Chuveiro Deca
        chuveiro_deca_1 = ProdutoModel(
            nome="Desviador Para Chuveiro Desviador Universal Cromado, 1982.C",
            nome_referencia="Desviador Para Chuveiro Desviador Universal Cromado",
            codigo="1982.C",
            marca_id=2,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=1452.90,
        )
        chuveiro_deca_2 = ProdutoModel(
            nome="Chuveiro Com Tubo Para Teto Unic 40 Cm Cromado, 1969.C.TET.040",
            nome_referencia="Chuveiro Com Tubo Para Teto Unic 40 Cm Cromado",
            codigo="1969.C.TET.040",
            marca_id=2,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=999.90,
        )
        chuveiro_deca_3 = ProdutoModel(
            nome="Chuveiro Com Tubo De Teto Aquamax Cromado, 1998.C.TET",
            nome_referencia="Chuveiro Com Tubo De Teto Aquamax Cromado",
            codigo="1998.C.TET",
            marca_id=2,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=3292.86,
        )

        session.add(chuveiro_deca_1)
        session.add(chuveiro_deca_2)
        session.add(chuveiro_deca_3)

        # Chuveiro Deca
        chuveiro_docol_1 = ProdutoModel(
            nome="Chuveiro Technoshower com Desviador, Cod. 01511606",
            nome_referencia="Chuveiro Technoshower com Desviador",
            codigo="Cod. 01511606",
            marca_id=3,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=3899.90,
        )
        chuveiro_docol_2 = ProdutoModel(
            nome="Chuveiro Docol Heaven Q200, Cod. 00888206",
            nome_referencia="Chuveiro Docol Heaven Q200",
            codigo="Cod. 00888206",
            marca_id=3,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=3020.97,
        )
        chuveiro_docol_3 = ProdutoModel(
            nome="Chuveiro novo Technoshower Ônix, Cod. 012048CE",
            nome_referencia="Chuveiro novo Technoshower Ônix",
            codigo="Cod. 012048CE",
            marca_id=3,
            categoria_id=3,
            unidade_de_venda="UN",
            valor=5643.65,
        )

        session.add(chuveiro_docol_1)
        session.add(chuveiro_docol_2)
        session.add(chuveiro_docol_3)

        # Porcelanato Polido Portinari
        porcelanato_polido_portinari_1 = ProdutoModel(
            nome="LIRIC WH POL 1200,0X1200,0X9,2MM, 62469",
            nome_referencia="LIRIC WH POL 1200,0X1200,0X9,2MM",
            codigo="62469",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=142.20,
        )
        porcelanato_polido_portinari_2 = ProdutoModel(
            nome="RARITA BL POL 1200,0X1200,0X9,2MM, 62470",
            nome_referencia="RARITA BL POL 1200,0X1200,0X9,2MM",
            codigo="62470",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=125.80,
        )
        porcelanato_polido_portinari_3 = ProdutoModel(
            nome="RARITA GR POL 1200,0X1200,0X9,2MM, 62471",
            nome_referencia="RARITA GR POL 1200,0X1200,0X9,2MM",
            codigo="62471",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=135.76,
        )
        porcelanato_polido_portinari_4 = ProdutoModel(
            nome="SICILIA OFW POL 877,0X877,0X9,5MM, 61471",
            nome_referencia="SICILIA OFW POL 877,0X877,0X9,5MM",
            codigo="61471",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=105.76,
        )
        porcelanato_polido_portinari_5 = ProdutoModel(
            nome="SONETO MARBLE GR POL 1200,0X2400,0X9MM, 61032",
            nome_referencia="SONETO MARBLE GR POL 1200,0X2400,0X9MM",
            codigo="61032",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=148.53,
        )
        porcelanato_polido_portinari_6 = ProdutoModel(
            nome="TIMELESS WH POL 1200,0X1200,0X9,2MM, 62619",
            nome_referencia="TIMELESS WH POL 1200,0X1200,0X9,2MM",
            codigo="62619",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=124.86,
        )
        porcelanato_polido_portinari_7 = ProdutoModel(
            nome="TIVOLI SBE POL 877,0X877,0X9,5MM, 61847",
            nome_referencia="TIVOLI SBE POL 877,0X877,0X9,5MM",
            codigo="61847",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=133.95,
        )
        porcelanato_polido_portinari_8 = ProdutoModel(
            nome="YORK SGR POL 1200,0X1200,0X9,2MM, 62621",
            nome_referencia="YORK SGR POL 1200,0X1200,0X9,2MM",
            codigo="62621",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=168.74,
        )
        porcelanato_polido_portinari_9 = ProdutoModel(
            nome="YORK WH POL 1200,0X1200,0X9,2MM, 62622",
            nome_referencia="YORK WH POL 1200,0X1200,0X9,2MM",
            codigo="62622",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=99.99,
        )
        porcelanato_polido_portinari_10 = ProdutoModel(
            nome="YORK WH POL 877,0X877,0X9,5MM, 61310",
            nome_referencia="YORK WH POL 877,0X877,0X9,5MM",
            codigo="61310",
            marca_id=4,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=95.78,
        )

        session.add(porcelanato_polido_portinari_1)
        session.add(porcelanato_polido_portinari_2)
        session.add(porcelanato_polido_portinari_3)
        session.add(porcelanato_polido_portinari_4)
        session.add(porcelanato_polido_portinari_5)
        session.add(porcelanato_polido_portinari_6)
        session.add(porcelanato_polido_portinari_7)
        session.add(porcelanato_polido_portinari_8)
        session.add(porcelanato_polido_portinari_9)
        session.add(porcelanato_polido_portinari_10)

        # Porcelanato Polido Eliane
        porcelanato_polido_eliane_1 = ProdutoModel(
            nome="KHALI MARFIM PO 100x100cm, 8055699",
            nome_referencia="KHALI MARFIM PO 100x100cm",
            codigo="8055699",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=123.75,
        )
        porcelanato_polido_eliane_2 = ProdutoModel(
            nome="KHALI OFF WHITE PO 100x100cm, 8055698",
            nome_referencia="KHALI OFF WHITE PO 100x100cm",
            codigo="8055698",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=134.75,
        )
        porcelanato_polido_eliane_3 = ProdutoModel(
            nome="MONT BLANC PO 100x100cm, 8055704",
            nome_referencia="MONT BLANC PO 100x100cm",
            codigo="8055704",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=158.75,
        )
        porcelanato_polido_eliane_4 = ProdutoModel(
            nome="MUNARI BRANCO PO 100x100cm, 8055695",
            nome_referencia="MUNARI BRANCO PO 100x100cm",
            codigo="8055695",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=113.85,
        )
        porcelanato_polido_eliane_5 = ProdutoModel(
            nome="MUNARI CIMENTO PO 100x100cm, 8055697",
            nome_referencia="MUNARI CIMENTO PO 100x100cm",
            codigo="8055697",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=168.74,
        )
        porcelanato_polido_eliane_6 = ProdutoModel(
            nome="MUNARI MARFIM PO 100x100cm, 8055696",
            nome_referencia="MUNARI MARFIM PO 100x100cm",
            codigo="8055696",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=184.72,
        )
        porcelanato_polido_eliane_7 = ProdutoModel(
            nome="ONIX CRISTAL PO 100x100cm, 8055700",
            nome_referencia="ONIX CRISTAL PO 100x100cm",
            codigo="8055700",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=181.85,
        )
        porcelanato_polido_eliane_8 = ProdutoModel(
            nome="SILEX VEGGIE PO 90x90cm, 8049644",
            nome_referencia="SILEX VEGGIE PO 90x90cm",
            codigo="8049644",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=148.36,
        )
        porcelanato_polido_eliane_9 = ProdutoModel(
            nome="KHALI OFF WHITE PO 60x120cm, 8049786",
            nome_referencia="KHALI OFF WHITE PO 60x120cm",
            codigo="8049786",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=193.74,
        )
        porcelanato_polido_eliane_10 = ProdutoModel(
            nome="KHALI MARFIM PO 60x120cm, 8049787",
            nome_referencia="KHALI MARFIM PO 60x120cm",
            codigo="8049787",
            marca_id=5,
            categoria_id=4,
            unidade_de_venda="M²",
            valor=167.43,
        )

        session.add(porcelanato_polido_eliane_1)
        session.add(porcelanato_polido_eliane_2)
        session.add(porcelanato_polido_eliane_3)
        session.add(porcelanato_polido_eliane_4)
        session.add(porcelanato_polido_eliane_5)
        session.add(porcelanato_polido_eliane_6)
        session.add(porcelanato_polido_eliane_7)
        session.add(porcelanato_polido_eliane_8)
        session.add(porcelanato_polido_eliane_9)
        session.add(porcelanato_polido_eliane_10)

        # Porcelanato Acetinado Portinari
        porcelanato_acetinado_portinari_1 = ProdutoModel(
            nome="MEZZO BE NAT 800,0X1600,0X10,0MM, 62481",
            nome_referencia="MEZZO BE NAT 800,0X1600,0X10,0MM",
            codigo="62481",
            marca_id=4,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=275.63,
        )
        porcelanato_acetinado_portinari_2 = ProdutoModel(
            nome="LIRIC WH NAT 1200,0X1200,0X9,2MM, 62463",
            nome_referencia="LIRIC WH NAT 1200,0X1200,0X9,2MM",
            codigo="62463",
            marca_id=4,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=233.45,
        )
        porcelanato_acetinado_portinari_3 = ProdutoModel(
            nome="BOULEVARD SGR NAT 1200,0X1200,0X9,2MM, 62465",
            nome_referencia="BOULEVARD SGR NAT 1200,0X1200,0X9,2MM",
            codigo="62465",
            marca_id=4,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=168.75,
        )
        porcelanato_acetinado_portinari_4 = ProdutoModel(
            nome="AUDAZ DGR NAT 1000,0X1000,0X9,0MM, 62458",
            nome_referencia="AUDAZ DGR NAT 1000,0X1000,0X9,0MM",
            codigo="62458",
            marca_id=4,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=147.77,
        )
        porcelanato_acetinado_portinari_5 = ProdutoModel(
            nome="AUDAZ BK NAT 1000,0X1000,0X9,0MM, 62456",
            nome_referencia="AUDAZ BK NAT 1000,0X1000,0X9,0MM",
            codigo="62456",
            marca_id=4,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=176.35,
        )

        session.add(porcelanato_acetinado_portinari_1)
        session.add(porcelanato_acetinado_portinari_2)
        session.add(porcelanato_acetinado_portinari_3)
        session.add(porcelanato_acetinado_portinari_4)
        session.add(porcelanato_acetinado_portinari_5)

        # Porcelanato Acetinado Eliane
        porcelanato_acetinado_eliane_1 = ProdutoModel(
            nome="KHALI OFF WHITE AC 120x120cm, 8049584",
            nome_referencia="KHALI OFF WHITE AC 120x120cm",
            codigo="8049584",
            marca_id=5,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=278.65,
        )
        porcelanato_acetinado_eliane_2 = ProdutoModel(
            nome="KHALI MARFIM AC 120x120cm, 8049585",
            nome_referencia="KHALI MARFIM AC 120x120cm",
            codigo="8049585",
            marca_id=5,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=195.34,
        )
        porcelanato_acetinado_eliane_3 = ProdutoModel(
            nome="KHALI GREIGE AC 120x120cm, 8049586",
            nome_referencia="KHALI GREIGE AC 120x120cm",
            codigo="8049586",
            marca_id=5,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=210.30,
        )
        porcelanato_acetinado_eliane_4 = ProdutoModel(
            nome="MUNARI MARFIM AC 120x120cm, 8050279",
            nome_referencia="MUNARI MARFIM AC 120x120cm",
            codigo="8050279",
            marca_id=5,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=259.84,
        )
        porcelanato_acetinado_eliane_5 = ProdutoModel(
            nome="GUACHE TERRACOTA MA 120x120cm, 8049572",
            nome_referencia="GUACHE TERRACOTA MA 120x120cm",
            codigo="8049572",
            marca_id=5,
            categoria_id=5,
            unidade_de_venda="M²",
            valor=168.88,
        )

        session.add(porcelanato_acetinado_eliane_1)
        session.add(porcelanato_acetinado_eliane_2)
        session.add(porcelanato_acetinado_eliane_3)
        session.add(porcelanato_acetinado_eliane_4)
        session.add(porcelanato_acetinado_eliane_5)

        await session.commit()

    print("Produtos criados com sucesso.")
    print("-" * 100)


async def adicionar_usuarios(async_session) -> None:
    print("-" * 100)
    print("Criando as usuários no banco de dados.")

    async with async_session as session:
        usuario_admin = UsuarioModel(
            cpf="12221405609",
            nome="Italo",
            sobrenome="Silva Fernandes Admin",
            telefone="34992127233",
            email="italoadmin@email.com",
            senha=gerar_hash_senha("290302"),
            permissao_id=1,
        )
        usuario_vendedor = UsuarioModel(
            cpf="12221405609",
            nome="Italo",
            sobrenome="Silva Fernandes Vendedor",
            telefone="34992127233",
            email="italovendedor@email.com",
            senha=gerar_hash_senha("290302"),
            permissao_id=2,
        )
        usuario_cliente = UsuarioModel(
            cpf="12221405609",
            nome="Italo",
            sobrenome="Silva Fernandes Cliente",
            telefone="34992127233",
            email="italocliente@email.com",
            senha=gerar_hash_senha("290302"),
            permissao_id=3,
        )

        session.add(usuario_admin)
        session.add(usuario_vendedor)
        session.add(usuario_cliente)

        await session.commit()

    print("Usuários criadas com sucesso.")
    print("-" * 100)


async def main():
    async with async_session() as session:
        await adicionar_categorias(session)
        await adicionar_marcas(session)
        await adicionar_produtos(session)
        await adicionar_usuarios(session)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
