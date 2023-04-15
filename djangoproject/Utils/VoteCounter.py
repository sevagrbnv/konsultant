from votes.models import Vote


def voteCount(obj, type):
    filterargs = {'question_id': obj.id, 'type': type}
    return Vote.objects.filter(**filterargs).count()
