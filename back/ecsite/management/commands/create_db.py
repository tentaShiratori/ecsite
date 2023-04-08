from django.core.management.base import BaseCommand, CommandError
import MySQLdb
from django.conf import settings


class Command(BaseCommand):
    help = "Drop database"

    def handle(self, *args, **options):
        print("create database!")
        db = MySQLdb.connect(
            host=settings.DATABASES["default"]["HOST"],
            user=settings.DATABASES["default"]["USER"],
            passwd=settings.DATABASES["default"]["PASSWORD"],
        )
        cursor = db.cursor()
        sql = f"CREATE DATABASE IF NOT EXISTS `{settings.DATABASES['default']['NAME']}` DEFAULT CHARACTER SET `utf8mb4`"
        cursor.execute(sql)
        db.close()
