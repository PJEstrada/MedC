
from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.conf import  settings
from django.conf import settings


class Invoice(models.Model):

	#WILL NEED TO CHANGE ENTRY TYPES ONCE WE DECIDE HOW TO ENTER THEM


	customer_apellido = models.CharField(max_length=255)
	customer_segundo_apellido = models.CharField(max_length=255)
	customer_nombre = models.CharField(max_length=255)
	items = MultiSelectField(choices=settings.PRODUCTOS,
							 max_choices=4,
							 max_length=255)
	insurance = models.CharField(max_length=255, choices=settings.SEGUROS)
	date = models.DateField(auto_now_add=True, editable=False)
	total = models.FloatField()
	detalles = models.TextField(max_length=10000)


	def __unicode__(self):
		verbose = self.date + self.user + self.total + self.items+self.date+self.total+self.insurance
		return verbose




	############################################
	# I DON'T REALLY KNOW WHERE TO PUT THIS....#
	############################################


	def getInvoices(last,secondLast,first,secondFirst,item,insurer,startDate,endDate):
		q=Invoice.objects.all()
		if last is not None:
			q= q.filter(customerApellido__iexact=last)
		if secondLast is not None:
			q= q.filter(customerSegundoApellido__iexact=secondLast)
		if first is not None:
			q= q.filter(customerNombre__iexact=first)
		if secondFirst is not None:
			q= q.filter(customerSegundoNombre__iexact=secondFirst)
		if item is not None:
			q= q.filter(items__icontains=item)
		if insurer is not None:
			q= q.filter(insurance__iexact=insurer)
		if startDate is not None:
			q= q.filter(date_gte=startDate)
		if endDate is not None:
			q= q.filter(date_lte=endDate)

		return q