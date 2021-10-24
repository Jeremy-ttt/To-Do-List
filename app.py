from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'todo.jeremytt66.club'
json_path = os.path.dirname(os.path.abspath(__file__)) + '\data.json'
print(json_path)
@app.route('/', methods=['GET', 'POST'])
def todolist():
    if request.method == 'GET':
        with open("data.json", 'r', encoding='utf-8') as f:
            data = f.read()
        data = json.loads(data)
        tasks = data['data']
        total = data['total']
        return render_template('index.html', tasks=tasks, total=total, zip=zip)


@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        form = request.form.to_dict()
        print(form)
        content = form['content']
        with open(json_path, 'r', encoding='utf-8') as f:
            data = f.read()
        data = json.loads(data)
        data['data'].append({"name": content, "status": "undone"})
        data['total'] = int(data['total'])+1
        with open(json_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data))
        return redirect(url_for('todolist'))



@app.route('/delete', methods=['POST'])
def delete_task():
    if request.method == 'POST':
        form = request.form.to_dict()
        print(form)
        delete_index = int(form['delete_task'].replace("delete", ""))
        with open(json_path, 'r', encoding='utf-8') as f:
            data = f.read()
        data = json.loads(data)
        data['total'] = data['total'] - 1
        data['data'] = data['data'][:delete_index] + data['data'][delete_index + 1:]
        with open(json_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data))
        return redirect(url_for('todolist'))



@app.route('/change_status', methods=['POST'])
def change_status():
    if request.method == 'POST':
        form = request.form.to_dict()
        print(form)
        task_index = int(form['change_status'].replace("change", ""))
        with open(json_path, 'r', encoding='utf-8') as f:
            data = f.read()
        data = json.loads(data)
        status = data['data'][task_index]['status']
        if status == 'done':
            data['data'][task_index]['status'] = 'undone'
        else:
            data['data'][task_index]['status'] = 'done'
        with open(json_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data))
        return redirect(url_for('todolist'))


if __name__ == '__main__':
    app.run()
