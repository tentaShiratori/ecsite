# Use an official Node.js runtime as a parent image
FROM node:16-alpine
ARG NODE_ENV
ARG NEXT_PUBLIC_BACKEND_URL
# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json
COPY ./package.json ./
COPY ./yarn.lock ./

# Install dependencies
RUN yarn install --production


# Copy the rest of the application code
COPY . .

# Build the Next.js application
RUN yarn build

# Expose port 3000
EXPOSE 3000

# Set the NODE_ENV environment variable to production
RUN touch .env.production
RUN echo "NODE_ENV=$NODE_ENV" >> .env.production
RUN echo "NEXT_PUBLIC_BACKEND_URL=$NEXT_PUBLIC_BACKEND_URL" >> .env.production

# Start the application
CMD ["yarn", "start"]