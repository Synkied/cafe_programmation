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
                sep=";",
                encoding="ISO-8859-1",
            )
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3A'], 1)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['3B'], 2)
            csv_file_df['dimension'] = csv_file_df['dimension'].replace(['4C'], 3)

            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4A'], 1)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4B'], 2)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4C'], 3)
            csv_file_df['avancement'] = csv_file_df['avancement'].replace(['4D'], 4)

            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1A'], 2)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1B'], 1)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1C'], 3)
            csv_file_df['fonction'] = csv_file_df['fonction'].replace(['1D'], 4)

            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2B'], 4)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2A'], 3)
            csv_file_df['contexte'] = csv_file_df['contexte'].replace(['2C'], 1)

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


# "CRITERE 1 : Fonction
#    1A : musée, patrimoine…
#    1B : bibliothèque, numérique…
#    1C : théâtre, spectacle…
#    1D : fabrique, hybride…"
#    "CRITERE 2 : Contexte
#    2A : construction nouvelle
#    2B : monument historique
#    2C : batiment non patrimonial"
#    "CRITERE 3 : Dimension
#    3A : moins de 3 000 m²
#    3B : entre 3 000 et 10 000 m²
#    3C : plus de 10 000 m²"
#    "CRITERE 4 : Avancement
#    4A : à l'étude
#    4B : en réalisation
#    4C : réalisé
#    4D : en attente ou abandonné"
