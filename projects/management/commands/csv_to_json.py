import os, getopt, sys
import pandas as pd
import json

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-i', help='Absolute path to CSV input file.')

    def handle(self, *args, **options):
        input_file = options['i']
        if os.path.isfile(input_file):
            print('file found', input_file)

            csv_file_df = pd.read_csv(
                input_file,
                sep=",",
                encoding="ISO-8859-1",
            )
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['1-XS', '2-S'], 1)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3-M'], 2)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['4-L', '5-XL'], 3)

            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['1-ETU'], 1)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['2-2-CONS', '3-REAL'], 2)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4-FAIT'], 3)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['5-ATT'], 4)

            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1-MUSEO'], 2)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['2-BIBLIO'], 1)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['3-SPECT'], 3)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['4-FABR'], 4)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['5-MONUM'], 2)

            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['1-MONUM'], 1)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2-REHAB'], 3)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['3-NEUF'], 2)

            json_file = csv_file_df.to_json(orient="records")
            fixture_list = []
            counter = 1

            for project in json.loads(json_file):
                json_fixture = {}
                json_fixture['fields'] = project
                json_fixture['model'] = 'projects.project'
                json_fixture['pk'] = counter
                fixture_list.append(json_fixture)
                counter += 1

            with open('C:\\Users\\PC\\Desktop\\projets_clients\\cafe_programmation\\projects\\fixtures\\test.json', 'w') as f:
                json.dump(fixture_list, f)
