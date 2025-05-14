name: NOM_DU_WORKFLOW

on:
  event_trigger: ...

jobs:
  nom_du_job:
    runs-on: ubuntu-latest

    steps:
      - name: Étape 1
        run: commande_shell

      - name: Étape 2
        uses: une_action_existante@version

