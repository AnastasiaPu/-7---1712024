from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/api/gifts', methods=['GET'])
def get_gifts():
  conn = sqlite3.connect('gifts.db')
  c = conn.cursor()
  c.execute('SELECT * FROM gifts')
  gifts = c.fetchall()
  conn.close()
  return jsonify({'gifts': gifts})

@app.route('/')
def index():
  conn = sqlite3.connect('gifts.db')
  c = conn.cursor()
  c.execute('SELECT * FROM gifts')
  gifts = c.fetchall()
  conn.close()
  return render_template('index.html', gifts=gifts)


if __name__ == '__main__':
    app.run(debug=True)