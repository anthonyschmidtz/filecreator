from flask import Flask, jsonify
from operations import FileCreator


app = Flask(__name__)
file_creator = FileCreator()


@app.route('/service/api/start_create_files', methods=['GET'])
def start_create_files():
    """
    начать создание файлов
    :return:
    """
    status = file_creator.start_thread()
    if status:
        status_code = 200
        status_msg = 'Успешно'
    else:
        status_code = 409
        status_msg = 'В настоящий момент файлы уже создаются'

    return jsonify({'description': status_msg}), status_code


@app.route('/service/api/stop_create_files', methods=['GET'])
def stop_create_files():
    """
    остановить создание файлов
    :return:
    """
    status = file_creator.stop_thread()
    if status:
        status_code = 200
        status_msg = 'Успешно'
    else:
        status_code = 409
        status_msg = 'В настоящий момент файлы не создаются'

    return jsonify({'description': status_msg}), status_code


if __name__ == '__main__':
    app.run()
