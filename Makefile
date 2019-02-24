build-image:
	docker build -t markvl/blog-builder .

compile:
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder acrylamid compile
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder compass compile

update:
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder acrylamid compile

aco:
	docker run --init -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) -p 8080:8000 markvl/blog-builder acrylamid aco || true

imageoptim:
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder jpegoptim --strip-com --strip-exif --strip-iptc --strip-xmp assets/images/*.jpg
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder optipng assets/images/*.png

publish:
	rm -rf output
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder jpegoptim --quiet --strip-com --strip-exif --strip-iptc --strip-xmp assets/images/*.jpg
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder optipng assets/images/*.png
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder acrylamid compile
	docker run -it --rm -v $$(pwd):/blog -u $$(id -u $$(whoami)):$$(id -g $$(whoami)) markvl/blog-builder compass compile
	rsync -rtuvz --delete output/ knuth:/var/www/www.vlent.nl/html
