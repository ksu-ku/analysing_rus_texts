import os
import requests
import csv
from ruts import DiversityStats

texts = []
for filename in os.listdir("тексты/01a3be1f-bb56-49f8-bdd6-d2f312c162e7"):
    with open(os.path.join("тексты/01a3be1f-bb56-49f8-bdd6-d2f312c162e7", filename), 'r', encoding="UTF-8") as f:
        text = f.read()

        ds = DiversityStats(text)
        d = ds.get_stats()
        ttr = d['ttr']
        rttr = d['rttr']
        cttr = d['cttr']
        httr = d['httr']
        sttr = d['sttr']
        mttr = d['mttr']
        dttr = d['dttr']
        mattr = d['mattr']
        msttr = d['msttr']
        mtld = d['mtld']
        mamtld = d['mamtld']
        hdd = d['hdd']
        simpson_index = d['simpson_index']
        hapax_index = d['hapax_index']

        name_of_file = f.name
        response = requests.post("http://api.plainrussian.ru/api/1.0/ru/measure/", data={"text": text})
        metric = response.json()
        chars = metric['metrics']['chars']
        num_chars = str(chars)
        letters = metric['metrics']['letters']
        num_letters = str(letters)
        index_fk = metric['indexes']['index_fk']
        num_index_fk = str(index_fk)
        num_grade_fk = metric['indexes']['grade_fk']
        index_dc = metric['indexes']['index_dc']
        num_index_dc = str(index_dc)
        num_grade_dc = metric['indexes']['grade_dc']
        index_cl = metric['indexes']['index_cl']
        num_index_cl = str(index_cl)
        num_grade_cl = metric['indexes']['grade_cl']
        index_SMOG = metric['indexes']['index_SMOG']
        num_index_SMOG = str(index_SMOG)
        num_grade_SMOG = metric['indexes']['grade_SMOG']
        index_ari = metric['indexes']['index_ari']
        num_index_ari = str(index_ari)
        num_grade_ari = metric['indexes']['grade_ari']

        tmp = {'uuid': f.name, 'num_chars': num_chars, 'num_letters': num_letters,
               'num_index_fk': num_index_fk, 'num_grade_fk': num_grade_fk,
               'num_index_dc': num_index_dc, 'num_grade_dc': num_grade_dc,
               'num_index_cl': num_index_cl, 'num_grade_cl': num_grade_cl,
               'num_index_SMOG': num_index_SMOG, 'num_grade_SMOG': num_grade_SMOG,
               'num_index_ari': num_index_ari, 'num_grade_ari': num_grade_ari,
               'ttr': ttr, 'rttr': rttr, 'cttr': cttr, 'httr': httr, 'sttr': sttr,
               'mttr': mttr, 'dttr': dttr, 'mattr': mattr, 'msttr': msttr, 'mtld': mtld,
               'mamtld': mamtld, 'hdd': hdd, 'simpson_index': simpson_index, 'hapax_index': hapax_index}
        texts.append(tmp)

        fieldnames = ['uuid', 'num_chars', 'num_letters', 'num_index_fk', 'num_grade_fk', 'num_index_dc',
                      'num_grade_dc', 'num_index_cl', 'num_grade_cl', 'num_index_SMOG', 'num_grade_SMOG',
                      'num_index_ari', 'num_grade_ari', 'ttr', 'rttr', 'cttr', 'httr', 'sttr', 'mttr', 'dttr',
                      'mattr', 'msttr', 'mtld', 'mamtld', 'hdd', 'simpson_index', 'hapax_index']
        csv_file = 'analyse_01a3be1f-bb56-49f8-bdd6-d2f312c162e7.csv'
        try:
            with open(csv_file, 'w', encoding='UTF-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in texts:
                    writer.writerow(data)
        except IOError:
            print('I/O error')
