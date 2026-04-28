FROM node:20-bullseye-slim
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm install --production=false
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm","start"]
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Expose port
EXPOSE 3000

# Run the application
CMD ["sh", "-c", "npm start -- -H 0.0.0.0 -p ${PORT:-3000}"]
