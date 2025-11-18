# -----------------------------
# 1. Use lightweight Python base
# -----------------------------
FROM python:3.10-slim

# -----------------------------
# 2. Set working dir
# -----------------------------
WORKDIR /app

# -----------------------------
# 3. Copy requirements first for caching
# -----------------------------
COPY requirements.txt .

# -----------------------------
# 4. Install dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# 5. Copy all project files
# -----------------------------
COPY . .

# -----------------------------
# 6. Expose Flask port
# -----------------------------
EXPOSE 5000

# -----------------------------
# 7. Production server using gunicorn
# -----------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

