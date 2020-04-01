# Generated by Django 2.2.11 on 2020-03-31 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
        ('cursos', '0002_auto_20200331_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno', to='alunos.Aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='cursos.Curso')),
            ],
        ),
    ]
