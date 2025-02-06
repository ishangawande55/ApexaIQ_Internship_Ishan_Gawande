PYTHONPATH=$(pwd) pytest tests/test_api.py -v

PYTHONPATH=$(pwd) pytest tests/test_api.py -v --html=report.html --self-contained-html