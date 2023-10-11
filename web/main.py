# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, json
from __init__ import create_app, db
from models import Question
from sqlalchemy import or_, and_, cast, Date, Sequence, func
import requests

app = create_app()


#Функция пост запроса к серверу для теста
@app.route('/sendpost', methods=['GET'])
def sendpost():

    requests.post('http://127.0.0.1:5000/api/v1/post', json={"questions_num": 10})

    return 'Post Send'


#Функция поиска вопросов и ответов
@app.route('/api/v1/post', methods=['POST'])
def api_answerdata():

    userpost = request.get_json()
    r = requests.get('https://jservice.io/api/random?count={}'.format(userpost['questions_num']))
    answer = r.json()

    for items in answer:

        findinbase = bool(Question.query.filter_by(idanswer=str(items['id'])).first())

        if findinbase == False:
            new_question = Question(idanswer=items['id'], question=items['question'], answer=items['answer'], created_at=items['created_at'])
            db.session.add(new_question)
            db.session.commit()
        else:
            while True:
                rnew = requests.get('https://jservice.io/api/random?count={}'.format(1))
                answernew = rnew.json()

                for itemsnew in answernew:

                    findinbase = bool(Question.query.filter_by(idanswer=str(itemsnew['id'])).first())

                    if findinbase == False:
                        new_question = Question(idanswer=itemsnew['id'], question=itemsnew['question'],answer=itemsnew['answer'], created_at=itemsnew['created_at'])
                        db.session.add(new_question)
                        db.session.commit()
                        break

    last_item = Question.query.order_by(Question.id.desc()).first()

    print(jsonify(last_item).json)

    return jsonify(last_item)




#Функция поиска вопросов и ответов
@app.route('/api/v1/allpost', methods=['GET'])
def api_alldata():



    all_items = Question.query.order_by(Question.id.desc()).all()


    return jsonify(all_items)











if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(host='0.0.0.0', debug=True)