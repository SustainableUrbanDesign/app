#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # This allows easy placement of apps within the interior
    # main directory.
    # current_path = Path(__file__).parent.resolve()
    # sys.path.append(str(current_path / "platform"))
    
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
