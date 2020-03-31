FROM ruby:2.7-alpine as jekyll-base

RUN apk add --no-cache build-base gcc bash cmake git

RUN gem install jekyll

EXPOSE 4000

WORKDIR /site

# docker run --rm -v `pwd`:/site -p 4000:4000 -it jekyll /bin/bash
# script/bootstrap
# bundle exec jekyll serve --force_polling -H 0.0.0.0 -P 4000
