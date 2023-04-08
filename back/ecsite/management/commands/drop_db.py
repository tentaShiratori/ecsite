from django.core.management.base import BaseCommand, CommandError
import MySQLdb
from django.conf import settings


class Command(BaseCommand):
    help = "Drop database"

    def handle(self, *args, **options):
        print("Drop database!")
        db = MySQLdb.connect(
            host=settings.DATABASES["default"]["HOST"],
            user=settings.DATABASES["default"]["USER"],
            passwd=settings.DATABASES["default"]["PASSWORD"],
        )
        cursor = db.cursor()
        sql = f"DROP DATABASE IF EXISTS `{settings.DATABASES['default']['NAME']}`"
        cursor.execute(sql)
        db.close()
