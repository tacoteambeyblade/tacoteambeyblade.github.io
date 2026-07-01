import requests
import os
from requests.exceptions import HTTPError, RequestException

API_KEY = os.environ["API_KEY"]
COMMUNITY_ID = "PlazaCoacalco"
TIMEOUT = 10
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/vnd.api+json',
    'Authorization': API_KEY,
    'Authorization-Type': 'v1',
    'If-None-Match': ''
}

def main() -> None:

    tournament_type = input("¿De qué torneo quieres obtener información?\n1) Taco League\n2) Taco Fun\n> ")
    if input(f"Tu torneo fue hecho en la comunidad de '{COMMUNITY_ID}' (s/n)?\n> ") == "s":
        community_id = COMMUNITY_ID
    else:
        community_id = input("Ingresa el COMMUNITY_ID:\n> ")
    print(f"Tu COMMUNITY_ID es = '{community_id}'")
    tournament_id = input("Ingresa tu TOURNAMENT_ID:\n> ")

    url = f"https://api.challonge.com/v2.1/tournaments/{tournament_id}/matches.json?community_id={community_id}"
    print(f"La petición GET se hará a\n'{url}'")

    payload = {}
    response = requests.request("GET", url, headers=HEADERS, data=payload)
    print(response.json())

    '''
    try:
        response = requests.get(url=url, headers=HEADERS, timeout=TIMEOUT)
        #response.raise_for_status()
        print(response.json())
    except HTTPError as err:
        print(f"ERROR HTTP: {err}")
        raise
    except RequestException as err:
        print(f"Error de conexion: {err}")
        raise
    '''

if __name__ == "__main__":
    main()