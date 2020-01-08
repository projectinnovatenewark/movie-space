# FROM mhart/alpine-node:11 AS builder
# WORKDIR /frontend

# COPY . .
# RUN yarn run build

# FROM mhart/alpine-node
# RUN yarn global add serve

# WORKDIR /frontend
# COPY --from=builder /frontend/build .
# CMD ["serve", "-p", "80", "-s", "."]

# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /frontend

# add `/frontend/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache frontend dependencies
COPY package.json /frontend/package.json
RUN yarn install --silent

# start app
CMD ["yarn", "start"]