import pandas as pd
import numpy as np

from generate_docs import RSTDocument, RSTTableSection


class TestRSTDocument:
    def test_document_with_empty_title_renders_to_empty_string(self):
        # Given
        doc = RSTDocument(title=None)

        # When
        content = doc.render()

        # Then
        assert content == ""

    def test_document_with_title_renders_to_rst_title(self):
        # Given
        doc = RSTDocument(title="Title")

        # When
        content = doc.render()

        # Then
        assert content == "Title\n====="


class TestRSTTableSection:
    def test_section_renders_with_title(self):
        # Given
        data = pd.DataFrame()
        section = RSTTableSection(table_name="Test", data=data)

        # When
        content = section.render()

        # Then
        title, format = content.split("\n")[:2]
        assert title == "Test"
        assert format == "===="

    def test_section_renders_csv_table_header(self):
        # Given
        data = pd.DataFrame()
        header = ["Column name", "Nullable", "Comment"]
        section = RSTTableSection(table_name="Test", header=header, data=data)

        # When
        content = section.render()

        # Then
        header, columns, widths = content.split("\n")[3:6]
        assert header == ".. csv-table::"
        assert columns == "   :header: Column name, Nullable, Comment"
        assert widths == "   :widths: 20, 20, 20"

    def test_section_with_empty_data_renders_metadata_only(self):
        # Given
        data = pd.DataFrame()
        section = RSTTableSection(table_name="Test", data=data)

        # When
        content = section.render()

        # Then
        assert 7 == len(content.split("\n"))

    def test_section_with_data_renders_content(self):
        # Given
        data = pd.DataFrame([
            ["id", False, ""],
            ["name", True, ""],
            ["email", False, "staffer's email address"]
        ])
        section = RSTTableSection(table_name="Test", data=data)

        # When
        content = section.render()

        # Then
        rows = content.split("\n")[-4:-1]
        assert rows[0] == '   "id","False",""'
        assert rows[1] == '   "name","True",""'
        assert rows[2] == '   "email","False","staffer\'s email address"'

    def test_section_with_more_data_renders_content(self):
        # Given
        data = pd.DataFrame([
            ["id", False, np.nan],
            ["name", True, ""],
            ["email", False, "staffer's email address"],
            ["age", False, "sometime we know their age"]
        ])
        print(data)
        section = RSTTableSection(table_name="Test", data=data)

        # When
        content = section.render()

        # Then
        rows = content.split("\n")[-5:-1]
        print(rows)
        assert rows[0] == '   "id","False",'
        assert rows[1] == '   "name","True",""'
        assert rows[2] == '   "email","False","staffer\'s email address"'
        assert rows[3] == '   "age","False","sometime we know their age"'
