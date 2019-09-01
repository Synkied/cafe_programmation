import json
import os
import pandas as pd

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
                encoding="UTF-8",
            )
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3A'], 1)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3B'], 2)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3C'], 3)

            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4A'], 1)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4B'], 2)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4C'], 3)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4D'], 4)

            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1A'], 2)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1B'], 1)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1C'], 3)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1D'], 4)

            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2B'], 4)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2C'], 1)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2A'], 3)

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
