{%- macro template(txt) -%}
{{ make_badge(':material-puzzle:', 'Part template', txt=txt) }}
{%- endmacro -%}

{%- macro author(name, url) -%}
{{ make_badge(':octicons-person-fill-24:', 'Contributed by', '', name, url) }}
{%- endmacro -%}

{%- macro hsi() -%}
{{ make_badge(':material-cog:', 'Uses heat set inserts', None) }}
{%- endmacro -%}

{%- macro origin(txt, txt_url) -%}
{{ make_badge(':material-source-branch:', 'Based on work by', txt=txt, txt_url=txt_url) }}
{%- endmacro -%}

{%- macro version(txt) -%}
{{ make_badge(':material-tag:', 'Version', txt=txt) }}
{%- endmacro -%}

{%- macro qty(txt) -%}
{{ make_badge(':material-chip:', 'Number of parts mounted per tray', txt=txt) }}
{%- endmacro -%}

{%- macro size(txt) -%}
{%- set sz = txt.capitalize() -%}
{{ make_badge(':material-relative-scale:', 'Printed component size', txt=sz) }}
{%- endmacro -%}

{%- macro base_depth(txt) -%}
{{ make_badge(':material-format-vertical-align-bottom:', 'Required Base depth', txt=txt) }}
{%- endmacro -%}

{%- macro switch(txt) -%}
{{ make_badge(':material-power:', 'Compatible power switch type(s)', txt=txt) }}
{%- endmacro -%}

{%- macro iec(value) -%}
{%- if value -%}
{{ make_badge(':material-power-plug:', 'This component provides an IEC C14 power socket.') }}
{%- else -%}
{{ make_badge(':material-power-plug-off-outline:', 'This component does not provide an IEC power socket.') }}
{%- endif -%}
{%- endmacro -%}

{%- macro display(txt) -%}
{{ make_badge(':material-monitor:', 'Display type (CPU or MCU)', txt=txt) }}
{%- endmacro -%}

{%- macro front() -%}
{{ make_badge(':material-format-horizontal-align-left:', 'This is the front half of a larger component', 
                 txt='Front') }}
{%- endmacro -%}

{%- macro rear() -%}
{{ make_badge(':material-format-horizontal-align-right:', 'This is the rear half of a larger component', txt='Rear') }}
{%- endmacro -%}

{%- macro unified() -%}
{{ make_badge(':material-vector-combine:', 'Unified parts replace front and rear halves', txt='Unified')}}
{%- endmacro -%}

{%- macro half(txt) -%}
{%- set up = txt.upper() -%}
{%- if up == 'FRONT' -%}
{{ front() }}
{%- elif up == 'REAR' -%}
{{ rear() }}
{%- elif up == 'UNIFIED' -%}
{{ unified() }}
{%- endif -%}
{%- endmacro -%}

{%- macro vent() -%}
{{ make_badge(':material-air-filter:', 'Provides ventilation') }}
{%- endmacro -%}

{%- macro fan() -%}
{{ make_badge(':material-fan:', 'Mounts at least one fan') }}
{%- endmacro -%}

{%- macro extension(txt) -%}
{{ make_badge(':material-connection:', 'Panel mounts provided', txt=txt) }}
{%- endmacro -%}

{%- macro render(comp, variant, prefix='') -%}
<div markdown>
{%- set ckeys = comp.attributes.keys() -%}
{%- set vkeys = variant.attributes.keys() -%}
{%- if variant.template -%}
{{ template(variant.template) }}
{%- elif comp.template -%}
{{ template(comp.template) }}
{%- endif -%}
{%- if variant.author -%}
{{ author(variant.author.name, variant.author.url) }}
{%- endif -%}
{%- if 'origin' in vkeys -%}
{%- set o_auth = authorForId(variant.attributes['origin']) -%}
{%- elif 'origin' in ckeys -%}
{%- set o_auth = authorForId(comp.attributes['origin']) -%}
{%- endif -%}
{%- if o_auth -%}
{{ origin(o_auth.name, o_auth.url) }}
{%- endif -%}
{%- if 'version' in vkeys -%}
{{ version(variant.attributes['version']) }}
{%- elif 'version' in ckeys -%}
{{ version(comp.attributes['version']) }}
{%- endif -%}
{%- if 'half' in vkeys -%}
{{ half(variant.attributes['half']) }}
{%- endif -%}
{%- if 'length' in vkeys -%}
{{ size(variant.attributes['length']) }}
{%- elif 'length' in ckeys -%}
{{ size(comp.attributes['length']) }}
{%- endif -%}
{%- if 'base_depth' in vkeys -%}
{{ base_depth(variant.attributes['base_depth'])}}
{%- elif 'base_depth' in ckeys -%}
{{ base_depth(comp.attributes['base_depth'])}}
{%- endif -%}
{%- if 'display_type' in vkeys -%}
{{ display(variant.attributes['display_type']) }}
{%- elif 'display_type' in ckeys -%}
{{ display(comp.attributes['display_type']) }}
{%- endif -%}
{%- if 'switch' in vkeys -%}
{{ switch(variant.attributes['switch']) }}
{%- elif 'switch' in ckeys -%}
{{ switch(comp.attributes['switch']) }}
{%- endif -%}
{%- if 'count' in vkeys -%}
{{ qty(variant.attributes['count']) }}
{%- elif 'count' in ckeys -%}
{{ qty(comp.attributes['count']) }}
{%- endif -%}
{%- if 'mounts' in vkeys -%}
{{ extension(variant.attributes['mounts']) }}
{%- elif 'mounts' in ckeys -%}
{{ extension(comp.attributes['mounts']) }}
{%- endif -%}
{%- if 'iec' in ckeys -%}
{{ iec(comp.attributes['iec']) }}
{%- elif 'iec' in vkeys -%}
{{ iec(variant.attributes['iec']) }}
{%- endif -%}
{%- if 'vent' in  ckeys or 'vent' in vkeys -%}
{{ vent() }}
{%- endif -%}
{%- if 'fan' in  ckeys or 'fan' in vkeys -%}
{{ fan() }}
{%- endif -%}
{%- if 'hsi' in ckeys or 'hsi' in vkeys -%}
{{ hsi() }}
{%- endif -%}
</div>
{%- endmacro -%}
