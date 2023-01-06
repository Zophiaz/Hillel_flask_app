from flask import Flask
from flask import request, render_template
from database_file import DBManager
from celery_work import add
import alchemy_db
import models_db
from sqlalchemy import select

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        conn = alchemy_db.engine.connect()
        res1 = select(models_db.SQL_base)
        result = conn.execute(res1)
        data_res = result.fetchall()
        print(result)
    pass
    return "OK"


@app.route("/logout", methods=['GET'])
def logout():
    add.apply_async(args=(1, 2))
    return "OK"


@app.route("/register", methods=['GET', 'POST'])
def register():
    return "OK"


@app.route("/user_page", methods=['GET'])
def user_page():
    return "OK"


@app.route("/currency", methods=['GET', 'POST'])
def currency_converter():

    if request.method == 'POST':

        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with DBManager() as db:
            buy_rate_1, sale_rate_1 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_currency_1}" ')

            buy_rate_2, sale_rate_2 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_currency_2}" ')

        cur_excange_buy = round(buy_rate_2 / buy_rate_1, 2)
        cur_excange_sale = round(sale_rate_2 / sale_rate_1, 2)

        return render_template('form.html',
                               cur_excange_buy=cur_excange_buy,
                               cur_excange_sale = cur_excange_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2 = user_currency_2
                               )
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
