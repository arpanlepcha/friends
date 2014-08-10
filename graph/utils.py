import json


def serialize(queryset):
    return json.dumps([dict(name=friend.name, surname=friend.surname, age=friend.age, gender=friend.gender,
                            id=friend.pk)for friend in queryset])


def filter_user(queryset, user_list):
    intersect = lambda x, y: len(set(x).intersection(set(y))) >= 2
    return serialize([user for user in queryset if intersect(user.friend_list(), user_list)])
