
# ------------------------------
# Superset Startup Script (Windows)
# ------------------------------

# 1. Activate the virtual environment
& "C:\superset-venv\Scripts\Activate.ps1"

# 2. Set required environment variables
$env:FLASK_APP = "superset"
$env:SUPERSET_CONFIG_PATH = "C:\superset-venv\superset_config.py"

# 3. Start Celery worker in a separate visible terminal  # celery start krva mate  jwt token set krvi
# Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -NoExit -Command "celery --app=superset.tasks.celery_app:app worker --pool=solo -Ofair"' -WindowStyle Normal

# (--optional--)
# 1st method: Start Celery in background - (logs are not visible)
# Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -Command "celery --app=superset.tasks.celery_app:app worker --pool=solo -Ofair"' -WindowStyle Hidden

# 2nd method: Start Celery in same terminal so logs are visible
# Start-Job { celery --app=superset.tasks.celery_app:app worker --pool=solo -Ofair }
# (--optional--)

# 4. Wait a few seconds to allow Celery to fully start
# Start-Sleep -Seconds 5

# 5. Start Superset web server
superset run -p 8088 --with-threads --reload --debugger

pause
