import pandas as pd


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
                self.title,
                "=" * len(self.title)
            ]
        else:
            return []

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.render())

    def add_section(self, section):
        self.sections.append(section)


class RSTTableSection(object):
    def __init__(self, table_name, data, header=None):
        self.table_name = table_name
        self.header = header or [str(c) for c in data.columns]
        self.data = data

    def render(self) -> str:
        return self._render_title() + \
               self._render_header() + \
               self._render_body()

    def _render_title(self):
        title = self.table_name
        formatting = "=" * len(title)
        return title + "\n" + formatting + "\n\n"

    def _render_header(self) -> str:
        header_names = ", ".join(self.header)
        header = [".. csv-table::",
                  "   :header: {}".format(header_names),
                  "   :widths: 15, 10, 30",
                  ""]
        return "\n".join(header)

    def _render_body(self):
        body = [self._render_row(row) for _, row in self.data.iterrows()]
        if len(body) > 0:
            body = [""] + body + [""]
        return "\n".join(body)

    def _render_row(self, row):
        return "   " + ",".join(str(col) for col in row)


def main():
    doc = RSTDocument()
    header = ["Column name", "Nullable", "Comment"]
    data = pd.DataFrame([
        ["id", False, ""],
        ["name", True, ""],
        ["email", False, "staffer's email address"],
        ["age", False, "sometime we know their age"]
    ])
    doc.add_section(RSTTableSection("First Table", data, header))
    doc.save("./docs/source/tables.rst")


if __name__ == "__main__":
    main()
