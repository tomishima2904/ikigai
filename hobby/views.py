from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import HobbiesTmp  # 趣味データベース

import random
class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print("Hello!")
        request.session['answers'] = {}  # この変数にユーザーが答えたタグを追加しようと思う
        request.session['questions'] = {
            'outdoor': "外は好き?",
            'team': "大勢が好き?",
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
    hobbies = HobbiesTmp.objects.all()

    def get(self, request, *args, **kwargs):
        context = {}
        """
        ここで藤田君が
        request.session['answers']の値を元にhobbiesから趣味を抽出する
        そんで下のcontext['your_hobby']に格納する
        """
        context['your_hobby'] = 'hogehoge'  # congtextのyour_hobbyに診断結果を入れる
        print(context['your_hobby'])  # ターミナル上に趣味が出力されればOK
        return render(request, self.template_name, context)