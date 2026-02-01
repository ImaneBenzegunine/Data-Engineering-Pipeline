{% macro my_macro_example(value) -%}
  lower({{ value }})
{%- endmacro %}
