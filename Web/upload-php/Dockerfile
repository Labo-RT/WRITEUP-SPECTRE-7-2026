FROM php:8.2-apache

RUN a2enmod rewrite

COPY html/ /var/www/html/

COPY flag.txt /

RUN chmod 777 /flag.txt

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]
