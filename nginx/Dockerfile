FROM nginx:1.24.0-alpine

RUN apk add --update nginx
# Replace the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf 

# RUN mkdir -p /tmp/nginx/vue-single-page-app
RUN mkdir -p /var/log/nginx
# RUN mkdir -p /var/www/html

# WORKDIR /tmp/nginx/vue-single-page-app

# COPY . .


# RUN chown nginx:nginx /var/www/html
CMD ["nginx", "-g", "daemon off;"]