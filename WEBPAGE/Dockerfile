# Use the official PHP image with Apache
FROM php:8.2-apache

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Copy website files to Apache server root
COPY src/ /var/www/html/

# Expose port 80
EXPOSE 80
