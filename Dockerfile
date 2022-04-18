FROM jekyll/jekyll 

EXPOSE 4000
WORKDIR /site

# docker build -t homepage .   
# docker run --rm --cpus=1 -v (pwd):/site -p 4000:4000 -it homepage /bin/bash
# script/bootstrap
# bundle exec jekyll serve --force_polling -H 0.0.0.0 -P 4000
