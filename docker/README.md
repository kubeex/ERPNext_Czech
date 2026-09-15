# Docker build podklady

Tento adresář neobsahuje kopii `frappe_docker` (ten se klonuje zvlášť na
cílovém serveru, viz `../DEPLOYMENT.md`) — jen soubory specifické pro
naši instalaci:

- `apps.json` — seznam custom aplikací pro `images/layered` build
  (erpnext → hrms → czech_localization; samotný `frappe` framework se
  nezadává v `apps.json`, ale přes build argumenty `FRAPPE_PATH` /
  `FRAPPE_BRANCH`, viz níže). Před buildem nahraď `<ORGANIZACE>`
  skutečnou GitHub organizací/uživatelem, kam pushneš `czech_localization`.
- `.env.example` — proměnné prostředí pro `docker compose`.

Ověřeno proti `frappe/frappe_docker` (branch `main`,
`docs/02-setup/02-build-setup.md` a `docs/03-production/01-tls-ssl-setup.md`,
staženo 2026-09-15). Před produkčním nasazením doporučeno znovu
zkontrolovat, že se postup od té doby nezměnil.

## Build vlastního image (`images/layered`)

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
cp /cesta/k/czech_localization/docker/apps.json apps.json

docker build \
  --no-cache \
  --build-arg=FRAPPE_PATH=https://github.com/frappe/frappe \
  --build-arg=FRAPPE_BRANCH=version-16 \
  --secret=id=apps_json,src=apps.json \
  --tag=erpnext-cz:16 \
  --file=images/layered/Containerfile .
```

`apps.json` se do buildu předává jako BuildKit secret (`--secret`), ne
jako `--build-arg` — díky tomu se případné přístupové tokeny k
privátním repozitářům nezapíšou do vrstev image. Vyžaduje Docker Engine
23.0+ (BuildKit je od té verze výchozí builder).

## Spuštění stacku

```bash
cp /cesta/k/czech_localization/docker/.env.example .env
nano .env   # doplnit DB_PASSWORD, LETSENCRYPT_EMAIL, SITES_RULE

docker compose --env-file .env \
  -f compose.yaml \
  -f overrides/compose.mariadb.yaml \
  -f overrides/compose.redis.yaml \
  -f overrides/compose.https.yaml \
  config > compose.erpnext-cz.yaml

docker compose --project-name erpnext-cz -f compose.erpnext-cz.yaml up -d
```

`overrides/compose.https.yaml` spouští Traefik přímo v tomto stacku a
řeší Let's Encrypt HTTPS podle `SITES_RULE` (Traefik v3 rule
expression, např. `` Host(`erp.firma.cz`) ``) — plný přehled je v
`frappe_docker/docs/03-production/01-tls-ssl-setup.md`.

## Vytvoření site

```bash
docker compose --project-name erpnext-cz exec backend \
  bench new-site \
  --mariadb-user-host-login-scope=% \
  --db-root-password <DB_PASSWORD z .env> \
  --admin-password <silné heslo pro Administrator> \
  --install-app erpnext \
  --install-app hrms \
  --install-app czech_localization \
  erp.firma.cz
```

Pořadí `--install-app` je důležité — `czech_localization` musí jít
poslední, aby jeho `translations/cs.csv` fungoval jako poslední
(nejsilnější) překladová vrstva nad ERPNext a HRMS.
