from repositories.vendendor_repository import VendendorRepository

class VendendorService:
    def cadastrar_vendendor(id_pessoa, data_cadastro):
        vendendor = VendendorRepository()
        return vendendor.cadastrar_vendedor(id_pessoa, data_cadastro)