from django.shortcuts import render
from django.views import generic
from matplotlib.style import context

class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print("Hello!")
        request.session['answer'] = []  # この変数にユーザーが答えたタグを追加しようと思う
        return super().get(request, **kwargs)


class OptionView(generic.TemplateView):
    template_name = "option.html"


class QuestionView(generic.TemplateView):
    template_name = "quetion.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):  # 質問に答えた時に行う動作を記述する(富島)
        context = {}
        return render(request, self.template_name, context)


class ResultsView(generic.TemplateView):
    template_name = "results.html"

    def get(self, request, *args, **kwargs):
        context = {}
        """
        ここで藤田君が
        request.session['answer']の値とデータセット上の趣味群を比較して最適な趣味を
        下のcontext['your_hobby']に格納する
        """
        context['your_hobby'] = 'hogehoge'  # congtextのyour_hobbyに診断結果を入れる
        return render(request, self.template_name, context)