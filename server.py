from flask import Flask, render_template, request, redirect, url_for, flash
from settings import OPTIONS, DATA_LABELS, DATA_LABELS_WITH_ID, TABLE_HEADER
import data_manager

app = Flask(__name__)
app.secret_key = "some_secret"


@app.route('/')
@app.route('/list')
def route_index():
    data_list = data_manager.read_file()
    return render_template('list.html',
                           table_header=TABLE_HEADER,
                           data_list=data_list)


@app.route('/story')
def route_story():
    title = "Super Sprinter 3000 - Add new Story"
    headline = "User Story manager - Add new Story"
    button = "Create"
    mode = "create"
    return render_template('form.html',
                           options=OPTIONS,
                           title=title,
                           headline=headline,
                           button=button,
                           mode=mode,
                           selected_story_dict={})


@app.route('/story/<int:id_story>')
def route_id_story(id_story):
    title = "Super Sprinter 3000 - Edit Story"
    headline = "User Story manager - Edit Story"
    button = "Update"
    mode = "edit"
    data_list = data_manager.read_file()
    for item in data_list:
        if item[0] == str(id_story):
            selected_story_dict = {label: item for label, item in zip(DATA_LABELS, item[1:])}
            return render_template('form.html',
                                   options=OPTIONS,
                                   title=title,
                                   headline=headline,
                                   button=button,
                                   mode=mode,
                                   id_story=id_story,
                                   selected_story_dict=selected_story_dict)
    return "This ID has no story attached to it."


@app.route('/save-story', methods=['POST'])
def route_save_story():
    print('SAVE request recieved')
    id_story = data_manager.get_id_form_file()
    data_manager.write_form_to_file(request.form, id_story)
    return redirect(url_for('route_index'))


@app.route('/edit-story', methods=['POST'])
def route_edit_story():
    print('EDIT request recieved')
    id_story = request.form['id_story']
    data_update_list = [request.form[label] for label in DATA_LABELS_WITH_ID]
    data_manager.update_file(id_story, data_update_list)
    return redirect(url_for('route_index'))


@app.route('/delete-story', methods=['POST'])
def route_delete_story():
    print('DELETE request recieved')
    id_story = request.form['id_story']
    data_manager.delete_story_from_file(id_story)
    return redirect(url_for('route_index'))


if __name__ == '__main__':
    app.run(debug=True)
