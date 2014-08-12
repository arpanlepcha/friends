from django.db import models


class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    name = models.CharField(max_length=64, blank=False)
    surname = models.CharField(max_length=64, blank=True)
    age = models.PositiveSmallIntegerField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    friends = models.ManyToManyField('self', symmetrical=False)



    def __unicode__(self):
        return '%s-%s' % ( self.name, self.surname)

    def friend_list(self):
        return [friend.pk for friend in self.friends.all()]

