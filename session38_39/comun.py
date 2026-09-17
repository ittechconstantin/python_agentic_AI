# =============================================================
# COMUN  -  un singur loc care vorbeste cu API-ul (Bounty Board)
# =============================================================
# Cele 3 pagini folosesc toate api() de mai jos, in loc sa repete fiecare
# propriul requests.get(...) cu propria gestiune de erori. `requests`
# il stii de la s32 - nou e doar organizarea intr-un fisier separat.
# =============================================================

import requests

API_URL = "http://127.0.0.1:8000"

def api(metoda: str, cale: str, **kwargs):
    """Intoarce mereu (ok, date_sau_mesaj). ok=False -> mesajul e un
    string gata de pus direct intr-un st.error(...)."""
    try:
        r = requests.request(metoda, f"{API_URL}{cale}", timeout=5, **kwargs)
    except requests.exceptions.ConnectionError:
        return False, "Nu pot contacta API-ul. Ai pornit `python3 s38_app.py` intr-un alt terminal?"
    except requests.exceptions.Timeout:
        return False, "API-ul a raspuns prea greu (timeout)."

    if r.status_code >= 400:
        try:
            detaliu = r.json().get("detail", r.text)
        except ValueError:
            return False, r.text

        if isinstance(detaliu, list):
            # 422 de la Pydantic: lista de erori, una per camp. Scoatem
            # "body"/"query"/"path" din loc - vrem "titlu: ...", nu "body.titlu: ...".
            mesaje = []
            for e in detaliu:
                camp = ".".join(str(p) for p in e["loc"] if p not in ("body", "query", "path"))
                mesaje.append(f"{camp}: {e['msg']}")
            return False, "; ".join(mesaje)
        return False, str(detaliu)

    return True, (r.json() if r.content else None)
