from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Pasaporte, Pais, Continente
from django.shortcuts import render
from django.db import connection


def id_pasaporte(request, id_pasaporte):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM pasaportes WHERE id_pasaporte = %s",
            [id_pasaporte]
        )
        row = cursor.fetchone()

    if row:
        data = {
            'numero_pasaporte': row[1],
            'nombre': row[2],
            'apellidos': row[3],
            'fecha_nacimiento': row[4],
            'sexo': row[5],
            'fecha_emision': row[6],
            'pais': Pais.objects.get(id=row[7]).nombre
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Pasaporte no encontrado'}, status=404)

def id_pais(request, id_pais):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM pasaportes WHERE pais_id = %s",
            [id_pais]
        )
        rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            'numero_pasaporte': row[1],
            'nombre': row[2],
            'apellidos': row[3],
            'fecha_nacimiento': row[4],
            'sexo': row[5],
            'fecha_emision': row[6],
            'pais': Pais.objects.get(id=row[7]).nombre
        })

    return JsonResponse(data, safe=False)

def id_continente(request, id_continente):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM pasaportes WHERE pais_id IN "
            "(SELECT id FROM paises WHERE continente_id = %s)",
            [id_continente]
        )
        rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            'numero_pasaporte': row[1],
            'nombre': row[2],
            'apellidos': row[3],
            'fecha_nacimiento': row[4],
            'sexo': row[5],
            'fecha_emision': row[6],
            'pais': Pais.objects.get(id=row[7]).nombre
        })

    return JsonResponse(data, safe=False)
