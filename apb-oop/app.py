from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class NameApp:
    def __init__(self):
        self.names = []

    def add_name(self, new_name):
        self.names.append(new_name)

    def delete_name(self, name):
        self.names.remove(name)

name_app = NameApp()

@app.route('/')
def index():
    return render_template('index_oop.html', names=name_app.names)

@app.route('/add', methods=['POST'])
def add_name():
    new_name = request.form.get('new_name')
    name_app.add_name(new_name)
    return redirect(url_for('index'))

@app.route('/delete/<name>')
def delete_name(name):
    name_app.delete_name(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
