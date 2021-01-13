import operator


def siglas_x_categoria(dic_triage, lista_aux):

    categoria = {}
    for sigla in lista_aux:
        for atencion in dic_triage:

            if sigla in dic_triage[atencion]:

                if atencion not in categoria:
                    categoria[atencion] = 1
                else:
                    categoria[atencion] += 1
    return categoria


def prioridades_enfermedades(lista2, citas, siglas2):
    aux = {}
    for li in lista2:
        for clave, valor in citas.items():
            for csi, vsi in siglas2.items():
                for i in range(len(valor)):

                    if (li == valor[i]) and (valor[i] == csi):

                        aux[vsi] = clave

    ordenado = dict(sorted(aux.items(), key=operator.itemgetter(1)))

    print("Orden de prioridad de las enfermedades es: ")
    for ca, va in ordenado.items():
        print(ca)


siglas = {
   'LMA': 'Leucemia Mieloide Aguda',
   'IAM': 'Infarto Agudo al Miocardio',
   'C19': 'Coronavirus',
   'HCA': 'Hepatitis Cronica Activa',
   'FQ': 'Fibrosis Quistica',
   'ECV': 'Enfermedad Cerebro Vascular',
   'DBT': 'Diabetes',
   'IRA': 'Insuficiencia Renal Aguda',
   'TBC': 'Tuberculosis',
   'TQC': 'Taquicardia',
   'UG': 'Ulcera Gastrica',
   'EM': 'Esclerosis Multiple',
   'M': 'Meningitis',
   'OMA': 'Otitis Media Aguda',
   'PNF': 'Pielonefritis',
   'EA': 'Alzheimer',
   'NIH': 'Neumonia Intra-Hospitalaria',
   'IHO': 'Infeccion Herida Operatoria',
   'HPT': 'Hipertension Pulmonar',
   'EP': 'Embolismo Pulmonar',
   'CBP': 'Cirrosis Biliar Primaria',
   'ARJ': 'Artritis Reumatoidea Juvenil',
   'SLT': 'Sindrome de Lisis Tumoral',
   'VZV': 'Virus Varicela Zoster',
   'TVP': 'Trombosis Venosa Profunda',
   'EI': 'Endocarditis Infecciosa',
   'AE': 'Arterioesclerosis',
   'HEL': 'Hemorragia Exterior Leve',
   'RF': 'Resfriado Comun',
   'E1': 'Esquince Nivel 1',
   'D': 'Depresion',
   'ART': 'Artrosis',
   'MG': 'Migrania',
   'HL': 'Herpes Labial',
   'LG': 'Laringitis',
   'FG': 'Faringitis',
   'GMN': 'Glomerulonefritis'
}

triage = {
    'C1': ['GMN', 'IAM', 'PNF', 'TVP', 'ECV', 'EP', 'C19'],
    'C2': ['LMA', 'TBC', 'NIH', 'IHO', 'HPT', 'FQ', 'SLT', 'IRA', 'M'],
    'C3': ['HCA', 'UG', 'EM', 'TQC'],
    'C4': ['DBT', 'CBP', 'VZV', 'ART', 'OMA'],
    'C5': ['EA', 'ARJ', 'HEL', 'RF', 'E1', 'D', 'MG', 'HL', 'LG', 'FG', 'EI']
}


lista = ['ARJ', 'OMA', 'GMN', 'RF', 'HCA', 'C19', 'EI', 'D', 'IRA']
print(siglas_x_categoria(triage, lista), "\n")

lista1 = ['D', 'M', 'IAM', 'TBC', 'MG', 'ART', 'C19']

prioridades_enfermedades(lista1, triage, siglas)
