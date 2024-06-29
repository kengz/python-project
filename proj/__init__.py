from pathlib import Path

import hydra

CWD = Path(__file__).parent
DIR = CWD.parent


def get_cfg(config_dir: str = str(CWD / 'conf'), config_name: str = 'config.yaml', overrides: list = []):
    with hydra.initialize_config_dir(version_base=None, config_dir=config_dir):
        cfg = hydra.compose(config_name, overrides=overrides)
    return cfg


cfg = get_cfg()
# NOTE config accessible via `from proj import cfg`
