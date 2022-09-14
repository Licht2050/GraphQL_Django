# GraphQL_Bib_Django

Dieses Projekt demonstriert die Verwendung von Graphene mit Django. Das Projekt verwendet Postgres für die persistente Datenspeicherung. Um das Projekt möglichst effizient und plattformunabhängig zu nutzen, kam doker-compose zum Einsatz. Eine Beispielbibliothek wird hier gezeigt.

## Starten des Projekts:

```text
docker-compose up
```

Zum Starten des Projekts müssen Docker und Docker-Compose installiert sein. Mann muss sich auch im bibliothek-Verzeichnis befinden.

Graphiql wird hier als GraphQL-Client verwendet. Es kann direkt im Browser wie folgt aufrufen werden: `http://127.0.0.1:8000/graphql`

## Änderungen vornehmen

In Django können Moduländerungen (wie das Hinzufügen eines neuen Felds oder das Entfernen eines Moduls) mit dem Befehl `migrations` angewendet werden.

In diesem Projekt erfolgt das Festschreiben von Änderungen in einem separaten Terminal, nachdem [das Projekt gestartet wurde](#starten-des-projekts). Geben Sie nach dem Öffnen eines Terminals den Befehl `docker exec -it bibliothek-web-1 bash` ein, um in dem Django-Container zu wechseln. Änderungen können jetzt mit den Befehlen `python manage.py migrations` und `python manage.py migrate` festgeschrieben werden.


Quellen:
- Dajngo mit GraphQL: `https://www.fullstacklabs.co/blog/django-graphene-rest-graphql`

- Unittest und Pytest: `https://docs.graphene-python.org/projects/django/en/latest/testing/`