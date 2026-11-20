from urllib import response

import data
import sender_stand_request

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()('token')
    return token

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert response.status_code == 201
    assert kit_body['name'] == response.json().get('name')

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert response.status_code == 400

def test3_nombre_vacio():
    current_kit_body = get_kit_body("")
    negative_assert(current_kit_body)

def test1_nombre_1_letra():
    current_kit_body = get_kit_body("e")
    positive_assert(current_kit_body)

def test5_caracteres_especiales():
    current_kit_body = get_kit_body("!""#$%&/()=?¡¿'´´{+{@;:-_{[+*}]")
    positive_assert(current_kit_body)

def test6_Se_permiten_espacios():
    current_kit_body = get_kit_body(" ")
    positive_assert(current_kit_body)

def test7_Se_permiten_numeros():
    current_kit_body = get_kit_body("0123456789")
    positive_assert(current_kit_body)

def test8_parametro_no_pasa_solicitud():
    current_kit_body = get_kit_body(None)
    negative_assert(current_kit_body)

def test9_Se_ha_pasado_un_parametro_diferentes():
    current_kit_body = get_kit_body(1234567890)
    negative_assert(current_kit_body)

def test2_numero_caracteres_permitido_511():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(current_kit_body)

def test2_numero_caracteres_mayor_al_permitido_512():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCd")
    negative_assert(current_kit_body)
