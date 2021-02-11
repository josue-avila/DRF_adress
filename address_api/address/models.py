from django.db.models import Model, CharField, DateTimeField


class Address(Model):
    cep = CharField(max_length=11, null=False)
    complement = CharField(max_length=100, null=True, blank=True)
    number = CharField(max_length=4, null=False)
    street = CharField(max_length=100, null=True)
    district = CharField(max_length=100, null=True)
    city = CharField(max_length=100, null=True)
    state = CharField(max_length=100, null=True)
    country = CharField(max_length=100, default="Brasil")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.complement} - \
        {self.district}, {self.city}, {self.state}, {self.country}"
