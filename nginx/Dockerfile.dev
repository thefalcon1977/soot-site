FROM tiangolo/nginx-rtmp:latest

# Create HLS and log directories with permissive permissions
RUN mkdir -p /tmp/hls /var/log/nginx \
    && chmod -R 755 /tmp/hls /var/log/nginx

# Remove default.conf to avoid conflicts
RUN rm -f /etc/nginx/conf.d/default.conf

# Expose ports for HTTP and RTMP
EXPOSE 8080 1935

# Run Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]