FROM node:20-alpine AS base

WORKDIR /app

COPY package.json ./
# Production build немесе dev режиміне дайындық
RUN npm install

COPY . .

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["npm", "run", "dev"]
