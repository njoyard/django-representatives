import json
from representatives.models import Representative
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        result = []
        personal_fields = ("first_name", "last_name", "full_name", "birth_place", "cv")
        gender_dict = dict(Representative.GENDER)
        for representative in Representative.objects.all():
            reps = {"id": representative.remote_id}
            reps["personal"] = {field: getattr(representative, field) for field in personal_fields}
            reps["personal"]["gender"] = gender_dict[representative.gender]
            reps["personal"]["birth_date"] = representative.birth_date.strftime("%F") if representative.birth_date else None

            result.append(reps)

        print json.dumps(result, indent=4)
