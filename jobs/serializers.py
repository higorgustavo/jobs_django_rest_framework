from rest_framework import serializers
from django.urls import reverse
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        exclude = ("is_active", "applicants")
        extra_kwargs = {
            "title": {"min_length": 10},
            "salary": {"min_value": 1000},
            "description": {"min_length": 10, "max_length": 500},
            "company": {"min_length": 3},
            "location": {"min_length": 10},
        }

    def get_links(self, obj):
        links = []
        self_link = reverse("jobs:detail", kwargs={"pk": obj.pk})
        links.append({
            "type": "GET",
            "rel": "self",
            "href": self_link,
        })
        links.append({
            "type": "PUT",
            "rel": "update_job",
            "href": self_link,
        })
        links.append({
            "type": "DELETE",
            "rel": "delete_job",
            "href": self_link,
        })
        return links

    # Outro tipo de Validação    

    # def validate_title(self, value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError("Deve conter pelo menos 10 caracteres")
    #     return value
    
    # def validate_salary(self, value):
    #     if value < 1000:
    #         raise serializers.ValidationError("O salário deve ser maior que R$ 1.000,00")
    #     return value
    
    # def validate_description(self, value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError("Deve conter pelo menos 10 caracteres")
    #     return value
    
    # def validate_company(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Deve conter pelo menos 10 caracteres")
    #     return value
