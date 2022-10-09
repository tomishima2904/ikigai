from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import HobbiesTmp, Hobbies  # 趣味データベース

import numpy as np
class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print("Hello!")
        request.session['answers'] = {}  # この変数にユーザーが答えたタグを追加しようと思う
        request.session['questions'] = {
            'outdoor': "屋外で活動したい?",
            'group': "大勢が好き?",
            'cost': "お金に余裕がある?",
            'skill': "スキルの習得に時間かかってもよい?"
        }
        return super().get(request, **kwargs)


class OptionView(generic.TemplateView):
    template_name = "option.html"


class QuestionView(generic.TemplateView):
    template_name = "question.html"

    def get(self, request, *args, **kwargs):
        context = {}
        tag, question = request.session['questions'].popitem()  # ランダムに質問とそれに対応するタグをポップ
        request.session['tag'] = tag
        context['tag'] = tag
        context['question'] = question
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):  # 質問にYesで答えた時にタグを記憶して、次の質問を提示(富島)
        context = {}
        # yesのボタンを押した時のみタグを記憶する
        if "btn_yes" in request.POST:
            request.session['answers'][request.session['tag']] = 1
        elif "btn_no" in request.POST:
            request.session['answers'][request.session['tag']] = 0
        print(f"User tags are {request.session['answers']}")

        # 質問がなくなった場合results.htmlに遷移
        if len(request.session['questions'])==0:
            print("All questions have been answered")
            return redirect('hobby:results')

        tag, question = request.session['questions'].popitem()  # ランダムに質問とそれに対応するタグをポップ
        request.session['tag'] = tag
        context['tag'] = tag
        context['question'] = question

        return render(request, self.template_name, context)


class ResultsView(generic.TemplateView):
    template_name = "results.html"
    hobbies = Hobbies.objects.all()
    def get(self, request, *args, **kwargs):
        context = {}
        # ユーザーの答えを取得，比較の際にリスト型を用いるためリスト型で取得
        answers = request.session['answers']
        answer_tags = list(answers.keys())
        answer_list = list(answers.values())

        # databaseから趣味の名前を取得
        hobbies_names = self.hobbies.values('hobby')

        # databaseのタグ情報を取得するルーチン
        # フィールド名を抽出して質問順にタグを整理する
        hobbies_fields = HobbiesTmp._meta.get_fields()
        field_list = []
        for field_check in answer_tags:
            for field in hobbies_fields:
                if field.name == field_check:
                    field_list.append(field.name)

        # フィールド名から存在するタグ要素を抽出
        field_tags = []
        for field in field_list:
            field_tags.append(self.hobbies.values_list(field))

        # 抽出したタグ要素を趣味毎になるように整理
        hobbies_tag = [[0 for i in range(len(field_tags))] for j in range(len(hobbies_names))]
        for j, hobby_tag in enumerate(field_tags):
            for i, tag in enumerate(hobby_tag):
                hobbies_tag[i][j] = tag[0]

        # タグの内容が一致した個数をカウントして辞書に格納
        result = {}
        for hobbiestag, hobbyname in zip(hobbies_tag, hobbies_names):
            matchlist = np.logical_xor(answer_list, list(hobbiestag))
            matchcount = len(matchlist) - np.sum(matchlist)
            result[hobbyname['hobby']] = matchcount

        # 一致率の高い順に辞書をソート
        result = dict(sorted(result.items(), key=lambda i: i[1], reverse=True))

        # 一致率の高い上位三位までを抽出
        result = {k:result[k] for k in list(result)[:3]}

        # 一致率の高い趣味の名前を取得
        result = list(result.keys())
        context['your_hobby'] = result # congtextのyour_hobbyに診断結果を入れる
        print(context['your_hobby'])  # ターミナル上に趣味が出力されればOK

        return render(request, self.template_name, context)