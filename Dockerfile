FROM nginx:1.25-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY deploy/security-headers.conf /etc/nginx/snippets/security-headers.conf
# Only the generated publish set is served; sources stay out of the image.
COPY dist/ /usr/share/nginx/html/
EXPOSE 80
