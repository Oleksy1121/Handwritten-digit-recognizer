# nodejs image
FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

# build production app
RUN npm run build

# use ngix image, version alpine (small weight)
FROM nginx:stable-alpine

# copy static files from build operation to Ngix server dir
COPY --from=build /app/build /usr/share/nginx/html

# set listening port
EXPOSE 80

# run ngix in "foreground" option
CMD ["nginx", "-g", "daemon off;"]