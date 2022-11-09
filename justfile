_:
    @just -l -u --list-heading $'Speed Test'

run:
    cd 3.10 && python ../main.py
    cd 3.11 && python ../main.py