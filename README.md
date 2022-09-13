# GraphQL_Bib_Django

Dieses Projekt demonstriert die Verwendung von Graphene mit Django. Das Projekt verwendet Postgres für die persistente Datenspeicherung. Um das Projekt möglichst effizient und plattformunabhängig zu nutzen, kam doker-compose zum Einsatz. Eine Beispielbibliothek wird hier gezeigt.

## Starten des Projekts:

```text
docker-compose up
```

Zum Starten des Projekts müssen Docker und Docker-Compose installiert sein. Es muss sich auch im bibliothek-Verzeichnis befinden.

Graphiql wird hier als GraphQL-Client verwendet. Es kann direkt im Browser wie folgt aufrufen werden: `http://127.0.0.1:8000/graphql`
