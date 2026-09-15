# Terminologický slovník

Závazný anglicko-český slovník pro `translations/cs.csv` a veškerý budoucí
překlad ERPNext/HRMS UI. Cíl: stejný anglický termín se vždy překládá
stejně, bez ohledu na to, kde v systému se objeví (žádné
`Customer → Klient` na jednom místě a `Customer → Zákazník` jinde).

## Pravidla

1. **Než přeložíš nový řetězec, zkontroluj tuto tabulku** — pokud obsahuje
   použité termíny, použij přesně tento překlad.
2. **Nový termín, který tabulka neobsahuje**, se po přeložení do ní
   doplní, aby se stal závazným pro příště.
3. **Placeholdery se nikdy nepřekládají ani neupravují**: `{0}`, `{1}`,
   `{name}`, `%s`, `%(value)s`, HTML tagy (`<b>`, `<a href=...>`), URL.
4. **Mechanický (slovo za slovem) překlad víceslovných frází se do
   `cs.csv` nedává** — u zkoušky na 970 názvech DocTypů takové skládání
   opakovaně dávalo gramaticky rozbitou češtinu (např. „Warehouse Type“ →
   „Sklad Typ“ místo „Typ skladu“). Frappe u nepřeložené fráze bezpečně
   zobrazí originální anglický text, což je vždy lepší než rozbitá
   čeština. Každá fráze v `cs.csv` proto musí být ověřená/psaná member
   týmu (nebo AI asistentem s kontrolou), ne generovaná skriptem.

## Slovník (aktuálně pokryté termíny)

