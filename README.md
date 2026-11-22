# francescobrusco.github.io

Sito personale di Francesco Brusco: https://francescobrusco.github.io/ (inglese: `/en/`).

## Pagine

| Percorso | Contenuto |
|---|---|
| `/` · `/en/` | Home: presentazione, ricerca, ultimo libro, attività |
| `/pubblicazioni/` · `/en/publications/` | Monografie (con copertine e link a laFeltrinelli), tesi di dottorato, articoli |
| `/libri/` · `/en/books/` | Rimandi automatici alle pagine delle pubblicazioni |
| `/produzione_discografica_italiana_1965_1999/` | Progetto di ricerca (repository separato) |

## Come modificare

Testi, libri, articoli e link sono in `strumenti/genera.py`; la grafica in `assets/style.css`. Dopo una modifica rigenera le pagine:

```
python strumenti/genera.py
```

Le copertine dei libri sono in `img/libri/`, con l'ISBN-13 come nome del file.
