from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from test_app.models import Worker
from test_app.serializers import WorkerSerializer


def index_page(request):
    # create
    # new_worker = Worker(name='Иван', second_name='Иванов', salary=0)
    # new_worker.save()

    # get and update
    # worker_by_id = Worker.objects.get(id=1)
    # worker_by_id.salary = worker_by_id.salary + 10
    # worker_by_id.save()

    # get all
    # all_workers = Worker.objects.all()
    # print(all_workers)

    # filter by ...
    # workers_filtered = Worker.objects.filter(salary=0)
    # print(workers_filtered)

    # for i in all_workers:
    #    print(f'{i.id} {i.second_name} {i.name} {i.salary}')

    # get page
    # return render(request, 'index.html')

    workers = Worker.objects.all()
    return render(request, 'index.html', context={'data': workers})


class WorkerView(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer