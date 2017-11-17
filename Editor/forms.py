from django import forms
from .models import T_NormativAct
#Данный файл отвечает за авто-генерацию форм
class PostForm(forms.ModelForm):

    class Meta:
        model = T_NormativAct
        fields = ('status','doctype','signing','regnum',
        'regdate','executor','theme','topic','docsubtype',
        'publicateflag','numofnewspaper','publicatedin',
        'publicatedate','mainexecutor','controldate',
        'result','controloff','pagescount','addonscount'
        ,'archivedelo','archivetom','sheetscount','file')
