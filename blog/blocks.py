from wagtail.core import blocks

CODE_CHOICES = [
    ('python', 'python'),
    ('javascript', 'javascript'),
    ('css', 'css'),
    ('markup', 'markup'),
    ('html', 'html'),
    ('go', 'go'),
    ('bash', 'bash'),
]


class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(choices=CODE_CHOICES, default="bash")
    text = blocks.TextBlock()

    class Meta:
        template = "blog/code_block.html"
        icon = "openquote"
        label = "Code Block"
    
