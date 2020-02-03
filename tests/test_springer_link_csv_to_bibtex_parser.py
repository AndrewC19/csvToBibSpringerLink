import unittest
import springer_link_csv_to_bibtex_parser
import tempfile
import shutil
import filecmp
from os import path


class TestSplitCamelCaseJoinedNames(unittest.TestCase):

    def test_regular_joined_camel_case_names(self):
        split_name = springer_link_csv_to_bibtex_parser.split_camel_case_joined_names("JohnMarkPeter")
        self.assertEqual(split_name, ["John", "Mark", "Peter"])

    def test_lower_case_first_name_in_camel_case_joined_names(self):
        split_name = springer_link_csv_to_bibtex_parser.split_camel_case_joined_names("johnMarkPeter")
        self.assertEqual(split_name, ["john", "Mark", "Peter"])

    def test_accented_characters_in_camel_case_joined_name(self):
        split_name = springer_link_csv_to_bibtex_parser.split_camel_case_joined_names("JoãoAdriánFrançois")
        self.assertEqual(split_name, ["João", "Adrián", "François"])


class TestJoinNamesAsCamelCase(unittest.TestCase):

    def test_regular_name(self):
        camel_case_joined_name = springer_link_csv_to_bibtex_parser.join_names_as_camel_case("Sally Carter")
        self.assertEquals(camel_case_joined_name, "sallyCarter")

    def test_triple_name(self):
        camel_case_joined_name = springer_link_csv_to_bibtex_parser.join_names_as_camel_case("John James Peter")
        self.assertEquals(camel_case_joined_name, "johnJamesPeter")

    def test_accented_characters_in_names(self):
        camel_case_joined_name = springer_link_csv_to_bibtex_parser.join_names_as_camel_case("Zoë Noël")
        self.assertEquals(camel_case_joined_name, "zoëNoël")


class TestConvertCsvToBibtex(unittest.TestCase):
    def setUp(self):
        self.test_directory = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_directory)

    def test_single_csv_to_bibtex_entry(self):
        test_single_bibtex_entry = path.join(self.test_directory, "test_single_bibtex_entry.bib")
        expected_single_bibtex_entry = "gold_standard_bibtex_files/single_bibtex_entry.bib"
        parser = springer_link_csv_to_bibtex_parser.CsvToBibtexParser("test_csv_files/single_csv_entry.csv",
                                                                      test_single_bibtex_entry)
        parser.convert_csv_to_bibtex()
        self.assertTrue(filecmp.cmp(test_single_bibtex_entry, expected_single_bibtex_entry), "Files do not match")

    def test_multiple_csv_to_bibtex_entry(self):
        test_multiple_bibtex_entries = path.join(self.test_directory, "test_multiple_bibtex_entries.bib")
        expected_multiple_bibtex_entries = "gold_standard_bibtex_files/multiple_bibtex_entries.bib"
        parser = springer_link_csv_to_bibtex_parser.CsvToBibtexParser("test_csv_files/multiple_csv_entries.csv",
                                                                      test_multiple_bibtex_entries)
        parser.convert_csv_to_bibtex()
        self.assertTrue(filecmp.cmp(test_multiple_bibtex_entries, expected_multiple_bibtex_entries),
                        "Files do not match")

if __name__ == '__main__':
    unittest.main()
