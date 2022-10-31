from datetime import datetime
import mysql.connector
from flask import Flask, request
from Sale import Sale, Currency

app = Flask(__name__)

SALES_TABLE = 'Sales'
CURRENCY_TABLE = 'Currency'

# get target currency from user, and print sales per day in that currency

@app.route('/report', methods=['GET', 'POST'])
def get_report():
    cursor = cnx.cursor()
    sales_query = ('SELECT * FROM {0}'.format(SALES_TABLE))
    cursor.execute(sales_query)
    sales = []
    for row in cursor:
        sales.append(Sale(row[0], row[1], row[2]))

    target = request.args.get('target')
    rate_query = ("SELECT exchange_rate FROM {0} WHERE source_currency=%s AND target_currency=%s AND start_date <=%s ORDER BY start_date DESC LIMIT 1 ;").format(CURRENCY_TABLE)
    report = {}
    for sale in sales:
        if str(sale.date) not in report:
            report[str(sale.date)] = 0
        if sale.currency == target:
            rate = 1
        else:
            cursor.execute(rate_query, [sale.currency, target, sale.date])
            for row in cursor:
                rate = row[0]
        # get rate for this particular sale .. currency, date
        report[str(sale.date)] += sale.amount * float(rate)
    cursor.close()

    return report



@app.route('/currency', methods=['GET'])
def get_rates():
    source, target = request.args.get('source'), request.args.get('target')
    cursor = cnx.cursor()
    curr_query = ('SELECT * FROM {0} WHERE source_currency=%s AND target_currency=%s;'.format(CURRENCY_TABLE))
    cursor.execute(curr_query, [source, target])
    currencies = []
    for row in cursor:
        c = Currency(row[0], row[1], row[2], row[3])
        currencies.append(str(c))

    cursor.close()
    html = '<ol>\n'
    for currency in currencies:
        html += currency
    response = html + '\n</ol>'
    return response


@app.route('/sales/<date>')
def get_sales(date):
    cursor = cnx.cursor()
    query = ('SELECT * FROM {0} WHERE sales_date=%s'.format(SALES_TABLE))
    d = datetime.strptime(date, "%Y-%m-%d")
    cursor.execute(query, [d])
    sales = []
    for row in cursor:
        sales.append(str(Sale(row[0], row[1], row[2])))

    cursor.close()
    html = '<ol>\n'
    for sale in sales:
        html += sale
    response = html + '\n</ol>'
    return response


if __name__ == '__main__':
    cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='interview_schema')
    app.run(debug=True, host='localhost')
    cnx.close()
