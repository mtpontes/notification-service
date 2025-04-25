from logging import getLogger, INFO, basicConfig

basicConfig(
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log = getLogger()