from flask import Flask, render_template, request, make_response
import requests
import json
import psycopg2
app = Flask(__name__)



def check_in_db(address):
    connection = psycopg2.connect(user="postgres",
                                  password="faha",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="db_nft")
    cur = connection.cursor()
    cur.execute("SELECT * FROM nft where nft_address='"+address+"'")
    if(cur.rowcount==0):
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        answer=""
        address = request.form.get('address')
        if (check_in_db(address)):
            connection = psycopg2.connect(user="postgres", password="faha", host="127.0.0.1", port="5432",
                                          database="db_nft")

            cur = connection.cursor()
            cur.execute("SELECT nft_metadata FROM nft where nft_address='"+address+"'")
            records = cur.fetchall()
            answer=records[0][0]
        else:
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)
            headers = {
                "accept": "application/json",
                "X-API-Key": "KWWugGMUt7x1iqf0sAjQK9LlRa92jROvaX37DcMZjiiDxtfW4pX04TArIYE6JpZw"
            }
            answer = requests.get(url, headers=headers).text
            connection = psycopg2.connect(user="postgres", password="faha", host="127.0.0.1", port="5432",
                                          database="db_nft")

            cur = connection.cursor()
            cur.execute("insert into nft(nft_address,nft_metadata) values('{}','{}')".format(address, returnValue))
            connection.commit()
        return '''
                        <h1>{}</h1>
                          '''.format(answer)

    # otherwise handle the GET request
    return '''
                   <form method="POST"style="margin: auto; width: 220px; text-align: center;">
                       <div><label>address: <input type="text" name="address"></label></div>
                       <input type="submit" value="Submit">
                   </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=5432)