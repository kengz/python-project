# Notebook for development using VSCode interactive Python
from loguru import logger

from proj import cfg, main


sample_path = cfg.data.sample.path
with open(sample_path, 'w') as f:
    f.write(main.greet())

logger.info(f'Written to {sample_path}')
