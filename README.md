# Flask Rebar REST API Demo
This code accompanies the [blog post ](https://think-engineer.com/blog/) discussing how to write a reliable REST API using, Python, Flask and Rebar, written by [Adam](https://github.com/amitchone) for [Think Engineer](www.think-engineer.com).

### How to use
If you really don't want to read the [blog post](https://think-engineer.com/blog/) then simply clone the repository to a machine that has Docker installed, build the image and run:
```sh
git clone https://github.com/Think-Engineer/flask-rebar_demo
cd flask-rebar_demo
docker build -t flask-rebar_demo .
docker run -p 8000:8000 flask-rebar_demo
```
And then read the blog post!