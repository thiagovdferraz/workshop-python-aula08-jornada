from loguru import logger

# Configurando o arquivo de log com rotação de 5MB
# A opção rotation determina que um novo arquivo será criado sempre que o atual atingir 5MB.
logger.add("meu_app.log", rotation="5 MB")

logger.info("Essa mensagem será salva no arquivo")