FROM node:22-slim AS base

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm ci

COPY . .
RUN npm run build

ENV NODE_ENV=production
ENV SIGMA_WORKSPACE=/data

EXPOSE 3000
CMD ["npm", "start"]
