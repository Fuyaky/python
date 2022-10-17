solana api
import requests
adress ="3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU"
url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)

headers = {
    "accept": "application/json",
    "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z"
 }

 response = requests.get(url, headers=headers)

 print(response.text)

#postgre
import psycopg2
conn = psycopg2.connect("dbname=db_nft user=postgres password='faha'")
cur = conn.cursor()
cur.execute("SELECT * FROM testValues where randomString='hello world'")
records = cur.fetchall()
print(records)
cur.execute("insert into testValues(randomString) values('hello world')")
conn.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
