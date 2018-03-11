class RSTDocument(object):
    def __init__(self, title=None):
        self.title = title
        self.sections = []

    def render(self) -> str:
        content = self._render_title() + \
                  [section.render() for section in self.sections]
        return "\n".join(content)

    def _render_title(self):
        if self.title is not None:
            return [
                self.title + "\n",
                "=" * len(self.title),
                "\n"
            ]
        else:
            return []

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.render())

    def add_section(self, section):
        self.sections.append(section)


class RSTTableSection(object):
    def __init__(self, table_name, metadata):
        self.table_name = table_name
        self.metadata = metadata

    def render(self) -> str:
        return self._render_header() + self._render_body()

    def _render_header(self)-> str:
        return """{title}
==============

.. csv-table::
   :header: "Column name", "Null values", "Comment"
   :widths: 15, 10, 30""".format(title=self.table_name)

    def _render_body(self):
        return """
   "id", false,
   "name", true, "The first name of the staffer"
   "email", false, "full email address"
"""


def main():
    doc = RSTDocument()
    doc.add_section(RSTTableSection("First Table"))
    doc.save("./docs/source/tables.rst")


if __name__ == "__main__":
    main()
