FROM node:18-alpine as frontend-build

WORKDIR /frontend

# Create necessary directories
RUN mkdir -p public src

# Copy package files and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy all frontend files
COPY frontend/ ./

# Build the React app
RUN npm run build

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=frontend-build /frontend/build /app/frontend/build

EXPOSE 8000

CMD ["python", "run.py"]
