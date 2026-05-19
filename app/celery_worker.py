import sys
from app.celery_app import celery

if __name__ == "__main__":
    sys.argv = [
        "celery",
        "-A",
        "app.celery_app:celery",
        "worker",
        "--loglevel=info"
    ]

    from celery.bin.celery import main
    main()
