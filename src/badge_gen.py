# badge_gen.py

# Utility methods
def __text_gen(txt : str, txt_url : str = None) -> str:
    if txt_url:
        return '<a href="{txt_url}" class="jh-text-badge" markdown>{txt}</a>'.format(
            txt_url=txt_url, txt=txt)
    else:
        return '<span class="jh-text-badge" markdown>{txt}</span>'.format(txt=txt)
    

def __icon_gen(icon: str, tooltip: str, url: str = None) -> str:
    if url:
        return '<a href="{url}" title="{tooltip}" class="jh-icon-badge" markdown>{icon}</a>'.format(
            icon=icon, url=url, tooltip=tooltip)
    else:
        return '<span title="{tooltip}" class="jh-icon-badge" markdown>{icon}</span>'.format(
            icon=icon, tooltip=tooltip)

def badge(icon: str,
          tooltip: str,
          icon_url: str = None,
          txt : str = None,
          txt_url : str = None) -> str:
    """
    Creates a badge element from an icon, text, urls, and a tooltip.

    Badges can be used to concisely display information with optional links.
    Badges should always have an icon and tooltip. Text should be kept short,
    preferably one word.
    """
    icon_html = __icon_gen(icon, tooltip, icon_url)
    if txt:
        txt_html = __text_gen(txt, txt_url)
        return '<p class="jh-badge" markdown>{} {}</p>'.format(icon_html, txt_html)
    else:
        return '<p class="jh-badge" markdown>{}</p>'.format(icon_html)
    
def version_badge(version: str, indent : str = '') -> str:
        if not version:
            return ''
        return badge(':material-tag:', 'Version', '../templates', version)

def author_badge(name: str, url: str, indent : str = '') -> str:
    return badge(':octicons-person-fill-24:', 'Contributor', 'http://todo', 
                 name, url)

def hsi_badge(indent : str = '') -> str:
    return badge(':material-cog:', 'Uses heat set inserts', None)

def mcu_count_badge(txt, indent : str ='') -> str:
    return badge(':fontawesome-solid-microchip:', 'Number of MCUs per tray',
                icon_url=None, txt=txt)

def short_tray_badge() -> str:
    return ''

def base_depth_badge(txt: str) -> str:
    return badge(':material-format-vertical-align-bottom:',
                 "Required Base depth", 'https://TODO',txt)

def switch_badge(txt: str) -> str:
    return badge(':material-power:', 'Power switch options',
                 'https://TODO', txt)

def display_badge(txt : str) -> str:
    return badge(':material-monitor-dashboard:', 'Display type (CPU or MCU)',
                 'https://TODO', txt)