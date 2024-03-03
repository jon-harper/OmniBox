{%- macro embed_video(url) -%}
<video controls="">
    <source src="{{url}}" type="video/mp4">
</video>
{%- endmacro -%}

{% macro overview_video(url) -%}
??? overview
{{make_indented(embed_video(url), '    ')}}
{%- endmacro %}

{% macro step(txt, img_url, img_txt, width='480px') -%}
<figure markdown>
{%- if img_url -%}
[![{{img_txt}}]({{img_url}}){ width='{{width}}'' }]({{img_url}})
{%- endif -%}
<figcaption markdown>{{txt}}</figcaption>
</figure>
{%- endmacro %}

{% macro render_steps(step_list, img_width) %}
{% for current_step in step_list -%}
{{ step(current_step.txt, current_step.img, current_step.img_txt, width=img_width) }}
{% endfor %}
{% endmacro %}