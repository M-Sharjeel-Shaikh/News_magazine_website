
echo = "BUILD START"
python3.7.5 -m pip install -r requirment.txt
python3.7.5 manage.py collectstatic  --noinput --clear
echo = "BUILD END"