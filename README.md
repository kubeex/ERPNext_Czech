# Czech Localization

Vlastní Frappe aplikace obsahující veškerou českou lokalizaci a firemní
úpravy nad ERPNext / HRMS:

- `czech_localization/translations/cs.csv` — český překlad (poslední
  překladová vrstva, instaluje se až po ERPNext a HRMS)
- `TERMINOLOGY.md` — závazný anglicko-český terminologický slovník
- vlastní custom fields, workflows a reporty (přibývají postupně)

## Princip

- `frappe`, `erpnext` a `hrms` se nikdy needitují přímo.
- Veškerá firemní/česká logika žije zde a je verzovaná v Gitu.
- Instalační pořadí na site: `erpnext` → `hrms` → `czech_localization`.

## Instalace (bench)

```bash
bench get-app czech_localization <git-url>
bench --site <site-name> install-app czech_localization
```

## License

MIT
