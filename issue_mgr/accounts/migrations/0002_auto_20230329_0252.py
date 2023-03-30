# Generated by Django 4.1.7 on 2023-03-29 02:52

from django.db import migrations

def populate_team(apps, schemaeditor):
    defaults = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team"
    }
    Team= apps.get_model ("accounts","Team")
    for key, desc in defaults.items():
        team_obj= Team(name=key, descrption=desc)
        team_obj.save()


def populate_roles(apps, schemaeditor):
    defaults= {
        "developer": "A person who writes code",
        "scrum master": "The dev team's coach",
        "product owner": "The person who writes software for the team"
    }
    Role= apps.get_model ("accounts","Role")
    for key, desc in defaults.items():
        team_obj= Role(name=key, description=desc)
        team_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_team),
        migrations.RunPython(populate_roles)
    ]
