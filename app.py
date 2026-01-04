rom flask import Flask,render_template_string, reguest
import os
import psycopg 2

app = Flask(_name_)

DATABASE_URL = os.getenv("Database_Url","postgresql://enes:R9jTctcoXYU3SmSm63KrQ06N4cR9jv91@dpg-d426sq1r0fns739058mg-a/bulut_bilisim_2")

HTML = """
<!doctype html>
<html>
<head>
     <title>Dünyadan Selam!</title>
     <style>
       body { font-family : Arial; text-align: center; padding: 50px; background: #ef2f3; }
       hi { color : #333; }
       form { margin: 20px auto; }
       input { padding:10px; font-size: 16px; }
       button {padding: 10px 15px; background: #4CAF50; color: white; border-radius: 6px; cursor: pointer; }
       ul { list-style: none; padding: 8px; border-radius 5px; }
       li { background: white; margim: 5px auto; width 200px; padding: 8px; border-radius: 5px; }
     </style>
</head>
<body>
     <h1>Buluttan Selam!</h1>
     <p>Adını yaz,selamını bırak </p>
     <form method ="POST">
          <input type="text" name="isim" placeholder="Adını yaz" required>
          <button type="submit">Gönder</button>
     </form>
     <h3>Ziyaretçiler:</h3>
     <ul>
</body>
</html>
"""
def connect_db():
     conn = psycopg2.connect(DATABASE_URL)
     return conn
@app.route("/", methods=["GET" , "POST"])
def index():
     conn = connect_db()
     cur = conn.cursor()
     cur.execute("CREATE TABLE İN NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY,isim TEXT))

     if request.method == "POST":
        isim = request.form.get("isim")
         if isim:
           cur.execute("İNSERT İNTO ziyaretciler (isim) VALUES (%s)",(isim,))
           conn.commit()
     cur.execute(SELECT isim FROM ziyaretciler ORDER BY id DESC LİMİT 10")
     isimler = [row[0] for row in cur.fettchall()]

     cur.close()
     conn.close()
     return render_template_string(HTML, isimler=isimler)
 if _name_=="_main_":
      app.run(host="0.0.0.0",port=5000)
