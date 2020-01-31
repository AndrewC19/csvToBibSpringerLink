import springer_link_csv_to_bibtex_parser
import argparse

parser = argparse.ArgumentParser(description='Convert a SpringerLink auto-generated CSV references file to Bibtex')
parser.add_argument('-i','--input', help='Provide the path to your input csv file', required=True)
parser.add_argument('-o','--output', help='Provide the path to your output folder', required=True)
args = vars(parser.parse_args())

csv_to_bibtex_parser = springer_link_csv_to_bibtex_parser.CsvToBibtexParser(args['input'], args['output'])
csv_to_bibtex_parser.convert_csv_to_bibtex()