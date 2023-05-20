#!/usr/bin/env python
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
    # django.setup() # 没有这一行会报raise AppRegistryNotReady("Apps aren't loaded yet.") django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
