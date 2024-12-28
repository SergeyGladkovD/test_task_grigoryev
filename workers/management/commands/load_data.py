import openpyxl
from django.core.management.base import BaseCommand

from workers.models import Worker


class Command(BaseCommand):
    """Команда загружает из Excel файла в базу данных."""

    help = "Load data from Excel file into database"

    def handle(self, *args, **options):
        workbook = openpyxl.load_workbook("Workers.xlsx")
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            worker_id, full_name, brigade_number, salary, specialization = row
            Worker.objects.create(
                id=worker_id,
                full_name=full_name,
                brigade_number=brigade_number,
                salary=salary,
                specialization=specialization,
            )

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
