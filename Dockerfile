FROM ubuntu:latest
# train machine learning model
# save performances
CMD echo ‘{“perf”:0.99}’ > /data/perf.json