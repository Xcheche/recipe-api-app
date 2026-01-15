"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the database."""

    def check(self, databases=None):
        """Check database connection."""
        return connections["default"].cursor()
      
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                self.check(databases=["default"])
                db_conn = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
