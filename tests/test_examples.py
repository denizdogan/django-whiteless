from pathlib import Path

from django.template import Context, Template

example_inputs = (Path(".") / "examples").glob("*.md")
examples = ((p, p.with_suffix(".output")) for p in example_inputs)


class TestExamples(object):
    def test_examples(self):
        for in_file, out_file in examples:
            template = '{% load whiteless %}' + in_file.read_text()
            expected = out_file.read_text()
            output = Template(template).render(Context())
            assert output == expected, in_file
