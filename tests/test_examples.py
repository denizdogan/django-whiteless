from pathlib import Path

import pytest
from django.template import Context, Template

example_dir = Path(__file__).parent / "examples"


class TestExamples:
    @pytest.mark.parametrize(
        "in_file", sorted(example_dir.glob("*.md")), ids=lambda path: path.stem
    )
    def test_examples(self, in_file):
        template = "{% load whiteless %}" + in_file.read_text(encoding="utf-8")
        expected = in_file.with_suffix(".output").read_text(encoding="utf-8")
        output = Template(template).render(Context({"xs": [1, 2, 3]}))
        assert output == expected
