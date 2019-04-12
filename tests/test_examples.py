from glob import glob
from os.path import dirname, join

from django.template import Context, Template

example_dir = join(dirname(__file__), "examples")
example_input_fnames = glob(join(example_dir, "*.md"))
example_inputs = (join(example_dir, fname) for fname in example_input_fnames)
examples = (
    (example, example.replace(".md", ".output")) for example in example_input_fnames
)


class TestExamples(object):
    def test_examples(self):
        for in_file, out_file in examples:
            with open(in_file) as f:
                template = "{% load whiteless %}" + f.read()
            with open(out_file) as f:
                expected = f.read()
            output = Template(template).render(Context())
            assert output == expected, in_file
