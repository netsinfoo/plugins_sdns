from extras.plugins import PluginConfig


class SdnsConfig(PluginConfig):
    """Essa classe define o plugin do sdns."""

    name = 'sdns'
    verbose_name = 'sdns'
    description = 'Dns Plugin'
    version = '1.0'
    author = 'Manoel Bezerra'
    author_email = 'manoelbezerra@info.ufrn.br' 
    base_url = 'sdns'
    required_settings = []
    default_settings = {}

config = SdnsConfig