| Anglicky | Česky |
|---|---|
| Absent | Nepřítomen |
| Accounts payable | Závazky |
| Accounts receivable | Pohledávky |
| Active | Aktivní |
| Address | Adresa |
| Administrator | Administrátor |
| All | Vše |
| Allowed to transact with | Povoleno obchodovat s |
| Amended from | Opraveno z |
| Applicable on account | Platí pro účet |
| Appraisal | Hodnocení |
| Approved | Schváleno |
| Asset | Majetek |
| Asset category | Kategorie majetku |
| Asset maintenance | Údržba majetku |
| Asset movement | Pohyb majetku |
| Asset repair | Oprava majetku |
| Assigned to | Přiřazeno |
| Attachments | Přílohy |
| Attendance | Docházka |
| Availability of slots | Dostupnost termínů |
| Bank account | Bankovní účet |
| Bank reconciliation | Bankovní odsouhlasení |
| Batch | Šarže |
| Bill of materials | Kusovník |
| Branch | Pobočka |
| Campaign | Kampaň |
| Cancel | Stornovat |
| Cancelled | Stornováno |
| Casual leave | Volno |
| Chart of accounts | Účtová osnova |
| Chart of accounts importer | Import účtové osnovy |
| City | Město |
| Closed | Uzavřeno |
| Comments | Komentáře |
| Company | Firma |
| Completed | Dokončeno |
| Contact | Kontakt |
| Contract | Smlouva |
| Cost center | Nákladové středisko |
| Created by | Vytvořil |
| Custom field | Vlastní pole |
| Custom script | Vlastní skript |
| Customer | Klient |
| Dashboard | Dashboard |
| Date of birth | Datum narození |
| Date of joining | Datum nástupu |
| Delete | Smazat |
| Delivery note | Dodací list |
| Department | Oddělení |
| Designation | Pracovní pozice |
| Disabled | Zakázáno |
| Doctype to sync | DocType k synchronizaci |
| Download | Stáhnout |
| Draft | Koncept |
| Edit | Upravit |
| Email account | E-mailový účet |
| Employee | Zaměstnanec |
| Employee advance | Záloha zaměstnanci |
| Employee checkin | Příchod / odchod |
| Employee grievance | Stížnost zaměstnance |
| Employee group | Skupina zaměstnanců |
| Employee onboarding | Nástup zaměstnance |
| Employee promotion | Povýšení zaměstnance |
| Employee separation | Ukončení pracovního poměru |
| Employee skill | Dovednost zaměstnance |
| Employee transfer | Přeložení zaměstnance |
| Employment type | Typ pracovního poměru |
| Enabled | Povoleno |
| Exchange rate | Směnný kurz |
| Expense claim | Vyúčtování výdajů |
| Expense claim type | Typ výdaje |
| Female | Žena |
| Fiscal year | Fiskální rok |
| From date | Od data |
| Full-time | Plný úvazek |
| Gate pass | Propustka |
| General ledger | Hlavní kniha |
| Global settings | Globální nastavení |
| Goal | Cíl |
| Grand total | Celková částka |
| Guest | Host |
| Half day | Půl dne |
| Half day status | Stav půldenní docházky |
| Healthcare | Zdravotnictví |
| Holiday list | Seznam svátků |
| In progress | Probíhá |
| In time | Příchod |
| Inactive | Neaktivní |
| Intern | Stážista |
| Interview | Pohovor |
| Is active | Je aktivní |
| Item | Položka |
| Item group | Skupina položek |
| Item lead time | Dodací lhůta položky |
| Item price | Cena položky |
| Item wise tax detail | Detail daně dle položky |
| Job applicant | Uchazeč o zaměstnání |
| Job card | Výrobní karta |
| Job offer | Nabídka zaměstnání |
| Job opening | Volná pozice |
| Journal entry | Účetní zápis |
| Lead | Potenciální zákazník |
| Leave allocation | Přidělení volna |
| Leave application | Žádost o volno |
| Leave balance | Zůstatek volna |
| Leave block list | Blokovaná období volna |
| Leave period | Období volna |
| Leave policy | Politika volna |
| Leave type | Typ volna |
| Letter head | Hlavičkový papír |
| Logs to clear | Logy k vymazání |
| Loyalty program | Věrnostní program |
| Maintenance schedule | Plán údržby |
| Maintenance visit | Servisní návštěva |
| Male | Muž |
| Material request | Požadavek na materiál |
| Mobile no | Mobilní telefon |
| Mode of payment | Způsob platby |
| Mode of payment account | Účet způsobu platby |
| Modified by | Upravil |
| Naming series | Číselná řada |
| Net total | Čistá částka |
| New | Nový |
| None | Žádné |
| Not started | Nezahájeno |
| Notice period | Výpovědní lhůta |
| Notification | Oznámení |
| On hold | Pozastaveno |
| On leave | Na volnu |
| Open | Otevřeno |
| Opportunity | Obchodní příležitost |
| Other | Jiné |
| Out time | Odchod |
| Overdue | Po splatnosti |
| Owner | Vlastník |
| Paid | Zaplaceno |
| Part-time | Částečný úvazek |
| Pause sla on status | Pozastavit SLA při stavu |
| Payment entry | Platba |
| Payment terms template | Šablona platebních podmínek |
| Pick list | Vychystávací seznam |
| Payroll entry | Zpracování mezd |
| Pending | Čeká na vyřízení |
| Postal code | PSČ |
| Present | Přítomen |
| Price list | Ceník |
| Pricing rule | Cenové pravidlo |
| Print | Tisk |
| Print format | Tiskový formát |
| Print settings | Nastavení tisku |
| Privilege leave | Dovolená |
| Probation | Zkušební doba |
| Process statement of accounts | Zpracování výpisu účtů |
| Process statement of accounts cc | Zpracování výpisu účtů - kopie |
| Process statement of accounts customer | Zpracování výpisu účtů - klient |
| Production plan | Výrobní plán |
| Project | Projekt |
| Purchase invoice | Přijatá faktura |
| Purchase order | Nákupní objednávka |
| Purchase receipt | Příjemka |
| Purpose of travel | Účel cesty |
| Quality inspection | Kontrola kvality |
| Quantity | Množství |
| Quotation | Nabídka |
| Rejected | Zamítnuto |
| Relieving date | Datum ukončení |
| Remarks | Poznámky |
| Reply to address | Adresa pro odpověď |
| Report | Report |
| Reports to | Nadřízený |
| Requested | Požadováno |
| Role | Role |
| Salary component | Mzdová složka |
| Salary slip | Výplatní páska |
| Salary structure | Mzdová struktura |
| Sales invoice | Vydaná faktura |
| Sales order | Prodejní objednávka |
| Save | Uložit |
| Serial no | Sériové číslo |
| Series | Řada |
| Shift assignment | Přiřazení směny |
| Shift end time | Konec směny |
| Shift request | Žádost o směnu |
| Shift start time | Začátek směny |
| Shift type | Typ směny |
| Sick leave | Nemocenská |
| Sla fulfilled on status | SLA splněno při stavu |
| Status | Stav |
| Stock entry | Skladový pohyb |
| Stock reconciliation | Skladová inventura |
| Subcontracting order | Objednávka subdodávky |
| Subcontracting receipt | Příjemka subdodávky |
| Submit | Odeslat |
| Supplier | Dodavatel |
| System manager | Správce systému |
| System settings | Nastavení systému |
| Task | Úkol |
| Tax rule | Daňové pravidlo |
| Terms and conditions | Obchodní podmínky |
| Time zone | Časové pásmo |
| Timesheet | Výkaz práce |
| To date | Do data |
| Total leaves allocated | Celkem přiděleno volna |
| Total leaves taken | Celkem čerpáno volna |
| Training event | Školení |
| Training program | Vzdělávací program |
| Transaction deletion record to delete | Záznam transakce k odstranění |
| Unpaid | Nezaplaceno |
| Uom | Měrná jednotka |
| Upload | Nahrát |
| User | Uživatel |
| Vehicle log | Kniha jízd |
| Warehouse | Sklad |
| Work order | Výrobní příkaz |
| Workflow | Workflow |
| Working from home | Práce z domova |
| Working hours | Pracovní doba |
| Working hours threshold for absent | Práh pracovní doby pro nepřítomnost |
| Working hours threshold for half day | Práh pracovní doby pro půl dne |
| Workspace | Pracovní plocha |
| Yes | Ano |

