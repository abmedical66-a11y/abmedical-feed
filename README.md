# Feed XML AB Medical per Wow che Prezzi

Il workflow GitHub Actions scarica il feed AdNabu compresso, lo decomprime, ne verifica la validità XML e lo pubblica nella cartella `docs`.

## Attivazione

1. Caricare i file nel repository, conservando le cartelle.
2. In **Settings → Pages**, scegliere **Deploy from a branch**, branch **main**, cartella **/docs**, quindi **Save**.
3. In **Actions → Aggiorna feed AB Medical → Run workflow**, eseguire il primo aggiornamento.
4. Verificare che `docs/catalogo.xml` sia presente e che l'indirizzo Pages restituisca XML leggibile.

URL previsto (solo dopo attivazione e verifica): `https://abmedical66-a11yl.github.io/abmedical-feed/catalogo.xml`

Aggiornamento programmato quattro volte al giorno (UTC); GitHub può ritardare o saltare esecuzioni programmate. Verificare periodicamente l'ultimo aggiornamento.

**Nota:** il feed è pubblico, così come la cronologia delle versioni. Non aggiungere credenziali. I dati vengono ripubblicati senza modificare Shopify o Google Merchant Center. GitHub Pages può imporre limiti dimensionali: controllare la dimensione effettiva del file prima di utilizzare l'URL.
