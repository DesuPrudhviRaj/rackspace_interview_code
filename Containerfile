FROM python:3.10
RUN pip install PrettyTable
COPY rack-bill-code.py .
cmd python3 ./rack-bill-code.py
