from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from zipfile import ZipFile
from xml.etree import cElementTree as ElementTree

from searchfield.quickstart.xml import XmlDictConfig


@api_view(["POST"])
def fields(request, *args, **kwargs):
    cv = request.data['file']
    with ZipFile(cv, 'r') as zipObj:
        zipObj.extractall()

    # print(zipObj.filelist[0].filename)
    tree = ElementTree.parse(zipObj.filelist[0].filename)
    root = tree.getroot()
    xmldict = XmlDictConfig(root)

    researcher = {
        'fullname': xmldict['DADOS-GERAIS']['NOME-COMPLETO'],
        'citation_name': xmldict['DADOS-GERAIS']['NOME-EM-CITACOES-BIBLIOGRAFICAS'],
        'summary': xmldict['DADOS-GERAIS']['RESUMO-CV']['TEXTO-RESUMO-CV-RH'],
        'institution': xmldict['DADOS-GERAIS']['ENDERECO']['ENDERECO-PROFISSIONAL']['NOME-INSTITUICAO-EMPRESA'],
        'department': xmldict['DADOS-GERAIS']['ENDERECO']['ENDERECO-PROFISSIONAL']['NOME-ORGAO'],
        'unity': xmldict['DADOS-GERAIS']['ENDERECO']['ENDERECO-PROFISSIONAL']['NOME-UNIDADE'],
        'graduation': xmldict['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['GRADUACAO']['NOME-CURSO']
    }

    return Response(
        {
            'predictions': [
                ['Machine Learning', 0.54389],
                ['Recommendation Systems', 0.14389],
                ['Network Systems', 0.24389],
                ['Robotics', 0.34389],
                ['Discrete Mathematics', 0.44389],
                ['Computational Geometry', 0.64389],
                ['Graphs Theory', 0.74389],
            ],
            'researcher': researcher
        }

    )
