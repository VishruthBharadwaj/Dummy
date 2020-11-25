from rest_framework import serializers

from .models import Member
import time



class MemberSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		
		
		model = Member
		fields = ('employee_name','employee_salary','employee_age','profile_image','id_no')




