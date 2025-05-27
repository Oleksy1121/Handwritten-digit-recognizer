FROM python:3.12-slim-bookworm AS python_build

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend/
COPY training/model_builder.py ./training/model_builder.py
COPY training/image_transforms.py ./training/image_transforms.py

EXPOSE 8000

CMD [ "uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000" ]