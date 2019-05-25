ECHO ON

REM Create the Conda environment
conda env update --name "%~1" --file environment.yml

REM Switch to the newly created environment
activate "%~1"

REM Configure Notebook Diff
nbdime extensions --enable
jupyter nbextension enable nbdime --py
nbdime config-git --enable
