import unittest
import springer_link_csv_to_bibtex_parser


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


if __name__ == '__main__':
    unittest.main()
