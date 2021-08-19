# Uma simples biblioteca de gerenciamento de Banco de Dados de Chave-Valor
# para apenas armazenar a pontuação máxima e talvez algo mais que possa
# ter no futuro
import pickledb

def load_db() -> pickledb.PickleDB:
  """ Carrega o banco de dados """

  # Auto Dump -> True para salvar automaticamente no arquivo
  db = pickledb.load('database.db', True)

  return db