# Use an official Node.js runtime as a parent image
FROM node:16-alpine
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
ENV NODE_ENV production
ENV NEXT_PUBLIC_BACKEND_URL $NEXT_PUBLIC_BACKEND_URL

# Start the application
CMD ["yarn", "start"]