from flask import Flask, render_template, request, make_response
import requests
import json
import psycopg2
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        answer=""
        address = request.form.get('address')
        connection = psycopg2.connect("dbname=db_nft user=postgres password='faha' port=5433")
        cur = connection.cursor()
        cur.execute("SELECT nft_metadata FROM nft where nft_address='" + address + "'")
        if cur.rowcount==0:
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)

            headers = {
                "accept": "application/json",
                "X-API-Key": "KWWugGMUt7x1iqf0sAjQK9LlRa92jROvaX37DcMZjiiDxtfW4pX04TArIYE6JpZw"
            }

            response = requests.get(url, headers=headers)
            answer = response.text
            connection = psycopg2.connect("dbname=db_nft user=postgres password='faha' port=5433")

            cur = connection.cursor()
            cur.execute("insert into nft(nft_address,nft_metadata) values('{}','{}')".format(address, answer))
            connection.commit()
        else:
            records = cur.fetchall()
            answer = records[0][0]
        return '''
                        <p>{}</p>
                          '''.format(answer)

    # otherwise handle the GET request
    return '''
                   <form method="POST">
                       <label>Enter nft address: <input type="text" name="address"></label>
                       <input type="submit" value="Submit">
                   </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=5000)
