"""A template escapes what a visitor typed, unless the template or the code says it is safe."""
from _setup import report, setup
version = setup()
from django.template import Context, Template
from django.utils.html import format_html

name = '<script>alert(1)</script>'
plain = Template("Hello {{ name }}").render(Context({"name": name}))
marked = Template("Hello {{ name|safe }}").render(Context({"name": name}))
built = format_html("<b>{}</b>", name)
report("<script>" not in plain and "<script>" in marked and "<script>" not in built and built.startswith("<b>"),
       f"Django {version}: a pet named {name} came out of {{{{ name }}}} as {plain[6:]}; out of {{{{ name|safe }}}} as {marked[6:]}; out of format_html('<b>{{}}</b>', name) as {built}")
