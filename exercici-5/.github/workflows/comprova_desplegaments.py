name: Empaquetat

on:
  push:
    branches:
      - main

jobs:
  test-linux:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del repositorio
        uses: actions/checkout6

      - name: Configurar entorno Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.13'

      - name: Ejecutar test unitarios
        run: python -m unittest -v

      - name: Compilar ejecutable binario
        run: pyinstaller --onefile comprova_desplegaments.py


  test-win:
    runs-on: windows-latest
    steps:
      - name: Checkout del repositorio
        uses: actions/checkout6

      - name: Configurar entorno Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Ejecutar test unitarios
        run: python -m unittest -v

      - name: Compilar ejecutable binario
        run: pyinstaller --onefile comprova_desplegaments.py


  test-mac:
    runs-on: macos-latest
    steps:
      - name: Checkout del repositorio
        uses: actions/checkout6

      - name: Configurar entorno Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.13'

      - name: Ejecutar test unitarios
        run: python -m unittest -v

      - name: Compilar ejecutable binario
        run: pyinstaller --onefile comprova_desplegaments.py


