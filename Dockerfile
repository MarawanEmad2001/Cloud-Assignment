#base image
FROM python
ENV DIR=/cloud
COPY . $cloud
WORKDIR $cloud
CMD python pyfile.py 