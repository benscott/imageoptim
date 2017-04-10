# ImageOptimAPI

Python class for accessing the [Image Optim API](https://imageoptim.com/api)

"Web service for image compression. Easily resize and optimize images on your server."

Supports image resiszing to power of 2 dimensions, for optimal use with THREE.WebGLRenderer.


# Requirements

* [Python 3.x](https://www.python.org)
* [Requests](http://docs.python-requests.org/en/master/)
* [Pillow](https://python-pillow.org/)

You also need to sign up for an account at https://im2.io/register, providing your username to API calls (see usage)


# Installation

Pip install:

    pip install -e git+git@github.com:benscott/image_optim_api.git#egg=image_optim_api


# Usage

Optimize an image

    api = ImageOptimAPI(USERNAME);
    img = api.image_from_file_path(file_path)
    img.save(NEW_FILE)


Upscale & optimize an image

    api = ImageOptimAPI(USERNAME);
    img = api.image_from_file_path(file_path, {'size': '8192x4096', 'fit': True})
    img.save(NEW_FILE)


ImageOptim API options can be passsed in as a dict of attribute:value. If an attribute requires no value (e.g. fit), set value to True.
See [API Documentation](https://im2.io/api/post) for details of API options.


Resize an image to power of 2 (optimised for THREE.WebGLRenderer)

    api = ImageOptimAPI(USERNAME);
    img = api.image_from_file_path(file_path, resize_pow2=True)
    img.save(NEW_FILE)


You can also use a callback (for async sort of stuff)

    image_optim = ImageOptim()

    def done(results):
        print(results)

    image_optim.optimize('/path/to/image.jpg', done)
