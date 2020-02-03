import pandas as pd
import re
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase


def split_camel_case_joined_names(joined_camel_case_names):
    individual_camel_case_names = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)',
                                              joined_camel_case_names)
    return [name.group(0) for name in individual_camel_case_names]


def join_names_as_camel_case(name):
    names_list = re.split('([^a-zA-Z\u00C0-\u024F\u1E00-\u1EFF])', name)
    first_name_lower_case = names_list[0].lower()
    other_names_camel_case = [name.capitalize() for name in names_list[1:] if name.isalnum()]
    camel_case_list = [first_name_lower_case] + other_names_camel_case
    camel_case = ''.join(camel_case_list)
    return camel_case


class CsvToBibtexParser:
    """ Given a CSV file path to a SpringerLink auto-generated references CSV and an output_file_path, provide the
     functionality to parse the CSV into an equivalent bibtex (.bib) format """

    def __init__(self, csv_file_path, output_file_path):
        self.csv = pd.read_csv(csv_file_path)
        self.output_path = output_file_path

    def convert_csv_to_bibtex(self):
        csv_dict = self.csv.to_dict('records')
        writer = BibTexWriter()
        with open(self.output_path, 'w', encoding="utf-8") as bibtex_file:
            for csv_entry in csv_dict:
                bibtex_entry = self.convert_csv_entry_to_bibtex_entry(csv_entry)
                bibtex_file.write(writer.write(bibtex_entry))

    def convert_csv_entry_to_bibtex_entry(self, document_record):
        bibtex_key = self.create_bibtex_entry_key_from_csv_entry(document_record)
        bibtex_entry = BibDatabase()
        bibtex_entry.entries = [
            {'journal': str(document_record['Publication Title']),
             'title': str(document_record['Item Title']),
             'author': self.get_authors_from_csv_entry(document_record),
             'year': str(document_record['Publication Year']),
             'doi': str(document_record['Item DOI']),
             'url': str(document_record['URL']),
             'ENTRYTYPE': str(document_record['Content Type']),
             'ID': bibtex_key}
        ]
        return bibtex_entry

    def create_bibtex_entry_key_from_csv_entry(self, csv_entry):
        document_authors = self.get_authors_from_csv_entry(csv_entry)
        first_author = document_authors[0]
        first_author_camel_case = join_names_as_camel_case(first_author)
        document_year = csv_entry['Publication Year']
        return first_author_camel_case + str(document_year)

    @staticmethod
    def get_authors_from_csv_entry(csv_entry):
        document_authors = str(csv_entry['Authors'])
        document_authors_list = split_camel_case_joined_names(document_authors)
        document_authors_list_without_quotes_or_braces = str(document_authors_list).replace("'", "")[1:-1]
        return document_authors_list_without_quotes_or_braces