## Jak rozšiřovat pokrytí (další kola překladu)

`czech_localization/czech_localization/translations/cs.csv` obsahuje
**14 418 ověřených překladů** — fáze 1 (247 ručně ověřených klíčových
termínů pro DocTypy, zaměstnance/docházku/dovolené/směny/projekty a
základní prodej/nákup/sklad/účetnictví) plus fáze 2 (14 171 řetězců
přeložených po dávkách přes AI asistenta podle této terminologie,
s automatickou kontrolou zachování placeholderů/HTML a promítnutím
zpět do slovníku výše, viz commit "Add bulk Czech translations for
remaining pending strings").

Zbytek — **499 řetězců** ve `scripts/translation/pending_strings.csv`
— je vědomě nepřeložený: jde o interní `snake_case` fieldnames, SQL/
formátovací klíčová slova, samostatné nejednoznačné zkratky a pár
poškozených/neúplných zdrojových řetězců, kde je bezpečnější nechat
anglický originál než hádat špatný překlad (viz pravidlo 4 níže).
CSV má tři sloupce (anglicky, česky [prázdné], kontext), připravené
k doplňování, pokud se pro některý z nich najde jistý překlad.

Doporučený postup pro další kolo:

1. Vezmi dávku ~50–100 řádků z `pending_strings.csv`.
2. Přelož je **s ohledem na gramatiku celé fráze**, ne mechanicky
   slovo od slova — v ideálním případě přes AI asistenta, kterému dáš
   k dispozici tuto tabulku jako závaznou terminologii.
3. Nové/potvrzené termíny přidej do tabulky výše i do `cs.csv`.
4. Přeložené řádky z `pending_strings.csv` odeber.
5. Commitni do Gitu — každé kolo je samostatný, review-ovatelný commit.

Při aktualizaci ERPNext/HRMS spusť znovu
`scripts/translation/extract_strings.py` proti nové verzi zdrojových
repozitářů a nové řetězce (diff proti současnému `cs.csv` +
`pending_strings.csv`) přidej do backlogu stejným postupem — nepřekládá
se nikdy od nuly, jen delta (viz `DEPLOYMENT.md`, sekce Aktualizace).
