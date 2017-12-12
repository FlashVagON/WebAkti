from django.db import models


class T_Status(models.Model):
    status = models.CharField("Статус документа", max_length=200)

    def __str__(self):  # \__
        return self.status  # / такая штука для вывода текста

    class Meta:
        # default_manager_name = 'Статусы документа'
        verbose_name = 'Статус документа'


class T_Doctype(models.Model):
    doctype = models.CharField("Тип документа", max_length=200)

    def __str__(self):
        return self.doctype

    class Meta:
        verbose_name = 'Тип документа'


class T_Signing(models.Model):
    typeossigning = models.CharField("Подписание документа", max_length=200)

    def __str__(self):
        return self.typeossigning

    class Meta:
        verbose_name = 'Вид подписания'


class T_Executor(models.Model):
    executor = models.CharField("Исполнитель документа", max_length=200)

    def __str__(self):
        return self.executor

    class Meta:
        verbose_name = 'Исполнители'


class T_Theme(models.Model):
    theme = models.CharField("Тема", max_length=2000)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Тема документа'


class T_Docsubtype(models.Model):
    subtype = models.CharField("Вид документа", max_length=200)

    def __str__(self):
        return self.subtype

    class Meta:
        verbose_name = 'Вид документа'


class T_Publicationlocate(models.Model):
    publicatedin = models.CharField("Где опубликовано", max_length=200)

    def __str__(self):
        return self.publicatedin

    class Meta:
        verbose_name = 'Место опубликования'


class T_Mainexecutor(models.Model):
    mainexecutor = models.CharField("Ответственный исполнитель", max_length=200)

    def __str__(self):
        return self.mainexecutor

    class Meta:
        verbose_name = 'Ответственный исполнитель'


class T_Signers(models.Model):
    name = models.CharField("ФИО", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подписывающие'


class T_Acceptancers(models.Model):
    name = models.CharField("ФИО", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Утверждающие'


class T_NormativAct(models.Model):
    status = models.ForeignKey(T_Status, verbose_name="Статус", on_delete=models.CASCADE)
    doctype = models.ForeignKey(T_Doctype, verbose_name="Тип документа", on_delete=models.CASCADE)
    signing = models.ForeignKey(T_Signing, verbose_name="Вид подписания", on_delete=models.CASCADE)
    regnum = models.CharField("Рег. №", max_length=200)
    regdate = models.DateField(verbose_name="Регистрационная дата")
    executor = models.ForeignKey(T_Executor, verbose_name="Исполнитель", on_delete=models.CASCADE)
    theme = models.ForeignKey(T_Theme, verbose_name="Тема", on_delete=models.CASCADE)
    topic = models.CharField("Заголовок", max_length=2000)
    docsubtype = models.ForeignKey(T_Docsubtype, verbose_name="Подтип документа", on_delete=models.CASCADE)
    publicateflag = models.BooleanField("подлежит опубликованию")
    numofnewspaper = models.CharField("№ газеты", max_length=200)
    publicatedin = models.ForeignKey(T_Publicationlocate, verbose_name="Опубликовано в", on_delete=models.CASCADE)
    publicatedate = models.DateField(verbose_name="дата публикации")
    mainexecutor = models.ForeignKey(T_Mainexecutor, verbose_name="Ответственный исполнитель", on_delete=models.CASCADE)
    controldate = models.DateField(verbose_name="дата контроля")
    result = models.BooleanField("результат исполнения")
    controloff = models.BooleanField("снято с контроля")
    pagescount = models.IntegerField("кол-во листов")
    addonscount = models.IntegerField("колво приложений")
    archivedelo = models.CharField("Дело №", max_length=200)
    archivetom = models.CharField("Том №", max_length=200)
    sheetscount = models.IntegerField("Листы")
    file = models.FileField("Файл", upload_to="tmp/", blank=True)
    ageementers = models.ManyToManyField(T_Acceptancers, verbose_name="Утверждено")
    signers = models.ManyToManyField(T_Signers, verbose_name="Подписано")
    def __str__(self):
        return self.regnum

    class Meta:
        verbose_name = 'Нормативные акты'

        # на удаление
    # class T_NormativAct_podchin(models.Model):
    # normact = models.ForeignKey(T_NormativAct, on_delete=models.CASCADE)
    # signername = models.ManyToManyField(T_Signers)
    # def __str__(self):
    # return self.normact
    # class Meta:
    # verbose_name = 'Кем подписан'
    # class T_NormativAct_podchin2(models.Model):
    # normact = models.ForeignKey(T_NormativAct, on_delete=models.CASCADE)
    # signername = models.ManyToManyField(T_Acceptancers)
    # def __str__(self):
    # return self.normact
    # class Meta:
    # verbose_name = 'Кем утвержден'
