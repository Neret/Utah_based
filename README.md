# ThinkPad Sealed Hummingbird

Obiettivo: partire da una base Hummingbird pulita, aggiungere solo i pacchetti
utili al ThinkPad dal repository OCI di [Utah](https://github.com/projectbluefin/utah)
e mantenere la catena di avvio sigillata con composefs, UKI firmata e
systemd-boot.

## Build

- `seal/Containerfile.base` parte da `os-minimal` Hummingbird e installa i
  pacchetti elencati in `recipes/packages.txt`. Il repository Utah è fissato a
  digest e montato solo durante l'installazione: gli RPM e i metadati non
  vengono copiati nell'immagine.
- `sbsigntools` è l'unica eccezione: arriva dai repository Fedora 45 ufficiali,
  con verifica GPG, perché `sealed-sync` ne usa `sbattach` e `sbverify`.
- `.github/workflows/build.yml` verifica firma Cosign e attestazione GitHub
  del repository Utah prima di creare la base preparata.
- `recipes/recipe.yml` applica le personalizzazioni ThinkPad e i servizi
  dell'immagine.
- `.github/workflows/build-sealed.yml` conserva il flusso composefs, UKI,
  Secure Boot e systemd-boot.

Il repository pacchetti upstream è
[projectbluefin/utah-packages](https://github.com/projectbluefin/utah-packages).
Non copiare qui il suo manifest completo: aggiornare la lista locale solo con
i pacchetti necessari a questo sistema. Quando si aggiorna il digest Utah,
verificare la nuova provenienza e la compatibilità con Hummingbird prima della
build.
