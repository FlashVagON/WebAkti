from django import forms
from .models import T_NormativAct
from django.forms.extras.widgets import SelectDateWidget


# from django.contrib.admin.widgets import AdminDateWidget use admin widget


class PostForm(forms.ModelForm):
    regdate = forms.DateField(label="Регистрационная дата", widget=SelectDateWidget())
    publicatedate = forms.DateField(label="Дата публикации", widget=SelectDateWidget())
    controldate = forms.DateField(label="Дата контроля", widget=SelectDateWidget())

    class Meta:
        model = T_NormativAct
        fields = ['status', 'doctype', 'signing', 'regnum',
                  'regdate', 'executor', 'theme', 'topic', 'docsubtype',
                  'publicateflag', 'numofnewspaper', 'publicatedin',
                  'publicatedate', 'mainexecutor', 'controldate',
                  'result', 'controloff', 'pagescount', 'addonscount',
                  'archivedelo', 'archivetom', 'sheetscount', 'file']
