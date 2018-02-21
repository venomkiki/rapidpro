# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 09:15
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations, models


SQL = """
-- index for fast fetching of unsquashed rows
CREATE INDEX msgs_systemlabel_unsquashed
ON msgs_systemlabel(org_id, label_type) WHERE NOT is_squashed;

-- this is performed in Python-land now
DROP FUNCTION temba_squash_systemlabel(INTEGER, CHAR(1));

---------------------------------------------------------------------------------
-- Increment or decrement a system label
---------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION
  temba_insert_system_label(_org_id INT, _label_type CHAR(1), _count INT)
RETURNS VOID AS $$
BEGIN
  INSERT INTO msgs_systemlabel("org_id", "label_type", "count", "is_squashed") VALUES(_org_id, _label_type, _count, FALSE);
END;
$$ LANGUAGE plpgsql;
"""


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0079_populate_msg_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemlabel',
            name='is_squashed',
            field=models.BooleanField(default=False, help_text='Whether this row was created by squashing'),
        ),
        migrations.RunSQL(SQL),
    ]
