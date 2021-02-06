from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:sdns:register_list',
        link_text='Registros',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:register_add',
                title='Add a new register',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:register_add',
                title='Import news registers',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_register']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:sdns:domain_list',
        link_text='Dominios',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:domain_add',
                title='Add a new Domain',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:domain_add',
                title='Import news domains',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_domain']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:sdns:resp_list',
        link_text='Responsáveis',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:resp_add',
                title='Add a new Resp',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:resp_add',
                title='Import news resps',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_resp']
            ),
        )
    ),
   PluginMenuItem(
        link='plugins:sdns:ns_list',
        link_text='NameServer',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:ns_add',
                title='Add a new register Ns',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:ns_add',
                title='Import news registers NS',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_ns']
            ),
        )
    ),
     PluginMenuItem(
        link='plugins:sdns:mx_list',
        link_text='Mail_Server',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:mx_add',
                title='Add a new register Mx',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:ns_add',
                title='Import news registers Mx',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_mx']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:sdns:cts_list',
        link_text='Cname,Txt,SPF',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:cts_add',
                title='Add a new Resp',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:cts_add',
                title='Import news ctss',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_cts']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:sdns:domainserv_list',
        link_text='Servidores de Dominio',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:domainserv_add',
                title='Add a new Domain Server',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
            ),
            PluginMenuButton(
                link='plugins:sdns:domainserv_add',
                title='Import news Domain Servers',
                icon_class='mdi mdi-database-import-outline',
                color=ButtonColorChoices.BLUE,
                permissions=['sdns.add_domainserv']
            ),
        )
    ),
)