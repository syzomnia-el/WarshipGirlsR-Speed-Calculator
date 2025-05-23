uv run pyinstaller -F --optimize 2 src/mean.py -n mean --distpath bin/ --clean
rm -r build/
rm mean.spec
ls bin/