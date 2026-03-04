# ❌ N+1 — hits DB for every article's author
for article in Article.objects.all():
    print(article.author.name)  # 1 extra query per article!

# ✅ — 1 JOIN query
for article in Article.objects.select_related("author"):
    print(article.author.name)
```

---

## 6. Complete Summary Map
```
django.db.models.Model
│
├── DEFINE YOUR DATA
│   ├── Field types        (CharField, IntegerField, DateTimeField...)
│   └── class Meta         (ordering, db_table, indexes, constraints)
│
├── INSTANCE METHODS
│   ├── save()             → INSERT or UPDATE
│   ├── delete()           → DELETE
│   ├── full_clean()       → validate all fields
│   ├── clean()            → your custom validation
│   ├── refresh_from_db()  → re-sync from database
│   ├── __str__()          → human readable string
│   └── get_absolute_url() → canonical URL
│
└── QUERY API (via objects Manager)
    ├── .all()             → SELECT *
    ├── .filter()          → SELECT WHERE
    ├── .get()             → SELECT WHERE (single row)
    ├── .create()          → INSERT + return instance
    ├── .update()          → bulk UPDATE
    ├── .delete()          → bulk DELETE
    └── .select_related()  → JOIN (FK)