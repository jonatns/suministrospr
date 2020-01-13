# Generated by Django 2.2.9 on 2020-01-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suministros', '0002_auto_20200113_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministro',
            name='municipality',
            field=models.CharField(choices=[('adjuntas', 'Adjuntas'), ('aguada', 'Aguada'), ('aguadilla', 'Aguadilla'), ('aguas buenas', 'Aguas Buenas'), ('aibonito', 'Aibonito'), ('anasco', 'Anasco'), ('arecibo', 'Arecibo'), ('arroyo', 'Arroyo'), ('barceloneta', 'Barceloneta'), ('barranquitas', 'Barranquitas'), ('bayamon', 'Bayamon'), ('cabo rojo', 'Cabo Rojo'), ('caguas', 'Caguas'), ('camuy', 'Camuy'), ('canovanas', 'Canovanas'), ('carolina', 'Carolina'), ('catano', 'Catano'), ('cayey', 'Cayey'), ('ceiba', 'Ceiba'), ('ciales', 'Ciales'), ('cidra', 'Cidra'), ('coamo', 'Coamo'), ('comerio', 'Comerio'), ('corozal', 'Corozal'), ('culebra', 'Culebra'), ('dorado', 'Dorado'), ('fajardo', 'Fajardo'), ('florida', 'Florida'), ('guanica', 'Guanica'), ('guayama', 'Guayama'), ('guayanilla', 'Guayanilla'), ('guaynabo', 'Guaynabo'), ('gurabo', 'Gurabo'), ('hatillo', 'Hatillo'), ('hormigueros', 'Hormigueros'), ('humacao', 'Humacao'), ('isabela', 'Isabela'), ('jayuya', 'Jayuya'), ('juana diaz', 'Juana Diaz'), ('juncos', 'Juncos'), ('lajas', 'Lajas'), ('lares', 'Lares'), ('las marias', 'Las Marias'), ('las piedras', 'Las Piedras'), ('loiza', 'Loiza'), ('luquillo', 'Luquillo'), ('manati', 'Manati'), ('maricao', 'Maricao'), ('maunabo', 'Maunabo'), ('mayaguez', 'Mayaguez'), ('moca', 'Moca'), ('morovis', 'Morovis'), ('naguabo', 'Naguabo'), ('naranjito', 'Naranjito'), ('orocovis', 'Orocovis'), ('patillas', 'Patillas'), ('penuelas', 'Penuelas'), ('ponce', 'Ponce'), ('quebradillas', 'Quebradillas'), ('rincon', 'Rincon'), ('rio grande', 'Rio Grande'), ('sabana grande', 'Sabana Grande'), ('salinas', 'Salinas'), ('san german', 'San German'), ('san juan', 'San Juan'), ('san lorenzo', 'San Lorenzo'), ('san sebastian', 'San Sebastian'), ('santa isabel', 'Santa Isabel'), ('toa alta', 'Toa Alta'), ('toa baja', 'Toa Baja'), ('trujillo alto', 'Trujillo Alto'), ('utuado', 'Utuado'), ('vega alta', 'Vega Alta'), ('vega baja', 'Vega Baja'), ('vieques', 'Vieques'), ('villalba', 'Villalba'), ('yabucoa', 'Yabucoa'), ('yauco', 'Yauco')], max_length=255),
        ),
    ]
