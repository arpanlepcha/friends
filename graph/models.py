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

def util(d):
    friend_list = {}

    for user in d:
        friend_list[user.get('id')] = user.pop('friends', None)
        user['name'] = user.pop('firstName')
        p = Profile(**user)
        p.save()

    for key, value in friend_list.iteritems():
        p = Profile.objects.get(pk=key)
        for user in value:
            f = Profile.objects.get(pk=user)
            p.friends.add(f)
