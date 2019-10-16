import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps
from datetime import date

def calculateAge(birthDate):
    try:
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        return age
    except Exception as ex:
        return None


class Imports:

    @staticmethod
    def insert_df_people_analytics(df_people_analytics):
        for column in ['Data Nascimento', 'Matrícula', 'Nome', 'Vínculo', 'Vínculo Resumo', 'Status', 'Sexo',
                       'Empresa_CNPJ', 'Cargo', 'Tipo de Cargo', 'Tipo Saída', 'Data Admissão', 'Data Saída',
                       'E-Mail', 'CPF', 'Centro de Custo - Número']:
            if column not in df_people_analytics.columns:
                return {'status_code': 400,
                        'message': f'Missing required column on excel file: {column}'}

        final_output = []
        for idx, row in df_people_analytics.iterrows():
            age = calculateAge(row['Data Nascimento'])

            try:
                final_output.append({
                    'registry': row.get('Matrícula'),
                    'name': row.get('Nome').title(),
                    'bind': row.get('Vínculo').title(),
                    'bind_resume': row.get('Vínculo Resumo').title(),
                    'status': row.get('Status').title(),
                    'sex': row.get('Sexo').title(),
                    'company': row.get('Empresa_CNPJ').title(),
                    'role': row.get('Cargo').title(),
                    'role_type': row.get('Tipo de Cargo').title(),
                    'release_type': row.get('Tipo Saída').title(),
                    'age': age,
                    'birth_date': row.get('Data Nascimento'),
                    'admission_date': row.get('Data Admissão'),
                    'release_date': row.get('Data Saída'),
                    'email': row.get('E-Mail'),
                    'cpf': row.get('CPF'),
                    'cost_center': row.get('Centro de Custo - Número')
                })
            except Exception as ex:
                print(ex)

        try:
            mongo.db.people_analytics.drop()
            mongo.db.people_analytics.insert_many(final_output)

            return {'status_code': 200,
                    'message': 'Success'}
        except:
            return {'status_code': 503,
                    'message': "Can't insert on mongo database"}
