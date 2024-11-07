from loguru import logger

logger.debug("um aviso para o desenvolvedor")
logger.info("informacao importante do processo")
logger.warning("um aviso que algo vai para de funcionar no futuro")
logger.error("aconteceu uma falha")
logger.critical("aconteceu um problema que aborta a aplicacao")