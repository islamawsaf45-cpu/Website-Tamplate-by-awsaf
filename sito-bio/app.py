from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dati = {
        'nome': 'Your_Name',
        'descrizione': 'Your description' ,
        
        # Link social reali per i pulsanti rotondi/colorati
        'link_discord': 'Your_Discord_Link',
        'link_tiktok': 'Your_Tiktok_Link',
        'link_youtube': 'Your_youTube_link',
        
        # Link reali per i tre grandi rettangoli con i bordi rossi
        'link_Your link name here': 'Your_link_Here',
        'link_Your link name here': 'Your_link_here',
        'link_Your link name here': 'Your_Link_Here'
    }
    return render_template('index.html', utente=dati)

if __name__ == '__main__':
    app.run(debug=True)
