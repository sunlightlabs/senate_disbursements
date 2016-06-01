import csv
import re

FUNDING_YEAR_RE = re.compile(r'(Funding Year) (\d+)')
FISCAL_YEAR_RE = re.compile(r'(FY) (\d+)')
CONGRESS_NUMBER = re.compile(r'\((\d+)TH\)')


def format_csv(source_doc, csv_file='senate_data.csv', cleaned_file='senate_data_cleaned.csv'):
    unclean_data_reader = csv.reader(open(csv_file, 'r'))
    cleaned_data_writer = csv.writer(open(cleaned_file, 'wb'))
    cleaned_data_writer.writerow(["This data was parsed on an experimental basis by the Sunlight Foundation from Senate disbursement reports. Please cite 'The Sunlight Foundation' in any usage.  For more information see the readme at http://assets-reporting.s3.amazonaws.com/1.0/senate_disbursements/readme.txt."])
    cleaned_data_writer.writerow(['source_doc','senator_flag','senator_name', 'raw office',	'funding_year', 'fiscal_year', 'congress_number', 'reference_page', 'document_number',	'date_posted', 'start_date', 'end_date', 'description',	'salary_flag', 'amount', 'payee'])
    for line in unclean_data_reader:
        senator_flag = 1 if 'senator' in line[0].lower() else 0
        senator_name = line[0].split('Funding')[0].replace('SENATOR','').strip() if senator_flag else ''
        raw_office = line[0]

        try:
            funding_year = int(re.search(FUNDING_YEAR_RE, line[0]).group(2))
        except:
            funding_year = ''

        try:
            fiscal_year = int(re.search(FISCAL_YEAR_RE, line[0]).group(2))
        except:
            fiscal_year = ''

        try:
            congress_number = int(re.search(CONGRESS_NUMBER, line[0]).group(1))
        except:
            congress_number = ''

        reference_page = line[3]
        document_number = line[4]
        date_posted = line[5]
        payee = line[6]
        start_date = line[7]
        end_date = line[8]
        description = line[9]
        amount = line[10]

        salary_flag = 0 if start_date == '' and end_date == '' else 1

        cleaned_data_writer.writerow([source_doc, senator_flag, senator_name, raw_office, funding_year,
                                      fiscal_year, congress_number, reference_page, document_number, date_posted,
                                      start_date, end_date, description, salary_flag, amount, payee])