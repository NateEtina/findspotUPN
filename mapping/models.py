from django.db import models

class AddressType(models.Model):
    label = models.CharField(max_length=40, verbose_name=('Nom de la catégorie'))
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ("Catégorie d'adresse")
        verbose_name_plural = ("Catégories d'adresses")

    def __str__(self):
        return self.label

class Address(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    interest = models.BooleanField(default=False, verbose_name=("Définir point d'interêt"))
    description = models.TextField(blank = True, null=True, verbose_name=("Description de l'adresse"))
    adtype = models.ForeignKey(AddressType, verbose_name=("Catégorie de l'adresse"), on_delete=models.CASCADE)

class Building(Address):
    name = models.CharField(max_length=100, verbose_name=('Nom du bâtiment/bureau'))  
    localnum = models.IntegerField(verbose_name=('Nombre de locaux'),null=True, blank=True, default=0)
    burnum = models.IntegerField(verbose_name=('Nombre de bureaux/directions'),null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Bâtiments")
        verbose_name_plural = ("Bâtiments")

    def __str__(self):
        return self.name

class Bureau(Address):
    name = models.CharField(max_length=100, verbose_name=("Nom du Bureau/Direction"))  
    burbuilding = models.ForeignKey(Building, verbose_name=("Son bâtiment"),null=True, blank=True, default='Aucun', on_delete=models.CASCADE)
    hallnum = models.IntegerField(verbose_name=('Nombre d\'office'),null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Bureau/Direction")
        verbose_name_plural = ("Bureaux/Directions")

    def __str__(self):
        return self.name

class Office(Address):
    name = models.CharField(max_length=100, verbose_name=("Nom de l'office")) 
    officebur = models.ForeignKey(Building, verbose_name=("Son bureau"), on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Office")
        verbose_name_plural = ("Offices")

    def __str__(self):
        return self.name

class Local(Address):
    name = models.CharField(max_length=100, verbose_name=("Nom du Local"))  
    burbuilding = models.ForeignKey(Building, verbose_name=("Son bâtiment"), null=True, blank=True, default='Aucun', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Local/Salle")
        verbose_name_plural = ("Locaux/Salles")

    def __str__(self):
        return self.name

class Space(Address):
    name = models.CharField(max_length=100, verbose_name=("Nom de l'espace"))  
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Espace")
        verbose_name_plural = ("Espaces")

    def __str__(self):
        return self.name
